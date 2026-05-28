---
title: Rethinking Memory as Continuously Evolving Connectivity
title_zh: 重新思考记忆：持续演进的连接性
authors:
- Jizhan Fang
- Buqiang Xu
- Zhixian Wang
- Haoliang Cao
- Xinle Deng
- Baohua Dong
- Hangcheng Zhu
- Ruohui Huang
- Gang Yu
- Ying Wei
affiliations:
- Zhejiang University
- Alibaba Group
- MemTensor
- Tongji University
arxiv_id: '2605.28773'
url: https://arxiv.org/abs/2605.28773
pdf_url: https://arxiv.org/pdf/2605.28773
published: '2026-05-26'
collected: '2026-05-28'
category: Agent
direction: 连接演化驱动的Agent记忆框架
tags:
- Agent Memory
- Graph Memory
- Memory Evolution
- Connectivity
- Self-evolving Agents
one_liner: 提出FluxMem，将记忆建模为可演化的异构图，通过三阶段进化实现动态连接优化，在三个基准上达到SOTA
practical_value: '- **记忆连通性演化范式**：将记忆组织为异构图，根据任务反馈动态调整连接（新增缺失链接、剪除干扰边），可解决电商Agent长对话/多轮任务中检索不准、关键信息遗漏的问题。

  - **三阶段演化流程参考**：Stage I 初始连接构建、Stage II 反馈驱动精炼（链接级+单元级编辑）、Stage III 长期巩固（技能蒸馏与成熟度收敛），可直接模块化复用于Agent记忆系统设计。

  - **技能自动提取与成熟度度量**：利用PEMS指标判断过程技能是否收敛，避免冗余迭代；可将电商操作成功轨迹自动转化为可复用技能，提升跨任务泛化能力。

  - **单元级内容自适应**：在检索充足但抽象粒度不匹配时，方法动态细化和粗化记忆单元，可指导电商场景中不同步骤所需上下文粒度的动态调整。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现有记忆增强LLM Agent大多将记忆视为静态仓库，使用固定检索流水线，难以适应动态环境中的任务变化和反馈。这导致两类典型故障：（1）连接不准确——欠连接遗漏关键上下文，过连接引入噪声；（2）记忆单元粒度僵化，无法自适应调整。此外，缺少长期巩固机制使得类似经验无法沉淀为稳定技能。针对这些问题，论文提出一种连接演化记忆框架FluxMem。

**方法关键点**：
- **三层异构图记忆**：语义层（事实知识）、情节层（状态-动作轨迹）、过程层（可复用推理技能），节点通过任务关联动态连接。
- **三阶段演化**：Stage I 初始连接形成（混合评分检索+情节相似度+过程继承）；Stage II 反馈驱动精炼（根据环境或自检失败，执行链接扩展/剪除、记忆单元内容重整形）；Stage III 长期巩固（同类情节聚类、LLM提取技能节点，并通过过程演化成熟度评分PEMS迭代优化直到收敛）。
- **记忆上下文即激活子图**：每步决策时诱导出局部子图作为上下文，精炼即对子图拓扑的编辑。

**关键实验结果**：
- **LoCoMo长对话推理**：GPT-4.1-mini 平均LMJ分95.06，超过全上下文(81.23)和最强基线EverMemOS(93.05)；Qwen3-30B-A3B 达到93.44。
- **Mind2Web网页导航**：无元素过滤真实设置下，Cross-Task成功率从AWM的3.6提升至8.1（GPT‑4.1-mini），Gemini‑2.5-flash 上达到9.6。
- **GAIA通用助手任务**：Kimi K2 平均成功率从52.12升至64.85（+12.73%），Level 3 成功率从34.62升至46.15。
- **消融**：LoCoMo上Stage II是关键（移除后降约10分），Mind2Web上Stage III更重要；迭代次数增加带来单调提升，5轮后接近饱和。

**核心观点**：记忆不应是静态存储，而应成为随环境交互持续演化的连接结构。
