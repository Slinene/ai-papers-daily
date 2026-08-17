---
title: 'MobileMem: Learning from a Year of Mobile Experiences'
title_zh: MobileMem：移动端长期记忆基准与知识引导数据合成框架
authors:
- Xinle Deng
- Yida Xue
- Xiangyuan Ru
- Haoming Xu
- Shuofei Qiao
- Mengru Wang
- Yijun Chen
- Buqiang Xu
- Chen Jiang
- Yuchen Eleanor Jiang
affiliations:
- OPPO
- OpenKG
arxiv_id: '2608.13606'
url: https://arxiv.org/abs/2608.13606
pdf_url: https://arxiv.org/pdf/2608.13606
published: '2026-08-11'
collected: '2026-08-17'
category: Agent
direction: 面向移动设备 Agent 的长期记忆基准与数据合成
tags:
- long-term memory
- on-device agent
- benchmark
- knowledge graph
- data synthesis
- personalization
one_liner: 提出移动端长期记忆基准 MobileMem 与合成框架 KEME，系统评估端侧记忆系统在多跳、时序、偏好推理上的能力。
practical_value: '- **复合记忆架构可迁移到电商用户画像**：论文提出的“系统级记忆层（blackboard）+ 应用级记忆（cognitive
  offloading）”两层架构，很适合电商/推荐场景。应用侧（如订单、搜索、浏览、客服对话）先做初筛，只上报有长期价值的用户事件，系统侧构建跨域用户知识图谱，既节省算力又保护隐私。

  - **用 KEME 合成长期用户轨迹**：缺少跨 session 真实交互数据是推荐/Agent 评测痛点。KEME 的 persona + knowledge
  anchors + temporal event graph 能生成时间一致、偏好演化的长周期用户行为序列，可用于模拟用户兴趣漂移、跨 app 关联行为，训练或评测个性化模型。

  - **记忆系统选型结论直接可用**：实验显示 HippoRAG2 与 A-MEM 显著优于 NaiveRAG 和 Long Context，核心在于保留原始交互细节
  + 增强检索（实体关系图 PageRank / 丰富元数据）。在构建用户长期记忆库时，不要过度压缩摘要，应保留细粒度证据并用关键词、标签、图结构辅助召回。

  - **按错误类型定位瓶颈**：用 MemTrace 等归因工具区分提取错误、检索错误、生成错误，可指导优化方向。实际系统中多数失败可能来自上游提取或下游生成，而非只优化检索器。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机
移动端 AI Agent 正从单轮问答走向持久个人助理，需要长期记忆来积累和利用用户经验。但现有记忆基准假设云存储、无限算力，不适用于移动设备上海量、多模态、跨应用、强时序、隐私敏感的真实数据。端侧记忆面临记忆爆炸、跨应用碎片化、偏好持续演化、存储/算力受限、隐私合规等独特挑战。

## 方法关键点
- **基准形式化**：每个实例为 `(T, Q)`，T 是跨 session 的异构动作流（用户/助手/第三方 App 交互），Q 为多类 QA 对，端到端评估记忆系统。
- **两层记忆生态**：提出系统级记忆层（blackboard architecture）+ 应用级记忆（cognitive offloading），通过标准化协议交换结构化事件，应用侧过滤低价值交互，系统侧维护跨应用用户图谱和行为抽象。
- **KEME 合成框架**：基于用户先验知识（persona、知识锚点）构建时间事件图，四个 agent 协同：知识引导规划器自顶向下分层、知识锚点接地确保一致性、经验实现器生成 session 并驱动 persona 版本演化、经验驱动修订器自底向上修正未来事件。
- **两个数据集**：MobileMem（文本版，7 类应用模板）与 MobileMem-Omni（多模态版，加入截图、关系图、人脸合成，支持双语和视觉推理）。

## 关键结果
在 GPT-4.1-mini / GPT-5.4-mini 上评测 9 种记忆系统，A-MEM 与 HippoRAG2 总体最优（约 78–80%），远超 NaiveRAG（~37%）和 Long Context（~54%）。两者共同点是保留原始对话细节并用元数据/知识图谱增强检索，而非激进压缩。多跳、时序、查询聚焦摘要仍普遍困难；对抗问题中强系统易被弱相关记忆干扰。HippoRAG2 以较低 token 成本（~2.8k）获得高强度结果，A-MEM 成本高（5.5–11k tokens）。错误归因显示不同系统瓶颈差异大：Long Context 主要为更新错误，NaiveRAG 为检索错误，Mem0 为提取错误，EverMemOS 为生成错误，但所有系统均存在下游生成错误。

## 最值得记住的一句话
端侧长期记忆需要复合架构 + 保留原始证据的知识增强检索，移动记忆的本质不是压缩信息，而是组织并检索碎片化经验。
