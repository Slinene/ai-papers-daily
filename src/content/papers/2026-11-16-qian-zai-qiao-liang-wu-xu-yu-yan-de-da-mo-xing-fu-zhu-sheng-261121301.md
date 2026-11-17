---
title: 'Latent Bridge: Asking for Help Without Words'
title_zh: 潜在桥梁：无需语言的大模型辅助生成
authors:
- Qichao Wang
- Tingyu Qu
- Pengcheng Wu
- Yiran Zhong
- Feida Zhu
- Zhiqi Shen
- Peilin Zhao
- Steven Hoi
affiliations:
- Nanyang Technological University
- Alibaba Group
- Shanghai Jiao Tong University
arxiv_id: '2611.21301'
url: https://arxiv.org/abs/2611.21301
pdf_url: https://arxiv.org/pdf/2611.21301
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: 模型协作 · 大模型 prefill 表示迁移
tags:
- POND
- prefill-only
- model collaboration
- representation transfer
- efficient inference
- bridge
one_liner: POND 让大模型仅做 prefill 不参与解码，通过可训练桥接把隐藏状态注入小模型 attention，实现低延迟模型协作
practical_value: '- 在推荐/广告解释生成、对话式推荐等场景，如果要让大模型辅助小模型做在线生成，可以只让大模型对 input/context 做一次
  prefill，把其隐藏状态通过可训练 adapter 映射成小模型 attention 的额外 K/V，避免大模型逐 token 解码，显著降低线上 RT 和成本。

  - 桥接层可以做得非常轻量，冻结 sender 与 receiver 主体，只训练 bridge；工程上相当于给小模型加了一组外部条件化表示，适合在已有小模型上快速叠加能力。

  - 定期 review 机制可借鉴到流式生成场景：小模型先生成一部分内容，再让大模型 prefill 处理部分输出并更新指导，同时保留小模型已有 KV cache，避免重新计算，实现长序列生成中的动态校正。

  - 跨模型家族有效这一结论意味着不用强绑同构模型，可以在业务中选一个性能最好的大模型作为 sender，配合任意部署友好的小模型 receiver，训练数据只需聚焦核心高价值领域即可迁移到其他任务。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：文本式模型协作要求大模型先逐 token 生成中间回复，给推理引入大模型解码延迟，尤其当大模型辅助边缘部署的小模型时成本很高。

**方法关键点**：POND 采用 Prefill-Only, No-Decode 方案：冻结的大模型 sender 只对输入做 prefill，所有自回归解码由小模型 receiver 完成；一个可训练 bridge 把 sender 的隐藏状态映射为额外的 attention keys/values，供 receiver 在整个生成过程中使用。还支持 periodic review：sender 定期处理 receiver 已生成的部分内容，通过额外 prefill 更新指导，同时保留 receiver 已有 KV cache。

**关键结果**：在推理和编程基准上，POND 稳定提升 receiver 性能，sender 可来自不同模型家族；GLM-5.3 与 Qwen3.8-Max 对 Qwen receiver 带来的增益相当，说明独立训练模型家族间的表示迁移有效。在数学和编程任务上训练后，可直接迁移到通用知识任务，无需领域特定训练。
