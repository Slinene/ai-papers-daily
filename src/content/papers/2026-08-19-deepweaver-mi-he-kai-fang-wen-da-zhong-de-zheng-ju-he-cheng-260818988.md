---
title: 'DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering'
title_zh: DeepWeaver：弥合开放问答中的证据合成鸿沟
authors:
- Xujia Wang
- Yizhe Zhang
- Bin Xu
- Lei Hou
- Juanzi Li
affiliations:
- Tsinghua University
arxiv_id: '2608.18988'
url: https://arxiv.org/abs/2608.18988
pdf_url: https://arxiv.org/pdf/2608.18988
published: '2026-08-19'
collected: '2026-08-20'
category: RAG
direction: RAG 证据合成 · Thought Block Chain
tags:
- Evidence Synthesis
- Thought Block Chain
- RAG
- Long-Context QA
- Citation Grounding
- Deep Research
one_liner: 用 Thought Block Chain 将噪声证据编织成细粒度、带引用的声明，显著提升开放 QA 的证据利用率与引用质量
practical_value: '- **借鉴 TBC 作为生成前中间表示**：在电商/推荐场景中，当需要基于大量候选商品、用户评论、内容文档生成推荐理由或商品综述时，可以先用
  LLM 抽取结构化的「claim + keywords + salient info + evidence」块，把长上下文压缩为可管理的块链，再逐块生成最终文案，避免直接给
  LLM 全量候选导致的信息丢失。

  - **迭代式证据补全机制**：DeepWeaver 的 subordinate + commit 流程（识别未覆盖证据 → 生成子 TBC → merge/discard）可以直接迁移到商品推荐理由生成或搜索
  answer 合成中：先让模型生成初稿，再找出被忽略的用户痛点或商品卖点，补充后合并去重，能大幅提升内容覆盖率和细节保留度。

  - **随机采样证据分轮处理**：在广告文案、推荐理由等需要引用大量候选的场景，不必一次把所有商品/文档塞进 context，可按轮随机采样子集构造 TBC，多轮后覆盖全量证据，既能降低单次
  context 压力，又能保持最终输出的全面性。

  - **可解释性与引用对齐**：通过把每个 claim 显式链接到证据片段（商品属性、评论、文档段落），可以方便地做归因和后续验证，适合需要高可信度的搜索推荐答案生成，也方便在线上做引用溯源和质量审核。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机

检索增强生成（RAG）在开放问答中普遍面临「证据合成鸿沟」：检索到的证据往往噪声大、碎片化、知识密集，但直接让 LLM 一次性从长上下文中生成答案，会导致证据利用不足、引用错位、细节坍缩为浅层摘要。现有工作多优化检索质量或上下文压缩，却忽视了检索与生成之间的显式合成阶段。此外，长上下文模型即使窗口很大，也常因 lost in the middle 等现象而遗漏关键信息。因此需要一种中间模块，把噪声证据组织成细粒度、可追溯的结构，再驱动生成。

## 方法关键点

- **Thought Block Chain (TBC)**：核心数据结构，将答案分解为多个 thought block，每个 block 包含 claim、keywords、salient info 和 linked evidence 片段，既保留细粒度信息，又显式建立 claim-证据映射。
- **三阶段证据编织**：
  1. **Draft**：基于全量证据池直接生成答案草稿，然后抽取初始主 TBC T^0_M。
  2. **Subordinate**：定义残差证据集 R（未被 T^0_M 覆盖的片段），从 R 中生成子 TBC T^0_S，专门挖掘被忽略的方面、细节或替代证据。
  3. **Commit**：对 T^0_M 和 T^0_S 执行 merge（合并重叠 claim 和关键词，合成 woven claim）和 discard（删除无关、冗余、弱支持块），得到精炼 TBC T^1_M。
- **迭代精炼**：重复 subordinate + commit 多轮（默认 n=2），每轮随机采样 r 个证据片段以降低 context 压力。
- **证据锚定生成**：最终答案按 TBC 块逐个生成，每个 section 只使用对应的证据子集 E_i 作为局部上下文，最后串联并润色。

## 关键实验与结果

- **LoQA 基准**：构建了 100 个中文水环境领域开放问题，每个问题平均配套约 200 个证据块（约 206K tokens，其中约 100 个相关 + 100 个随机噪声），评估内容充分性、引用 grounding 和细节保留。
- **主结果**：在 Qwen3-30B-A3B-Instruct 上，DeepWeaver 相比直接 E-RAG，Recall 提升 7.6，Argument Sufficiency 提升 15.5%，Relevant Citations 提升 14.7 个，Relevant Ratio 提升 14.5%，Detail Preservation 提升 16.6%。即使 Oracle ER-RAG（只给相关证据）也落后于 DeepWeaver。
- **跨模型泛化**：在 DeepSeek-V3.2、DeepSeek-V4-Flash、Qwen3.5-122B 等多个 backbone 上一致提升，DeepWeaver + Qwen3-30B 甚至超过 DeepSeek-V3.2 直接生成的性能。
- **DeepResearch Bench**：在 Web 深度研究任务上，DeepWeaver 相比 WebWeaver 显著提高 Insight（45.78→47.59）、有效引用（26.74→60.13）和引用准确率（25.00→62.02），但 readability 稍降。

## 一句话记住

**“在检索和生成之间显式加入结构化证据合成（TBC + 迭代编织），比单纯提升检索质量或扩大上下文窗口更能释放 LLM 的长上下文利用能力。”**
