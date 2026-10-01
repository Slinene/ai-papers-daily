---
title: 'AdaM-Rec: Adaptive Modality Routing for Multimodal Recommendation'
title_zh: AdaM-Rec：面向多模态推荐的自适应模态路由框架
authors:
- Honghao Fu
- Jiacheng Chen
- Manxi Lin
- Junjun Zheng
- Xiangheng Kong
- Yiwei Wang
- Xin Yu
- Miao Xu
- Yuning Jiang
- Yujun Cai
affiliations:
- University of Queensland
- Alibaba Group
- Southeast University
- Adelaide University
arxiv_id: '2609.38455'
url: https://arxiv.org/abs/2609.38455
pdf_url: https://arxiv.org/pdf/2609.38455
published: '2026-09-29'
collected: '2026-10-01'
category: RecSys
direction: 多模态推荐 · 自适应模态路由
tags:
- Multimodal Recommendation
- Modality Routing
- LLM Agent
- Pseudo-query
- Recall Optimization
- E-commerce
one_liner: AdaM-Rec 用 LLM 智能体通过历史正样本伪查询做代理召回评估，动态路由文本与多模态召回预算
practical_value: '- 对多路召回系统，可以用“历史正样本伪查询”做在线代理评估：为每个 query 生成与当前粒度一致、指向用户已购/点击商品的伪
  query，在小候选池上比较文本向量和多模态向量的命中 rank，据此动态分配召回 quota，代替固定融合权重。

  - 将 LLM 作为策略控制器输出路由参数（分支权重和总预算），并结合相似用户的历史参数做 warm start；实验显示小预算时聚焦单一优势模态优于均分，可指导长尾流量召回策略。

  - 排序前按召回来源做特征裁剪：对文本召回候选过滤视觉属性，减少不相关视觉信号对相关性打分的干扰，尤其适合功能/规格型 query。

  - 工程上注意开销：agentic 路由增加推理成本，但可通过轻量文本编码器（如 0.6B）和控制迭代步数来平衡，多模态编码器容量对效果更敏感。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

多模态推荐常假设视觉信息总是有益，但真实电商 query 的模态依赖高度可变：外观驱动 query 需要视觉细节，功能/规格驱动 query 视觉易引入噪声。静态融合无法适配这种 query 级变化，导致召回或排序质量下降。AdaM-Rec 将模态融合转化为 agentic 路由问题，动态校准文本与多模态召回预算。

方法：离线阶段用 MLLM 从商品图文提取结构化画像，并用文本/多模态编码器生成检索向量；LLM 从用户历史交互中归纳 strong_pref/nice_to_have/dislike 偏好，基于偏好相似度检索协作用户。在线阶段，对当前 query 先依据相似用户的历史路由参数初始化 (α,β,K)；生成与 query 粒度一致、指向用户历史正样本的伪查询；在伪查询上分别执行文本和多模态召回，观察目标 item 的 rank；LLM policy 结合 memory 中历史观察迭代更新路由参数，最终得到该 query 的文本/多模态召回权重与总预算。推荐时按权重召回，注入协作用户的正样本候选，对文本召回候选过滤视觉属性后，再由 LLM 打 1-5 相关分并加权排序。

在 Amazon Beauty/Clothing/Music 的 query 推荐上，相对 TAIRA、MACF 等 SOTA，HR@20 平均提升 14.1%，NDCG 平均提升 15.9%；Beauty 上 HR@20 达 0.1711。在 Video Games/Baby 的偏好推荐上，也超过 MLLMRec-R1 等强基线。消融表明去掉自适应路由、伪查询自优化或 memory 均显著掉点；文本召回是主要语义锚点，多模态提供补充线索。
