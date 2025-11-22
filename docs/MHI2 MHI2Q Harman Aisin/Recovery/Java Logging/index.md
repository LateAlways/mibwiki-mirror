# Java Logging

The Harman units use a Java program to handle the GUI on the unit, as well as much of the background processing.

When issues occur, sometime the logging from this Java app can help narrow down the problem.

There are "official" build in ways to enable / filter this logging, but they rely on a closed source esolutions program & protocol which is not available at this time.

Instead of using this, we can re-route the logging to file on SD card.


You will need a way of editing the `/etc/boot/startup.sh` file on your unit. This could with a copy of `nano`, or WinSCP over ssh connection, or copy it to SD card, edit on computer, then copy back in place. 

You will need to ensure the system partition is writable to edit/replace this file, eg.

```javascript
mount -uw /mnt/system
```


### Modifying`startup.sh`

Search for the `start_hmi()` function, it should look like this:

```javascript
start_hmi()
{
	cd /mnt/app/eso

	if [[ $QUIET = 1 ]]; then
		bin/runHMI.sh > /dev/null 2>&1
	else
		bin/runHMI.sh
	fi
}
```

Rename this to `start_hmi_orig()` then add a replacement function that looks like:

```javascript
start_hmi()
{
	waitfor /fs/sda0 5

	logtarget=/dev/null
	if [ -d /fs/sda0/Logs ]; then
		mount -uw /fs/sda0
		logtarget=/fs/sda0/Logs/mmxlog.txt
		if [ -e $logtarget ]; then
			mv $logtarget ${logtarget}.1
		fi
	fi

	cd /mnt/app/eso

	bin/runHMI.sh 2>&1 | tee ${logtarget}
}
```

If your original function looked different, update the new one to match, eg. make sure the same directory is used for `cd /mnt/app/eso` and the same final script ( `bin/runHMI.sh` ) is run.


With this change in place, after a reboot, the unit will pause during startup until SD1 is mounted (can take a second or two) then run the main GUI java app with all logging output redirected to the file `Logs/mmxlog.txt` on the SD card.

If no SD card is inserted, startup will be delayed 5 seconds while it looks for one, so you might not want to leave this patch in place permanently if SD card is not used.


With this startup patch you'll get a fair bit of the internal logging coming out, though the standard log levels isn't very verbose. 

There are ways to adjust the verbosity of different module in use, but I'm not certain which method actually works.


Can try changing things in these files: 

* /eso/hmi/lsd/config/logging.properties
*  /eso/hmi/lsd/traceConfig.properties


Also in the service screens on the unit, there's places to set trace levels for logging domains - I'm not sure if setting things there helps as well


Feel free to update this page if the above verbosity settings are tested and you find out what works properly!