import { defineCollection, z } from 'astro:content';

const papers = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    authors: z.array(z.string()).default([]),
    arxiv_id: z.string(),
    url: z.string().url(),
    pdf_url: z.string().url().optional(),
    published: z.coerce.date(),
    collected: z.coerce.date(),
    category: z.string(),
    tags: z.array(z.string()).default([]),
    one_liner: z.string(),
    score: z.number().min(0).max(10),
    source: z.string(),
    depth: z.enum(['abstract', 'full_pdf']).default('abstract'),
  }),
});

export const collections = { papers };
