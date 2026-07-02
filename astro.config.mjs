import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

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
    remarkPlugins: [remarkMath],
    // throwOnError/strict false: never break the build on odd LaTeX; render
    // the offending expression in red instead of failing the whole site.
    rehypePlugins: [[rehypeKatex, { throwOnError: false, strict: false }]],
    shikiConfig: {
      theme: 'github-light',
      wrap: true,
    },
  },
});
