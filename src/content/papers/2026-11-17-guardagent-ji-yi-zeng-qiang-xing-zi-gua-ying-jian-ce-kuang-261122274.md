---
title: 'GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of
  Adversarial Promotions in LLM-Based Recommendation'
title_zh: GuardAgent：记忆增强型自适应检测框架用于 LLM 推荐中的对抗性促销攻击
authors:
- Shiyi Yang
- Xinshu Li
- Chen Wang
- Xiwei Xu
- Liming Zhu
- Lina Yao
affiliations:
- University of New South Wales
- CSIRO
- Monash University
- Macquarie University
arxiv_id: '2611.22274'
url: https://arxiv.org/abs/2611.22274
pdf_url: https://arxiv.org/pdf/2611.22274
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 记忆增强的推荐系统攻击检测
tags:
- LLM-based RecSys
- Adversarial Detection
- Agentic Framework
- Memory-Augmented
- Trustworthy RS
one_liner: 用记忆增强的 Agentic 循环持续学习并检测 LLM 推荐中的商品文本对抗性促销，兼顾可解释性与泛化性
practical_value: '- 电商商品标题/描述是商家可控文本，容易被用于操纵搜索推荐排名；可将 GuardAgent 的 Perception-Action-Reflection-Memory
  循环改造为电商治理中台，用 LLM 对商品文本做持续巡检，把商家恶意营销话术、异常标点、指令注入等作为检测对象。

  - 具体采用其 batch-wise 反思：不是每次错误都更新规则，而是攒够一批误判案例（论文中 batch size=3 即可），做 pairwise contrast
  和跨案例聚合，再让 LLM 修订检测 policy，能显著减少过拟合和假阳性；可替代硬编码正则规则或一次性分类器。

  - 双记忆设计值得借鉴：短期记忆存最新案例和策略，长期记忆存历史经验并用轻量 sentence transformer 做检索增强（top-k 相似样本），在推理时把相似案例和当前
  policy 一起喂给 LLM，提升对新攻击的泛化。工程上可将此封装成规则库+案例库，支持审计追踪。

  - 若上生产，注意成本控制：论文用 GPT-5 做反思/推理，GPT-3.5-turbo 做行动；可替换为本地开源 LLM（如 Qwen3-8B）並看到性能仅中等下降，说明架构收益大于单模型能力；建议先小流量试点，保留
  human review 处理高影响商品。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：传统 RS 中文本只是辅助信号，LLM-based RS 中文本成为推荐决策的主要媒介，攻击面从训练投毒转向推理时商品文本元数据篡改。商家通过拼接促销词、异常标点、改写标题或注入指令即可提升目标商品曝光，而现有 perplexity 检测器静态、不可解释、无法适应新攻击，且容易产生过高假阳性或漏检。因此需要自适应、可解释的检测方案。

**方法关键点**：
- GuardAgent 将检测建模为认知循环：Perception 构造状态（输入 + 记忆），Action 用 LLM 对 benign-malicious 商品文本对进行 CoT 推理并选出恶意候选；错误时触发 Reflection，采用 batch-wise 反思和 two-level contrastive analysis 修订可读的文本检测 policy。
- Memory 分短期记忆（STM）和长期记忆（LTM），分别负责快速适应与长期稳定；推理时用轻量 sentence transformer 检索相似历史样本，结合当前 policy 做 retrieval-augmented detection，输出带规则依据的解释。
- 训练阶段从失败案例中持续学习，通过对比良性/恶意文本的差异来细化规则，避免一次性静态分类器过拟合特定攻击模板。

**关键结果**：在 Amazon Products 和 Yelp Business 数据集上，针对 6 种文本攻击（字符级 DeepWordBug/PuncAttack、词级 TextFooler/BertAttack、句级 TrivialInsertion/ChatGPTAttack）以及 unseen 的 DrunkAgent 进化攻击进行评估。GuardAgent 在 Amazon 上取得 ACC 0.93 / F1 0.92，Yelp 上 ACC 0.84 / F1 0.81，优于 Zero-shot LLM、ICL、Retrieval ICL、Policy LLM、Fine-tuned RoBERTa 和 Perplexity Detector；对 DrunkAgent 检测率达 100%，FPR 极低。Ablation 显示 STM、LTM 和 batch-wise reflection 均对性能有实质贡献，batch size 3 和检索 3 个样本即可达到效果与效率的平衡。

**最值得记住的一句话**：把静态安全检测换成可自我进化的 Agent 记忆循环，用反思失败案例来持续修订文本检测规则，是应对 LLM 推荐中对抗性商品文本操纵的核心思路。
