import { defineCollection, z } from 'astro:content';

const papers = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),                      // English original (from arXiv)
    title_zh: z.string().optional(),        // Chinese translation
    authors: z.array(z.string()).default([]),
    affiliations: z.array(z.string()).default([]),  // 大学 / 公司 / 实验室
    arxiv_id: z.string(),
    url: z.string().url(),
    pdf_url: z.string().url().optional(),
    published: z.coerce.date(),
    collected: z.coerce.date(),
    category: z.string(),
    direction: z.string().optional(),       // 一句话方向归属
    tags: z.array(z.string()).default([]),
    one_liner: z.string(),
    practical_value: z.string().optional(), // markdown：对从业者的可借鉴点
    score: z.number().min(0).max(10),
    source: z.string(),
    depth: z.enum(['abstract', 'full_pdf']).default('abstract'),
  }),
});

const news = defineCollection({
  type: 'content',
  schema: z.object({
    date: z.coerce.date(),
    collected: z.coerce.date(),
    topic_count: z.number().int(),
    item_count: z.number().int(),
    topics: z.array(z.object({
      title: z.string(),
      summary: z.string(),
      tags: z.array(z.string()).default([]),
      sources: z.array(z.object({
        title: z.string(),
        url: z.string(),
        source: z.string(),  // "hn" | "reddit:LocalLLaMA" | etc.
        points: z.number().int().default(0),
      })).default([]),
    })),
  }),
});

const archive_papers = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    authors: z.string().optional(),       // free-form string (often a long author list)
    affiliation: z.string().optional(),
    date: z.string().optional(),          // free-form YYYY-MM
    venue: z.string().optional(),
    topic: z.string(),                    // 'agent-rl' | 'user-simulation' | 'gen-rec' | ...
    topic_name: z.string(),               // 'Agent RL' / 'User Simulation' / '生成式推荐'
    topic_icon: z.string().optional(),
    idea: z.string().optional(),          // one-paragraph hook
    paperUrl: z.string().url().optional(),
    codeUrl: z.string().url().nullable().optional(),
    tags: z.array(z.string()).default([]),
    unverified: z.boolean().default(false),
    detail: z.object({
      contribution: z.string().optional(),
      background: z.string().optional(),
      method: z.string().optional(),
      experiments: z.string().optional(),
      pros: z.string().optional(),
      cons: z.string().optional(),
      inspiration: z.string().optional(),
      takeaway: z.string().optional(),
    }).optional(),
  }),
});

const repos = defineCollection({
  type: 'content',
  schema: z.object({
    date: z.coerce.date(),
    collected: z.coerce.date(),
    repo_count: z.number().int(),
    repos: z.array(z.object({
      name: z.string(),            // owner/name
      url: z.string().url(),
      stars: z.number().int().default(0),
      language: z.string().optional(),
      topics: z.array(z.string()).default([]),
      one_liner: z.string(),       // 一句话这个项目是干嘛的
      capability: z.string(),      // 项目实现的能力（markdown，可多句）
      value: z.string(),           // 对从业者的借鉴价值（markdown，'- ' 列表）
      tags: z.array(z.string()).default([]),
    })),
  }),
});

export const collections = { papers, news, archive_papers, repos };
