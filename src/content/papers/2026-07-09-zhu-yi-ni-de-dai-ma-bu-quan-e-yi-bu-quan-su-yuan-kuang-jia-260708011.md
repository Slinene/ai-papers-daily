---
title: 'Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions'
title_zh: 注意你的代码补全：恶意补全溯源框架
authors:
- Anjun Gao
- Yueyang Quan
- Zhuqing Liu
- Minghong Fang
affiliations:
- University of Louisville
- University of North Texas
arxiv_id: '2607.08011'
url: https://arxiv.org/abs/2607.08011
pdf_url: https://arxiv.org/pdf/2607.08011
published: '2026-07-09'
collected: '2026-07-10'
category: Other
direction: LLM 后门·溯源
tags:
- backdoor-attack
- code-completion
- forensic
- LLM
- data-poisoning
one_liner: 提出 CodeTracer，仅凭微调语料和误补全事件即可将恶意代码补全追溯到具体的后门训练数据
practical_value: '- **恶意行为溯源思路可迁移到推荐模型**：当线上模型出现异常推荐（如恶意商品置顶），借鉴 CodeTracer 的指纹提取和语义搜索，从微调数据中定位投毒样本，适合大促前数据审计。

  - **无需模型内部参数**：仅用微调语料和误补全日志即可归因，适用于黑盒发布后的推荐系统安全调查，不依赖训练框架。

  - **指纹结构化方法可复用**：将异常推荐内容拆解为（上下文，关键行为，威胁类型）三元组，用 LLM 推理匹配可疑训练样本，可用于构建推荐系统的数据污染检测流水线。

  - **防御视角**：了解攻击者如何通过微调植入后门，反向提醒我们在使用第三方微调数据或用户反馈数据训练推荐模型时，需设计类似触发词过滤和语义一致性校验的防御措施。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：代码补全模型易受后门攻击，恶意微调数据可在特定上下文中触发不安全代码生成。现有防御易被绕过，亟需一种事后溯源方法，找出导致异常补全的具体污染样本。

**方法**：提出 CodeTracer 框架，仅需微调语料库和用户报告的误补全事件。首先从恶意输出中提取结构化行为指纹（上下文、漏洞类型、关键语义），然后在微调数据中通过语义相似度检索出候选样本，最后利用 LLM 进行多步推理，将不安全逻辑归因到确切的后门训练样本。整个过程无需模型参数或训练细节。

**结果**：在 3 类漏洞（SQL 注入、命令注入、路径遍历）和 10 种后门攻击上评估，与 16 个基线对比，CodeTracer 取得高归因准确率（Top-1 准确率超 90%）、低误报率（<5%），且对自适应攻击（如触发词变形、多阶段注入）保持鲁棒。
