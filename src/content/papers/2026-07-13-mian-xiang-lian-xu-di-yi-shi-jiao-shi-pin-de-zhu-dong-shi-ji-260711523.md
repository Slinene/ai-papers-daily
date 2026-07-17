---
title: 'Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos'
title_zh: 面向连续第一视角视频的主动式助手基准与记忆增强智能体
authors:
- Gong Sitong
- Tianyu Yan
- Caixin Kang
- Bo Zheng
- Xiang Ruan
- Huchuan Lu
- Kaipeng Zhang
- Yoichi Sato
- Yifei Huang
affiliations:
- 大连理工大学
- Alaya Lab
- 东京大学
arxiv_id: '2607.11523'
url: https://arxiv.org/abs/2607.11523
pdf_url: https://arxiv.org/pdf/2607.11523
published: '2026-07-13'
collected: '2026-07-17'
category: Agent
direction: 主动式智能体 · 长时记忆检索
tags:
- Proactive Agent
- Memory-Augmented
- Egocentric Video
- Retrieval-Augmented Generation
- Streaming Inference
- Temporal Reasoning
one_liner: 构建首个大规模主动式辅助基准 EgoServe，提出免训练记忆增强智能体 EgoMemo，实现基于多尺度记忆的自主干预决策
practical_value: '- **多尺度记忆层次可直接迁移到用户行为建模**：将用户 long-term behavior 序列按粒度组织为「短期行为（clip）→
  活动总结（activity）→ 长周期例行（session）」的层次化摘要，在推荐或 push 触发时按需检索不同粒度的上下文，缓解长记忆灾与窗口限制。

  - **知识图谱 + 多模态嵌入的并行检索设计值得借鉴**：EgoMemo 同时维护语义知识图谱（实体关系）和视觉嵌入库（难以文本化的视觉细节），多路并行检索后做
  caption 重建，这一范式可改造用于商品知识图谱 + 用户行为序列检索，提升推荐解释的上下文还原度。

  - **将主动干预决策建模为检索增强推理输出**：主动推送时机不再依赖硬规则事件检测，而是让 Agent 基于当前上下文 + 检索到的长程记忆自主生成干预决策与内容，可直接应用于电商消息推送、智能客服主动发起对话等场景。

  - **Caption 重建步骤桥接检索片段与完整上下文**：检索到的片段往往是零散的索引或 caption，用 VLM 根据检索目标和原片段重构连贯描述，这能解决
  RAG 类系统中“碎片化证据无法直接用于推理”的痛点，可复用到生成式推荐的结果解释或对话上下文中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有自我中心（egocentric）助手要么被动等待用户明确提问，要么仅根据预设任务触发响应，缺乏基于长程历史上下文自主判断“何时该出手”的能力。主动式辅助需要智能体在连续视频流中，不仅感知当下，还要结合用户的历史习惯、当前活动与目标，自行决定是否干预以及如何干预。这一范式弥补了从被动问答向主动服务的缺口，但缺乏对应的基准和模型。

## 方法关键点
- **EgoServe 基准**：首个面向连续自我中心视频的主动辅助评测集，包含 3000+ 服务实例，覆盖即时、短期、情节、长期 4 个记忆尺度，细分为安全提醒、错误纠正、习惯教练等 10 类服务。注释采用半自动流水线，结合基础模型生成与人工验证。
- **EgoMemo 智能体**：免训练、记忆增强架构，由两个流式阶段组成：
  1. **流式记忆构建**：将视频流逐段转化为（a）三层时序摘要（clip/activity/session 级）；（b）演化知识图谱（实体关系抽取与合并）；（c）视觉嵌入库（关键帧多模态编码），支持三类记忆的在线增长与索引。
  2. **流式检索增强推理**：每一步生成检索查询，并行从时序摘要、知识图谱、视觉嵌入三路检索相关证据，并通过 VLM 将检索到的片段（caption 索引、邻居实体等）重建成连贯上下文（caption reconstruction），最终由推理 LLM 输出干预决策与响应文本。

## 关键结果
- 在 EgoServe 上，EgoMemo 取得 8.0 总 F1，约为 GPT-5-mini（4.7）的 1.7 倍；尤其在长期服务上（记忆链接、例行优化），GPT 类模型几乎全 0，EgoMemo 获得非零分数。
- 在在线视频理解基准 OVO-Bench 的实时感知子任务上，EgoMemo 以 75.15 分显著超过 GPT-4o（64.46）等模型。
- 在离线自我中心问答基准 EgoSchema 上达到 74.8，比最强对比模型 EgoThinker 高出 7.2 点。
- 消融表明，多尺度记忆层次、caption 重建、知识图谱检索三者缺一不可，证明了各模块的互补性。

## 最值得记住的一句话
主动式辅助的本质是将「何时介入」从硬编码规则提升为基于上下文记忆的检索增强推理决策，多尺度记忆与重建式证据整合是让这一决策可工作的关键设计。
