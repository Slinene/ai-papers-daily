import { defineConfig } from 'astro/config';

const SITE = process.env.SITE_URL || 'https://slinene.github.io';
const BASE = process.env.BASE_PATH || '/ai-papers-daily';

export default defineConfig({
  site: SITE,
  base: BASE,
  trailingSlash: 'ignore',
  output: 'static',
  // sitemap removed: @astrojs/sitemap@3.2.1 crashes on build with
  // "Cannot read properties of undefined (reading 'reduce')". We have RSS
  // for feed discovery; sitemap isn't critical for this site.
  integrations: [],
  markdown: {
    shikiConfig: {
      theme: 'github-light',
      wrap: true,
    },
  },
});
