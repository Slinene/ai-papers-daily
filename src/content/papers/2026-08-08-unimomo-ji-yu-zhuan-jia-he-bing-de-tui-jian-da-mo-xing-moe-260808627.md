---
title: 'UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models'
title_zh: UniMoMo：基于专家合并的推荐大模型 MoE 加速
authors:
- Lei Xin
- Bin Gu
- Peize Li
- Zitong Wang
- Jianbo Zhao
- Changjiang Jiang
- Yanyue Xie
- Chao Huang
- Xuyang Zhao
- Zunhai Su
affiliations:
- Kuaishou Technology
- Hohai University
- Wuhan University
- ByteDance
- Alibaba (Ant Group)
arxiv_id: '2608.08627'
url: https://arxiv.org/abs/2608.08627
pdf_url: https://arxiv.org/pdf/2608.08627
published: '2026-08-08'
collected: '2026-08-13'
category: RecSys
direction: MoE 压缩加速推荐模型
tags:
- MoE
- model compression
- expert merging
- recommender systems
- acceleration
- adaptive routing
one_liner: 用无标签校准集度量专家功能相似性，结合路由曝光保护高频专家，将训练后推荐 MoE 压缩为小 MoE 并保持 NDCG
practical_value: '- 若业务推荐模型已采用 MoE，可借鉴 UniMoMo 做不同 serving budget 的模型档位：用同一训练后 checkpoint
  压缩出 2/4/8 等专家版本，线上按延迟或吞吐切换，避免为每个档位重新训练。

  - 压缩时不要只看参数距离，可复用无标签校准集（用户交互序列/候选商品）比较专家在相同输入上的输出相似度，做功能聚类合并；这比 L2 权重距离更贴近推荐行为，能降低合并带来的排序损失。

  - 引入 layer-adaptive protection：按 routing exposure（专家被路由的概率/流量占比）识别高频专家，限制其参与合并。电商推荐中头部流量专家通常承担关键用户群，保护它们能有效控制
  NDCG 回退，尤其适合流量分布高度倾斜的场景。

  - 该方法不增加线上压缩专用模块，最终导出标准 MoE，可直接替换现有推理服务；在 A100 上可取得 1.28×–2.21× 加速，适合广告/推荐精排阶段降低推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：稀疏 MoE 能提升推荐模型容量，但训练后的 checkpoint 仍存储并路由全部专家，线上推理成本高。现有压缩方法常需额外在线模块，或仅按参数距离合并，忽略功能相似性，难以在推荐场景保持排序质量。

方法关键点：UniMoMo 将 MoE 压缩建模为受限图粗化问题。核心是两处：其一，不再使用参数距离，而是基于功能相似性分组专家——用一个无标签校准集，比较不同专家在共享推荐状态（用户交互历史、候选商品）上的输出响应，相似度高的专家才合并；其二，引入 layer-adaptive protection，根据 routing exposure（专家被路由的流量曝光）保护高流量专家，限制它们参与合并，防止头部用户群性能下降。最终导出的是标准小 MoE，不需要线上压缩模块。

关键结果：在 Amazon Beauty、KuaiRec 和 TenRec 三个数据集上，包含 2、4、6 个 MoE block 的模型压缩到 4 个专家后，NDCG@10 相对源模型五轮均值为 99.92%–102.30%，A100 实测加速 1.28×–1.63×；更激进的 2 专家 top-1 工作点 NDCG@10 比率 98.36%–104.24%，加速 1.47×–2.21×。实验覆盖完整转换与适配流程，表明训练后的推荐 MoE 可按多个 serving budget 导出。
