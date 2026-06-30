---
title: When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding
title_zh: 投机解码中草稿接受准则的理论分析
authors:
- Aaryam Sharma
affiliations:
- Independent Researcher
arxiv_id: '2606.30265'
url: https://arxiv.org/abs/2606.30265
pdf_url: https://arxiv.org/pdf/2606.30265
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: LLM 推理加速 · 投机解码理论
tags:
- Speculative Decoding
- Greedy Decoding
- Acceptance Criterion
- KL Divergence
- Tree Decoding
- LLM Inference
one_liner: 为贪婪与放松接受下的投机解码提供基于 KL 散度的接受证书，覆盖树形解码
practical_value: '- 若在推荐系统中部署 LLM 进行实时生成（如对话式推荐、解释生成），可借鉴放松接受准则（加性/乘性/top-m 放松）提升
  draft 接受率，降低延迟。

  - 树形解码允许多候选并行验证，在目标分布较平坦时仍能保持较高接受概率，适合对延迟敏感的场景，可直接工程化。

  - 论文给出的基于 KL 散度和 margin 的接受条件，可用于离线评估 draft 模型质量，指导模型选择与阈值设定，平衡质量与速度。

  - 对于需要确定性输出（不要求分布完全匹配）的推送文案生成、搜索词改写等任务，可直接应用贪婪+放松的投机解码，无需额外校准。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：实际 LLM 推理系统广泛采用贪婪解码、放松接受或树形候选的投机解码，但缺乏理论支撑。现有分析聚焦于保持分布的随机采样设定，而本文针对这些确定性或松弛接受场景建立理论。

**方法**：将常见接受准则的拒绝域统一刻画为目标分布的下水平集，推导出拒绝事件发生所需的精确 KL 散度，并给出严格贪婪、加性/乘性放松、top-m 放松、熵阈值接受等准则下的接受证书与基于 margin 的紧界。进一步扩展至树形贪婪解码，导出目标 greedy token 能被 drafter top-m 覆盖的确切条件与仅靠 margin 的证书。

**结果**：在 Qwen3 模型上实验，放松与树形准则大幅扩大可认证接受区域，尤其在目标分布 margin 较低时效果显著。这些证书与分布式分析互补，刻画了实际系统中确定性的局部接受事件，为投机解码的参数选择提供理论依据。
