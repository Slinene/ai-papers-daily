---
title: Cross-Model Memory Transfer via Target-Side Reader Adaptation
title_zh: 跨模型记忆迁移：目标侧 reader 适配的关键作用
authors:
- Mingyuan Li
- Guangsheng Yu
- Xu Wang
- Shaoxiong Ji
affiliations:
- ELLIS Institute Finland
- University of Turku
- University of Technology Sydney
arxiv_id: '2608.17050'
url: https://arxiv.org/abs/2608.17050
pdf_url: https://arxiv.org/pdf/2608.17050
published: '2026-08-16'
collected: '2026-08-21'
category: LLM
direction: LLM 外部记忆跨模型迁移与 reader 适配
tags:
- Engram
- cross-model transfer
- external memory
- reader adaptation
- knowledge reuse
- LLM
one_liner: 提出跨模型冻结 Engram 记忆迁移范式，发现目标侧 reader 适配比记忆表本身更能激活外部知识复用
practical_value: '- 将商品属性、活动规则、用户事实等高频知识沉淀进外部哈希记忆表，与 backbone 解耦，便于在搜索/推荐/广告多条业务线间共享，仅需接入目标侧的轻量
  reader。

  - 模型升级或切换主干时，可冻结已训练的记忆表，只训练很小的 reader adapter，避免重训大模型，同时保留已有知识，降低迭代成本。

  - 若目标模型接口与源 reader 兼容，可直接复用记忆 artifact 零训练上线，适合快速验证；不兼容时先用 dual-layer four-branch
  reader 适配，可接近同源效果。

  - 注意这类外部记忆更适配可寻址的事实/规则，不适合隐式偏好或实时行为，工程上需设计好 key 编码和地址映射。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 知识利用的两条主流路径各有代价。非参数检索带来延迟和上下文开销，参数适应则把知识耦合进权重，难以更新、审计和迁移。Engram 哈希记忆处于中间态：知识存外部可寻址表，通过轻量 reader 消费。跨 backbone 迁移时，冻结记忆表与目标侧 reader 哪个更重要？

方法关键点：在源模型上训练 Engram 记忆和 reader，然后冻结记忆表，将其附加到另一个目标模型，只训练轻量 reader（跨模型冻结记忆提取）。消融分析记忆内容、寻址方式和 reader 对齐。关键设计是 dual-layer four-branch reader，用于目标侧适配。

关键结果：下游 QA 任务中，dual-layer four-branch reader 平均分 38.8，几乎弥合同模型与跨模型复用的差距；当 provider reader 与目标接口直接兼容时，冻结 artifact 无需目标训练即可提供显著效用，可选 reader adaptation 进一步提升。结论：Engram 可作为可复用外部知识 artifact，前提是目标具备兼容 reader 接口；若直接复用不足，target-side adaptation 可对齐。
