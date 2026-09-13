---
title: 'Recognizing Is Not Reversing: A Controlled Inversion Test of Fact-Preserving
  News Framing'
title_zh: 识别并非逆转：事实保持新闻框架的受控逆转测试
authors:
- Yi Liu
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.11769'
url: https://arxiv.org/abs/2609.11769
pdf_url: https://arxiv.org/pdf/2609.11769
published: '2026-09-10'
collected: '2026-09-13'
category: Eval
direction: LLM评估 · 框架逆转与事实保持
tags:
- LLM evaluation
- news framing
- fact preservation
- framing inversion
- controlled test
- robustness
one_liner: 通过540个受控新闻变体证明LLM即使识别出framing也几乎无法在保持事实下撤销干预
practical_value: '- 在电商文案、广告合规或评论中立化等LLM改写任务中，不要因为模型能识别出倾向/框架就假设它能可靠逆转；事实一致性需要独立约束与评估，可借鉴论文的原子事实配对与编辑记录方式构建评测集。

  - 对高风险文本（如商品描述、客服话术）建立“识别-逆转-事实保持”三分离评估，避免只测中立性分数或检测准确率；重点验证改写后关键事实是否仍然保留。

  - 若业务需要自动“去bias”或“去情绪”改写，建议采用受控变换生成配对样本而非仅依赖众包，能更干净地量化模型是否真正进行了逆转而非表面换词。

  - 本论文领域为新闻framing，业务直接可迁移点有限，但评估设计可借用于生成式推荐文案、消息推送词等场景的事实一致性验证。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM新闻framing研究集中在生成、检测或中立化，未验证模型能否在保持事实不变的前提下撤销已知framing变换，导致“识别framing”与“逆转framing”的能力被混为一谈。

### 方法关键点
提出受控逆转测试：在60篇新闻文章上，对三种framing文本实现（评价词汇、代理实现、信息显著性）施加三种干预强度，得到540个配对变体，保证原子事实一致并记录编辑。在Qwen、DeepSeek、Kimi上测试。

### 关键结果
事实保持约0.84，而干预逆转仅0.044–0.068；即使模型正确识别framing类型与方向，逆转也只有0.071。结果显示事实保真、framing识别与framing逆转三者显著分离，识别不等于能逆转。
