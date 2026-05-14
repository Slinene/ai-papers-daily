import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const papers = (await getCollection('papers')).sort(
    (a, b) => b.data.published.valueOf() - a.data.published.valueOf()
  );
  return rss({
    title: 'AI Papers Daily',
    description: 'Daily AI / RecSys papers, summarized by an agent.',
    site: context.site ?? 'https://example.github.io',
    items: papers.slice(0, 50).map(p => ({
      title: p.data.title,
      pubDate: p.data.published,
      description: p.data.one_liner,
      link: `/paper/${p.slug}`,
      categories: [p.data.category, ...p.data.tags],
    })),
  });
}
