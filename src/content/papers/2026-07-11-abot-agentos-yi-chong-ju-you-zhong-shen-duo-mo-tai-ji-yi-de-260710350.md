---
title: 'ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory'
title_zh: 'ABot-AgentOS: 一种具有终身多模态记忆的通用机器人Agent操作系统'
authors:
- Jiayi Tian
- Shiao Liu
- Yuting Xu
- Jia Lu
- Zihao Guan
- Honglin Han
- Di Yang
- Minqi Gu
- Yifei Qian
- Tianlin Zhang
affiliations:
- Alibaba Group
- AMAP CV Lab
arxiv_id: '2607.10350'
url: https://arxiv.org/abs/2607.10350
pdf_url: https://arxiv.org/pdf/2607.10350
published: '2026-07-11'
collected: '2026-07-15'
category: Agent
direction: 通用具身Agent操作系统与多模态记忆
tags:
- AgentOS
- MultiModalMemory
- GraphMemory
- SelfEvolution
- EmbodiedAI
one_liner: 提出通用Agent OS层，通过多模态图记忆与失败驱动自进化，提升长期具身任务执行能力
practical_value: '- **多模态图记忆可复用到用户/商品知识图谱**：将对话、行为、上下文等异构数据统一为类型化节点与边，构建持续增长的通用记忆底座，可用于电商对话Agent的长期偏好追踪与上下文管理。

  - **失败驱动的自进化回路适合在线学习系统**：诊断记忆失败自动生成修复规则，且按评估分割隔离，避免污染训练集；推荐系统可借鉴此机制实现模型的持续纠偏与冷启动改善。

  - **场景条件规划与多阶段验证提升复杂流程可靠性**：在推荐编排或多层排序中，可引入类似“规划-执行-验证”的思维链，对召回、粗排、精排结果进行结构化校验。

  - **边云协作架构适合大规模Agent部署**：将重计算推至云端，端侧仅保留轻量执行器，为电商Agent的实时性与隐私权衡提供工程参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有VLM/VLA系统提升了机器人感知与动作预测，但长期具身任务仍需统一的推理、记忆、工具使用与验证层。

**方法**：提出ABot-AgentOS，作为位于底层控制器之上的通用Agent操作系统。核心创新包括：
- **通用多模态图记忆（Universal Multi-modal Graph Memory）**：将对话、视觉观测、空间上下文、时序关系与任务轨迹转化为类型化节点与边，形成持久可追溯的记忆基底。
- **失败驱动自进化回路**：解析记忆错误，生成限门进化资产，仅作用于后续评估分割，防止当前分割真值泄露，实现持续提升。
- **场景条件规划与上下文隔离技能执行**：结合多阶段验证与边云协作，支撑跨实体执行。
- **EmbodiedWorldBench**：可执行评测集，含16场景、4难度、200+任务，覆盖导航、对话、动态事件等，采用轨迹归因评分。

**关键结果**：静态版本在LoCoMo获87.5，OpenEQA EM-EQA 59.9，Mem-Gallery 88.6，NExT-QA Acc@All 76.5；自进化后将LoCoMo提升至88.7，OpenEQA 60.4，Mem-Gallery 89.0，验证了Agent OS层对长期执行的增益。
