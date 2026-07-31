#!/usr/bin/env python3
"""
EsoTrace Viewer — opens and displays CTracer/EsoTrace binary log files
from Audi MHS2 head units.

Binary format (big-endian, stream of packets):
  Each packet: [uint32 payload_length][payload]
  Payload:     [uint8 message_type][type-specific body]

Key message types:
  0x00 INIT         — file header, process name
  0x03 CREATE_ENTITY— channel name/ID registration
  0x04 LOG_DATA     — single log entry
  0x31 BULK_LOG_DATA— batch of log entries
"""

import struct
import sys
import os
import csv
import io
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import datetime

# ── Constants ─────────────────────────────────────────────────────────────────

LEVEL_NAMES = {
    0: 'trace',
    1: 'debug',
    2: 'info',
    3: 'warn',
    4: 'ERROR',
    5: 'FATAL',
    6: 'off',
    7: 'none',
    8: 'disabled',
}

LEVEL_COLORS_FG = {
    0: '#888888',  # trace
    1: '#5555cc',  # debug
    2: '#007700',  # info
    3: '#cc7700',  # warn
    4: '#cc2200',  # ERROR
    5: '#880000',  # FATAL
}

MSG_TYPE_NAMES = {
    0:   'INIT',
    1:   'EXIT',
    2:   'TIME_SYNC',
    3:   'CREATE_ENTITY',
    4:   'LOG_DATA',
    5:   'DROPPED_DATA',
    16:  'TOGGLE_ENTITY',
    17:  'CHANGE_LEVEL',
    18:  'EXECUTE_CALLBACK',
    19:  'REGISTER_TIMEZONE',
    20:  'UPDATE_TIMEZONE',
    21:  'SYNC_MARKER',
    22:  'FILE_REQUEST',
    23:  'FILE_STATUS',
    24:  'FILE_TRANSFER',
    32:  'LOGGER_TIME',
    33:  'LOGGER_DATA',
    48:  'BULK_CREATE_ENTITY',
    49:  'BULK_LOG_DATA',
    50:  'BULK_CHANGE_LEVEL',
    128: 'MLP',
}


# ── Parser ─────────────────────────────────────────────────────────────────────

class ParseError(Exception):
    pass


class ByteReader:
    """Reads typed big-endian values from a bytes object."""

    def __init__(self, data, start=0):
        self.data = data
        self.pos = start

    @property
    def remaining(self):
        return len(self.data) - self.pos

    def read_raw(self, n):
        if self.pos + n > len(self.data):
            raise ParseError(f'EOF: need {n} bytes at {self.pos}, have {len(self.data) - self.pos}')
        chunk = self.data[self.pos:self.pos + n]
        self.pos += n
        return chunk

    def u8(self):
        b = self.data[self.pos]
        self.pos += 1
        return b

    def i8(self):
        v = self.u8()
        return v if v < 128 else v - 256

    def u16(self):
        return struct.unpack_from('>H', self.data, self._adv(2))[0]

    def i16(self):
        return struct.unpack_from('>h', self.data, self._adv(2))[0]

    def u32(self):
        return struct.unpack_from('>I', self.data, self._adv(4))[0]

    def i32(self):
        return struct.unpack_from('>i', self.data, self._adv(4))[0]

    def i64(self):
        return struct.unpack_from('>q', self.data, self._adv(8))[0]

    def bool_(self):
        return self.u8() != 0

    def _adv(self, n):
        if self.pos + n > len(self.data):
            raise ParseError(f'EOF: need {n} at {self.pos}')
        p = self.pos
        self.pos += n
        return p

    def esotrace_string(self):
        """Read a length-prefixed string in ESO serialization format.
           [uint8 encoding][uint16 char_count][bytes]
        """
        encoding = self.u8()
        char_count = self.u16()
        if encoding == 0:       # UTF-8
            byte_count = char_count
            raw = self.read_raw(byte_count)
            return raw.decode('utf-8', errors='replace')
        elif encoding == 1:     # UTF-16 BE
            byte_count = char_count * 2
            raw = self.read_raw(byte_count)
            return raw.decode('utf-16-be', errors='replace')
        else:                   # fallback: treat as raw bytes
            byte_count = char_count
            raw = self.read_raw(byte_count)
            return raw.decode('latin-1', errors='replace')

    def var_bytes(self):
        """Read [uint32 length][bytes]."""
        length = self.u32()
        return self.read_raw(length)


def format_timestamp(ts_us):
    """Convert microseconds-since-Unix-epoch to HH:MM:SS.mmm string."""
    try:
        secs = ts_us / 1_000_000
        dt = datetime.datetime.utcfromtimestamp(secs)
        ms = (abs(ts_us) % 1_000_000) // 1000
        return dt.strftime(f'%H:%M:%S.{ms:03d}')
    except (OSError, OverflowError, ValueError):
        return str(ts_us)


def parse_log_data_body(r, entities):
    """Parse a LOG_DATA body (without the leading type byte)."""
    timestamp = r.i64()
    level = r.i16()
    modifiers = r.i16()
    channel_id = r.i32()
    source_id = r.i32()
    log_type = r.i16()
    data = r.var_bytes()

    if log_type == 1:
        text = data.decode('utf-8', errors='replace').rstrip('\x00')
    else:
        text = f'[binary type={log_type} len={len(data)}]'

    channel_name = entities.get(channel_id, f'ch#{channel_id}')
    return {
        'kind': 'log',
        'timestamp': timestamp,
        'ts_str': format_timestamp(timestamp),
        'level': level,
        'level_name': LEVEL_NAMES.get(level, str(level)),
        'channel_id': channel_id,
        'channel_name': channel_name,
        'source_id': source_id,
        'text': text,
    }


def parse_file(data):
    """
    Parse an EsoTrace binary file.

    Returns (log_entries, metadata) where:
      log_entries — list of dicts with fields: timestamp, ts_str, level,
                    level_name, channel_name, source_id, text
      metadata    — dict with process_name, total_packets, parse_errors
    """
    entities = {}      # channel_id -> name
    log_entries = []
    process_name = None
    total_packets = 0
    parse_errors = 0

    stream = ByteReader(data)

    while stream.remaining >= 4:
        try:
            payload_len = stream.u32()
        except ParseError:
            break

        if payload_len == 0:
            continue
        if payload_len > stream.remaining:
            # Truncated file — stop
            break

        payload = stream.read_raw(payload_len)
        total_packets += 1

        if len(payload) == 0:
            continue

        msg_type = payload[0]
        body = payload[1:]
        r = ByteReader(body)

        try:
            if msg_type == 0:   # INIT
                revision = r.i8()
                name = r.esotrace_string()
                max_entities = r.i32()
                process_name = name

            elif msg_type == 3:  # CREATE_ENTITY
                name = r.esotrace_string()
                etype = r.i16()
                eid = r.i32()
                level = r.i16()
                has_parent = r.bool_()
                if has_parent:
                    r.i16()  # parentType
                    r.i32()  # parentId
                entities[eid] = name

            elif msg_type == 4:  # LOG_DATA
                entry = parse_log_data_body(r, entities)
                log_entries.append(entry)

            elif msg_type == 49:  # BULK_LOG_DATA
                count = r.i32()
                for _ in range(count):
                    try:
                        entry = parse_log_data_body(r, entities)
                        log_entries.append(entry)
                    except ParseError:
                        parse_errors += 1
                        break

            elif msg_type == 48:  # BULK_CREATE_ENTITY — same pattern as bulk log
                count = r.i32()
                for _ in range(count):
                    try:
                        name = r.esotrace_string()
                        etype = r.i16()
                        eid = r.i32()
                        level = r.i16()
                        has_parent = r.bool_()
                        if has_parent:
                            r.i16()
                            r.i32()
                        entities[eid] = name
                    except ParseError:
                        parse_errors += 1
                        break

            # All other message types are silently skipped

        except ParseError:
            parse_errors += 1

    return log_entries, {
        'process_name': process_name,
        'total_packets': total_packets,
        'parse_errors': parse_errors,
        'entity_count': len(entities),
    }


# ── GUI ────────────────────────────────────────────────────────────────────────

class EsoTraceViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('EsoTrace Viewer')
        self.geometry('1380x750')
        self.minsize(800, 400)

        self.all_records = []       # full merged + sorted list
        self.filtered_records = []  # after filters, for detail lookup
        self.loaded_files = []      # list of dicts: {path, fname, count, process_name}
        self._filter_job = None

        self.filter_var = tk.StringVar()
        self.filter_var.trace_add('write', self._schedule_filter)

        self.level_vars = {}

        self._build_ui()
        self._apply_filters()

    # ── UI construction ────────────────────────────────────────────────────────

    def _build_ui(self):
        self._build_menu()
        self._build_toolbar()
        self._build_main_area()
        self._build_statusbar()

    def _build_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open...', accelerator='Ctrl+O', command=self.open_file)
        file_menu.add_command(label='Add file(s) to session...', accelerator='Ctrl+A', command=self.add_files)
        file_menu.add_separator()
        file_menu.add_command(label='Show loaded files...', command=self.show_loaded_files)
        file_menu.add_command(label='Close all', command=self.close_all)
        file_menu.add_separator()

        export_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label='Export', menu=export_menu)
        export_menu.add_command(
            label='Plain text log — visible entries...',
            accelerator='Ctrl+S',
            command=lambda: self.export_log(all_records=False),
        )
        export_menu.add_command(
            label='Plain text log — all entries...',
            command=lambda: self.export_log(all_records=True),
        )
        export_menu.add_separator()
        export_menu.add_command(
            label='CSV — visible entries...',
            command=lambda: self.export_csv(all_records=False),
        )
        export_menu.add_command(
            label='CSV — all entries...',
            command=lambda: self.export_csv(all_records=True),
        )

        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)

        self.bind('<Control-o>', lambda e: self.open_file())
        self.bind('<Control-a>', lambda e: self.add_files())
        self.bind('<Control-s>', lambda e: self.export_log(all_records=False))

    def _build_toolbar(self):
        tb = tk.Frame(self, bd=1, relief=tk.RAISED, padx=4, pady=3)
        tb.pack(fill=tk.X, side=tk.TOP)

        tk.Button(tb, text='Open File', command=self.open_file, width=10).pack(side=tk.LEFT, padx=(0, 4))
        tk.Button(tb, text='Add File(s)', command=self.add_files, width=10).pack(side=tk.LEFT, padx=(0, 4))
        tk.Button(tb, text='Close All', command=self.close_all, width=9).pack(side=tk.LEFT, padx=(0, 12))

        tk.Label(tb, text='Search:').pack(side=tk.LEFT)
        search_entry = tk.Entry(tb, textvariable=self.filter_var, width=32)
        search_entry.pack(side=tk.LEFT, padx=(4, 16))
        search_entry.bind('<Escape>', lambda e: self.filter_var.set(''))

        tk.Label(tb, text='Levels:').pack(side=tk.LEFT, padx=(0, 4))
        for lvl in [0, 1, 2, 3, 4, 5]:
            var = tk.BooleanVar(value=True)
            self.level_vars[lvl] = var
            color = LEVEL_COLORS_FG.get(lvl, 'black')
            cb = tk.Checkbutton(
                tb,
                text=LEVEL_NAMES[lvl],
                variable=var,
                fg=color,
                activeforeground=color,
                command=self._apply_filters,
            )
            cb.pack(side=tk.LEFT, padx=1)

        tk.Button(tb, text='Clear Search', command=lambda: self.filter_var.set('')).pack(side=tk.LEFT, padx=(16, 0))

    def _build_main_area(self):
        pane = tk.PanedWindow(self, orient=tk.VERTICAL, sashrelief=tk.RAISED, sashwidth=5)
        pane.pack(fill=tk.BOTH, expand=True)

        # ── Table ──────────────────────────────────────────────────────────────
        table_frame = tk.Frame(pane)
        pane.add(table_frame, minsize=150, stretch='always')

        cols = ('ts', 'level', 'channel', 'thread', 'source', 'message')
        self.tree = ttk.Treeview(table_frame, columns=cols, show='headings', selectmode='browse')

        self.tree.heading('ts',      text='Timestamp',  anchor='w')
        self.tree.heading('level',   text='Level',      anchor='center')
        self.tree.heading('channel', text='Channel',    anchor='w')
        self.tree.heading('thread',  text='Thread ID',  anchor='center')
        self.tree.heading('source',  text='File',       anchor='w')
        self.tree.heading('message', text='Message',    anchor='w')

        self.tree.column('ts',      width=105, minwidth=90,  anchor='w',      stretch=False)
        self.tree.column('level',   width=60,  minwidth=50,  anchor='center', stretch=False)
        self.tree.column('channel', width=200, minwidth=100, anchor='w',      stretch=False)
        self.tree.column('thread',  width=90,  minwidth=70,  anchor='center', stretch=False)
        self.tree.column('source',  width=160, minwidth=60,  anchor='w',      stretch=False)
        self.tree.column('message', width=600, minwidth=200, anchor='w',      stretch=True)

        vsb = ttk.Scrollbar(table_frame, orient='vertical',   command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient='horizontal',  command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        for lvl, color in LEVEL_COLORS_FG.items():
            bold = lvl >= 4
            font = ('TkFixedFont', 9, 'bold') if bold else ('TkFixedFont', 9)
            self.tree.tag_configure(f'lvl{lvl}', foreground=color, font=font)

        self.tree.bind('<<TreeviewSelect>>', self._on_select)

        # ── Detail pane ────────────────────────────────────────────────────────
        detail_frame = tk.Frame(pane)
        pane.add(detail_frame, minsize=60, stretch='never')

        detail_label = tk.Label(detail_frame, text='Message detail:', anchor='w', font=('TkDefaultFont', 8))
        detail_label.pack(fill=tk.X, side=tk.TOP)

        self.detail_text = tk.Text(
            detail_frame, wrap=tk.WORD, height=4,
            state=tk.DISABLED, font=('Consolas', 9),
            relief=tk.SUNKEN, bd=1,
        )
        detail_vsb = ttk.Scrollbar(detail_frame, orient='vertical', command=self.detail_text.yview)
        self.detail_text.configure(yscrollcommand=detail_vsb.set)
        detail_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.detail_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ── Export ─────────────────────────────────────────────────────────────────

    def _records_to_export(self, all_records):
        return self.all_records if all_records else self.filtered_records

    def export_log(self, all_records=False):
        records = self._records_to_export(all_records)
        if not records:
            messagebox.showinfo('Export', 'Nothing to export.')
            return

        scope = 'all' if all_records else 'filtered'
        path = filedialog.asksaveasfilename(
            title=f'Export plain text log ({scope})',
            defaultextension='.log',
            filetypes=[('Log files', '*.log'), ('Text files', '*.txt'), ('All files', '*.*')],
        )
        if not path:
            return

        try:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                # Header comment
                f.write(f'# EsoTrace log export — {len(records)} entries ({scope})\n')
                f.write(f'# Exported: {datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}\n')
                if self.loaded_files:
                    for fi in self.loaded_files:
                        f.write(f'# Source: {fi["fname"]}  ({fi["count"]} entries, process: {fi["process_name"] or "unknown"})\n')
                f.write('# Columns: timestamp  level     channel                          thread_id   file                  message\n')
                f.write('#\n')

                # Pre-compute max channel width for alignment (capped at 40)
                max_ch = min(40, max((len(r['channel_name']) for r in records), default=8))

                for rec in records:
                    ts      = rec['ts_str']
                    level   = rec['level_name'].upper().ljust(8)
                    channel = rec['channel_name'][:max_ch].ljust(max_ch)
                    thread  = f'0x{rec["source_id"] & 0xFFFFFFFF:08x}'
                    src     = rec.get('source_file', '')[:22].ljust(22)
                    # Indent continuation lines so multi-line messages stay readable
                    text    = rec['text'].rstrip('\n')
                    lines   = text.split('\n')
                    indent  = ' ' * (12 + 1 + 8 + 1 + max_ch + 1 + 10 + 2 + 22 + 2)
                    body    = ('\n' + indent).join(lines)
                    f.write(f'{ts}  {level}  {channel}  {thread}  {src}  {body}\n')

            messagebox.showinfo('Export complete',
                                f'Exported {len(records)} entries to:\n{os.path.basename(path)}')
        except OSError as e:
            messagebox.showerror('Export failed', str(e))

    def export_csv(self, all_records=False):
        records = self._records_to_export(all_records)
        if not records:
            messagebox.showinfo('Export', 'Nothing to export.')
            return

        scope = 'all' if all_records else 'filtered'
        path = filedialog.asksaveasfilename(
            title=f'Export CSV ({scope})',
            defaultextension='.csv',
            filetypes=[('CSV files', '*.csv'), ('All files', '*.*')],
        )
        if not path:
            return

        try:
            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'Level', 'Channel', 'Thread ID',
                                 'File', 'Channel ID', 'Raw Timestamp', 'Message'])
                for rec in records:
                    writer.writerow([
                        rec['ts_str'],
                        rec['level_name'],
                        rec['channel_name'],
                        f'0x{rec["source_id"] & 0xFFFFFFFF:08x}',
                        rec.get('source_file', ''),
                        rec['channel_id'],
                        rec['timestamp'],
                        rec['text'],
                    ])

            messagebox.showinfo('Export complete',
                                f'Exported {len(records)} entries to:\n{os.path.basename(path)}')
        except OSError as e:
            messagebox.showerror('Export failed', str(e))

    def _build_statusbar(self):
        self.status_var = tk.StringVar(value='Ready — open a file with File > Open or Ctrl+O')
        bar = tk.Label(self, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, padx=4)
        bar.pack(side=tk.BOTTOM, fill=tk.X)

    # ── File loading ───────────────────────────────────────────────────────────

    _FILETYPES = [
        ('All files', '*.*'),
        ('Trace/binary files', '*.trc *.bin *.log *.trace'),
    ]

    def open_file(self):
        """Open one file, replacing any currently loaded session."""
        paths = filedialog.askopenfilenames(title='Open EsoTrace Log File(s)',
                                            filetypes=self._FILETYPES)
        if not paths:
            return
        self.all_records = []
        self.loaded_files = []
        self._load_paths(paths)

    def add_files(self):
        """Add one or more files to the current session (merges + sorts)."""
        paths = filedialog.askopenfilenames(title='Add EsoTrace Log File(s) to session',
                                            filetypes=self._FILETYPES)
        if not paths:
            return
        self._load_paths(paths)

    def close_all(self):
        """Clear all loaded files and records."""
        self.all_records = []
        self.loaded_files = []
        self.filtered_records = []
        self.tree.delete(*self.tree.get_children())
        self.title('EsoTrace Viewer')
        self.status_var.set('Ready — open a file with File > Open or Ctrl+O')
        self.detail_text.config(state=tk.NORMAL)
        self.detail_text.delete('1.0', tk.END)
        self.detail_text.config(state=tk.DISABLED)

    def show_loaded_files(self):
        """Show a popup listing all currently loaded files."""
        if not self.loaded_files:
            messagebox.showinfo('Loaded files', 'No files loaded.')
            return
        win = tk.Toplevel(self)
        win.title('Loaded files')
        win.resizable(True, True)
        win.geometry('640x300')

        cols = ('fname', 'entries', 'process', 'path')
        tv = ttk.Treeview(win, columns=cols, show='headings', selectmode='none')
        tv.heading('fname',   text='Filename')
        tv.heading('entries', text='Entries')
        tv.heading('process', text='Process name')
        tv.heading('path',    text='Full path')
        tv.column('fname',   width=180, stretch=False)
        tv.column('entries', width=70,  anchor='center', stretch=False)
        tv.column('process', width=160, stretch=False)
        tv.column('path',    width=400, stretch=True)

        for fi in self.loaded_files:
            tv.insert('', 'end', values=(fi['fname'], fi['count'],
                                         fi['process_name'] or '(unknown)', fi['path']))

        vsb = ttk.Scrollbar(win, orient='vertical', command=tv.yview)
        hsb = ttk.Scrollbar(win, orient='horizontal', command=tv.xview)
        tv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tv.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        win.grid_rowconfigure(0, weight=1)
        win.grid_columnconfigure(0, weight=1)

        total = sum(fi['count'] for fi in self.loaded_files)
        tk.Label(win, text=f'{len(self.loaded_files)} file(s) loaded — {total} total entries',
                 anchor='w', padx=4).grid(row=2, column=0, columnspan=2, sticky='ew')

    def _load_paths(self, paths):
        """Parse each path and append records to the session, then re-sort."""
        errors = []
        added_total = 0

        for path in paths:
            fname = os.path.basename(path)
            # Skip if already loaded
            if any(fi['path'] == path for fi in self.loaded_files):
                errors.append(f'{fname}: already loaded, skipped.')
                continue

            self.status_var.set(f'Parsing {fname}…')
            self.update_idletasks()

            try:
                with open(path, 'rb') as f:
                    data = f.read()
            except OSError as e:
                errors.append(f'{fname}: {e}')
                continue

            try:
                records, meta = parse_file(data)
            except Exception as e:
                errors.append(f'{fname}: parse error — {e}')
                continue

            # Tag every record with its source filename
            for rec in records:
                rec['source_file'] = fname

            self.all_records.extend(records)
            self.loaded_files.append({
                'path': path,
                'fname': fname,
                'count': len(records),
                'process_name': meta['process_name'],
            })
            added_total += len(records)

        if errors:
            messagebox.showwarning('Some files had errors', '\n'.join(errors))

        # Sort merged records by timestamp so multi-file sessions are in order
        self.all_records.sort(key=lambda r: r['timestamp'])

        self._update_title_and_status()
        self._apply_filters()

    def _update_title_and_status(self):
        n_files = len(self.loaded_files)
        n_records = len(self.all_records)
        if n_files == 0:
            self.title('EsoTrace Viewer')
            self.status_var.set('Ready — open a file with File > Open or Ctrl+O')
        elif n_files == 1:
            fi = self.loaded_files[0]
            proc = fi['process_name'] or '(unknown)'
            self.title(f'EsoTrace Viewer — {fi["fname"]}')
            self.status_var.set(f'{n_records} log entries | process: {proc} | {fi["fname"]}')
        else:
            names = ', '.join(fi['fname'] for fi in self.loaded_files)
            self.title(f'EsoTrace Viewer — {n_files} files')
            self.status_var.set(f'{n_records} log entries from {n_files} files: {names}')

    # ── Filtering ──────────────────────────────────────────────────────────────

    def _schedule_filter(self, *_):
        if self._filter_job:
            self.after_cancel(self._filter_job)
        self._filter_job = self.after(150, self._apply_filters)

    def _apply_filters(self, *_):
        query = self.filter_var.get().lower().strip()
        active_levels = {lvl for lvl, var in self.level_vars.items() if var.get()}

        self.tree.delete(*self.tree.get_children())
        self.filtered_records = []

        for rec in self.all_records:
            lvl = rec.get('level', -1)
            if lvl not in active_levels:
                continue

            if query:
                channel = rec.get('channel_name', '').lower()
                text = rec.get('text', '').lower()
                if query not in channel and query not in text:
                    continue

            self.filtered_records.append(rec)
            thread_hex = f'0x{rec["source_id"] & 0xFFFFFFFF:08x}'
            msg_display = rec['text'].replace('\n', '↵').replace('\r', '')[:300]
            src = rec.get('source_file', '')
            tag = f'lvl{lvl}' if lvl in LEVEL_COLORS_FG else ''
            self.tree.insert(
                '', 'end',
                iid=str(len(self.filtered_records) - 1),
                values=(rec['ts_str'], rec['level_name'], rec['channel_name'],
                        thread_hex, src, msg_display),
                tags=(tag,),
            )

        shown = len(self.filtered_records)
        total = len(self.all_records)
        n_files = len(self.loaded_files)
        if total == 0:
            self.status_var.set('No file loaded — use File > Open or Ctrl+O')
        else:
            file_hint = f'{n_files} file(s)' if n_files > 1 else (self.loaded_files[0]['fname'] if n_files == 1 else '')
            if shown == total:
                self.status_var.set(f'Showing all {shown} entries — {file_hint}')
            else:
                self.status_var.set(f'Showing {shown} of {total} entries (filtered) — {file_hint}')

    # ── Detail view ────────────────────────────────────────────────────────────

    def _on_select(self, _event):
        sel = self.tree.selection()
        if not sel:
            return
        try:
            idx = int(sel[0])
            rec = self.filtered_records[idx]
        except (ValueError, IndexError):
            return

        lines = [
            f'Timestamp : {rec["ts_str"]} (raw: {rec["timestamp"]})',
            f'Level     : {rec["level_name"]} ({rec["level"]})',
            f'Channel   : {rec["channel_name"]} (id: {rec["channel_id"]})',
            f'Thread ID : 0x{rec["source_id"] & 0xFFFFFFFF:08x}',
            f'File      : {rec.get("source_file", "(unknown)")}',
            f'',
            rec['text'],
        ]
        full = '\n'.join(lines)

        self.detail_text.config(state=tk.NORMAL)
        self.detail_text.delete('1.0', tk.END)
        self.detail_text.insert('1.0', full)
        self.detail_text.config(state=tk.DISABLED)


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app = EsoTraceViewer()
    if len(sys.argv) > 1:
        # Allow passing one or more files as command-line arguments
        paths = sys.argv[1:]
        app.after(100, lambda p=paths: app._load_paths(p))
    app.mainloop()
