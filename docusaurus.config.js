// @ts-check
const { themes: prismThemes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'MIB2 WIKI - Mirror',
  tagline: 'Unofficial mirror of mibwiki.one',
  favicon: 'img/favicon.svg',

  url: 'https://mibwiki.latealways.dev',
  baseUrl: '/',
  trailingSlash: true,

  organizationName: 'LateAlways',
  projectName: 'mibwiki-mirror',

  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',

  markdown: {
    // The docs were scraped from an external wiki and contain characters
    // (stray "<", "{", etc.) that are safe in plain Markdown but would
    // break MDX's JSX-expression parsing. Parse .md as classic Markdown.
    format: 'detect',
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/LateAlways/mibwiki-mirror/edit/main/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themes: ['@easyops-cn/docusaurus-search-local'],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'MIB2 WIKI - Mirror',
        items: [
          {
            href: 'https://github.com/LateAlways/mibwiki-mirror',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: 'Unofficial, read-only mirror of mibwiki.one — not affiliated with its authors.',
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

module.exports = config;
