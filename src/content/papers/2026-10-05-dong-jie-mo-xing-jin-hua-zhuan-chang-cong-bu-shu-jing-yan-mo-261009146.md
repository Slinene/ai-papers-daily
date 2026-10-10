---
title: 'Frozen Models, Evolving Expertise: Model-Agnostic Learning from Deployment
  Experience for Multimodal Medical AI'
title_zh: 冻结模型，进化专长：从部署经验中做模型无关的多模态医学AI学习
authors:
- Yexiao He
- Yucheng Tang
- Pengfei Guo
- Yufan He
- Andriy Myronenko
- Can Zhao
- Ang Li
- Daguang Xu
- Dong Yang
affiliations:
- University of Maryland, College Park
- NVIDIA
arxiv_id: '2610.09146'
url: https://arxiv.org/abs/2610.09146
pdf_url: https://arxiv.org/pdf/2610.09146
published: '2026-10-05'
collected: '2026-10-10'
category: Agent
direction: 冻结模型外部经验持续学习
tags:
- LLM
- VLM
- Continual Learning
- External Memory
- Multimodal RAG
- Model-Agnostic
one_liner: 提出参数无关外部专长框架，让冻结LLM/VLM从部署经验中持续提升并跨模型迁移
practical_value: '- 在线 Agent/导购/客服：用 LLM optimizer 从成功/失败轨迹重写 Skill 文档而非 append，控制长度、消解冲突规则；候选
  Skill 上线前用「下一批新流量 + 历史代表性 buffer」联合验证，接受条件为新样本平均收益>0、历史平均收益≥0、且 win>=loss，防止 prompt
  过拟合固定验证集。可套用于搜索 query 改写策略、导购话术策略。

  - 商品/内容多模态：维护 MMKB 式视觉记忆库，保存商品图+已知结论（类目、属性、违规、点击/转化标签），检索后用明确 prompt 让模型比较参考图证据与当前图的差异/缺失/矛盾，而不是只把图塞进上下文。实验显示同样
  references，仅当上下文会让视觉任务分数下降，加比较分析后才转正；可迁移到商品图质检、主图优选、属性抽取。

  - 知识与事实记忆：把可靠事实以「证据+适用条件」存入外部 Knowledge Memory，查询时先检索再检查是否直接回答且适用；只有多案例支持或有可信外部来源才入库。可做电商规则库、广告合规知识、平台政策问答的持续更新。

  - 经验外置可无缝迁移到新基座/新模型版本，冷启动成本低；换 LLM 供应商或升级模型时，无需重训，直接复用 Skill/Memory/MMKB，对正在 A/B
  不同底座或多租户模型选型的团队有用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM/VLM 部署后参数冻结，无法复用已验证病例、新证据和错误反馈；医疗场景更新快，重复犯错成本高。微调需权重且成本高；已有参数无关方法依赖固定验证集选 prompt，容易过拟合，且文本记忆丢失视觉细节。

**方法关键点**：
- 外部专长分三类：Skill 记录可复用推理与工具调用步骤，每批用 LLM optimizer 重写而非追加，控制长度并消解冲突；Knowledge Memory 只存有证据、适用条件的事实，来自已验证病例或 PubMed，多案例支持才入库；MMKB 保存原始图像+source answer，用多模态 embedding 做联合检索，并要求模型逐条解释参考证据、与当前图比较差异/缺失/矛盾。
- 上线验证：候选 Skill/Memory 与当前版本在下一批新病例+历史 buffer 上对比，接受条件为新病例平均收益>0、历史平均收益≥0、双方 win≥loss；周期性回滚更早版本。模型参数始终不变。

**关键实验**：在 AgentClinic-MedQA、MedChain、MedThink-Bench、MedThinkVQA、VisuLogic、QCalEval 六个 benchmark 上，4 个底座模型。Ours 在 24 对 benchmark-model 上全部超 Base，医学任务最高 +34.2%，在线平均 +17.6%（ACE 5.6%）；冻结泛化平均 +20.7%（SkillOpt 8.3%、ACE 1.9%）；跨模型零步迁移平均 +20.0%。消融：Skill 对文本/多步任务贡献最大（MedChain -12.1%），MMKB 对视觉任务贡献最大（QCalEval -14.0%）；取消验证所有 benchmark 下降 21.8%–37.8%。相同 references 下，标准检索仅 -3.5% 到 +5.0%，MMKB 的比较式使用最高 +23.9%。

**最值得记住**：冻结模型的持续提升应把经验外化为可验证、可迁移的 Skill/Knowledge/Visual Memory，而不是只靠微调或固定验证集选 prompt。
