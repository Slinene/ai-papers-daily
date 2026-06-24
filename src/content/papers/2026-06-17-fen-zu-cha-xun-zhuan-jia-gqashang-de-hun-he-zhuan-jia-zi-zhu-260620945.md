---
title: 'Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention'
title_zh: 分组查询专家：GQA上的混合专家自注意力
authors:
- Vishesh Tripathi
- Abhay Kumar
affiliations:
- FrontiersMind
arxiv_id: '2606.20945'
url: https://arxiv.org/abs/2606.20945
pdf_url: https://arxiv.org/pdf/2606.20945
published: '2026-06-17'
collected: '2026-06-24'
category: Training
direction: 稀疏注意力·动态查询头路由
tags:
- MoE
- GQA
- sparse-attention
- kv-cache
- conditional-computation
- transformer
one_liner: 在GQA中为每个token动态路由仅部分查询头，匹配密集基线且长上下文prefill加速1.7-1.8倍。
practical_value: '- 在推荐模型的Transformer序列编码中，若已使用GQA减少KV缓存，可直接引入GQE：保持KV头全激活，仅对查询头做token级稀疏路由，降低长序列用户行为建模的注意力计算量。

  - 路由选择可根据token难度（如特征重要性分数）设计轻量线性路由器，在训练时加入负载均衡损失防止头利用率崩塌，这一点与普通MoE一致，可直接复用现有MoE工程组件。

  - 长上下文推理加速明显，适合搜索推荐系统中需要处理用户长期行为序列（如数月点击历史）的场景，prefill阶段获得约1.8倍加速，同时保持下游任务精度无损。

  - 在资源受限的Agent多轮对话或生成式推荐中，KV缓存占用常为瓶颈，GQE保留了GQA的KV共享优势，又额外节省查询头计算，可以作为移动端或边缘推理的候选方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：标准密集自注意力对所有token统一激活所有注意力头，浪费计算，尤其在长序列下。混合专家（MoE）思想多用于MLP层，鲜少引入注意力块。与此同时，GQA通过共享KV头降低缓存和带宽，但查询头仍全量激活。如何将条件计算引入查询头，既保持GQA的KV缓存效率，又减少冗余的查询计算？

**方法**：提出Grouped Query Experts (GQE)，在GQA的每组查询头之上叠加MoE路由。每个GQA组内，路由器为每个token从该组的查询头专家中选出top-k，其余查询头不参与计算；KV头保持稠密不变。最终输出由激活的查询头拼接后经线性投影得到。GQE仅增加路由计算开销、专家权重增多但激活参数不变，训练时加入负载均衡损失。

**结果**：在250M参数规模、固定30B token预算下，GQE激活一半查询头时，在下游任务准确率上与全激活GQA基准持平，同时在长上下文推理中获得1.7–1.8倍prefill加速。验证了在保持精度下大幅降低注意力计算成本的可行性。
