---
title: 'GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents'
title_zh: GateMem：多主体共享记忆智能体的记忆治理基准
authors:
- Zhe Ren
- Yibo Yang
- Yimeng Chen
- Zijun Zhao
- Benshuo Fu
- Zhihao Shu
- Bingjie Zhang
- Yangyang Xu
- Dandan Guo
- Shuicheng Yan
affiliations:
- Jilin University
- Shanghai Jiao Tong University
- King Abdullah University of Science and Technology (KAUST)
- Tsinghua University
- National University of Singapore
arxiv_id: '2606.18829'
url: https://arxiv.org/abs/2606.18829
pdf_url: https://arxiv.org/pdf/2606.18829
published: '2026-06-16'
collected: '2026-06-22'
category: Agent
direction: 多智能体共享记忆治理评估
tags:
- Memory Governance
- Multi-Agent
- Benchmark
- Access Control
- Active Forgetting
- LLM Agents
one_liner: 首创多主体共享记忆治理基准，评估效用、访问控制与遗忘，揭示当前智能体在可靠共享记忆上的不足
practical_value: '- 共享记忆治理是电商/客服多角色Agent（如买家、卖家、平台客服）的刚需：不同主体写入和查询的权限隔离、状态更新与遗忘机制，可直接借鉴GateMem的三维评估框架来设计系统测试集。

  - 主动遗忘（active forgetting）能力对电商Agent至关重要：当用户请求删除历史记录或账户注销时，需要确保记忆真正消除，GateMem的遗忘泄露测试方法可复用于验证内部记忆模块的合规性。

  - 长上下文提示虽然治理得分更高，但高token成本不适用于大规模推荐/对话系统；检索式内存机制成本低却易泄露，这提示工程上需要混合方案：对敏感记忆用封装API进行精确擦除，对非敏感长语境采用压缩摘要。

  - 可借鉴的工程实现：增量记忆注入和隐藏检查点（hidden checkpoints）的评测设计，能度量记忆在连续交互中的漂移和泄露，适用于推荐系统中用户画像的忠诚度与隐私验证。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM记忆基准多假设单一用户，忽略了医院、办公、教育等共享场景中多主体（医生、护士、患者）写入同一记忆池并需依角色、关系进行访问控制与遗忘的现实需求，记忆治理（governance）成关键。

**方法**：提出GateMem基准，覆盖医疗、办公、教育、家庭四域，设计长时多参与多人对话剧情，通过增量记忆注入、隐藏检查点、结构化判断和泄露目标标注，联合评估三个维度：1）长期请求的效用（utility）；2）上下文权限边界下的访问控制（access control）；3）显式删除后的主动遗忘。

**结果**：实验表明，无方法能同时获得高效用、强访问控制和可靠遗忘。长上下文提示虽在治理评分上最优，但token开销大；检索式或外部记忆方法虽降低成本，却存在未授权或已删除信息的泄露。当前记忆智能体离可靠的机构级部署仍有明显差距。
