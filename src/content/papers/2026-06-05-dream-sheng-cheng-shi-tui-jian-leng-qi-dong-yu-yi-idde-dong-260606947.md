---
title: 'DREAM: Dynamic Refinement of Early Assignment Mappings'
title_zh: DREAM：生成式推荐冷启动语义ID的动态渐进修正
authors:
- Liwei Guan
- Huanjie Wang
- Hongwei Zhang
- Linxun Chen
- Zhaojie Liu
affiliations:
- Kuaishou Technology
arxiv_id: '2606.06947'
url: https://arxiv.org/abs/2606.06947
pdf_url: https://arxiv.org/pdf/2606.06947
published: '2026-06-05'
collected: '2026-06-08'
category: GenRec
direction: 生成式推荐 · Semantic ID冷启动优化
tags:
- Semantic ID
- Cold-Start
- Generative Recommendation
- Item Tokenization
- Multi-Path Inference
- LoRA
one_liner: 首次指出SID早期静态提交是冷启动瓶颈，通过渐进式候选池构建、保守提交与多路径推理提升冷物品召回4-12倍
practical_value: '- **渐进式 SID 修正思路**：将 Semantic ID 从一次性固定变为可逐步修正的接口，冷启动物品在获得足够交互证据前不强制提交单一路径，可借鉴到电商生成式推荐
  pipeline 中，避免新商品因初始 SID 偏差而长期不可达。

  - **冷启动候选池生成（CART）**：通过对比学习与反事实硬负例（CHN）构造行为对齐的候选 SID 池，可迁移至电商场景：为新商品预生成多个合理 SID，而非依赖单一的离线量化结果。

  - **低成本保守提交策略（UC3）**：利用冻结推荐模型评估候选 SID 的置信度加权投票，仅当支持度与边距均达标才更新主路径，否则回退至先验，这种无训练成本的评估机制可直接用于线上冷启动物品的
  SID 安全切换。

  - **多路径推理与冷温梯度隔离（CPDE）**：通过 LoRA 隔离冷物品梯度（避免干扰温物品）、维持动态束并注册多路径到约束解码树，可显著提高冷物品被生成命中的概率，适合工业级生成式推荐系统实现冷温解耦优化。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：基于 Semantic ID（SID）的生成式推荐将物品检索转化为自回归生成，但冷启动物品在交互稀疏时被离线 tokenizer 一次性指定一个静态 SID，一旦该路径在行为空间中不匹配，约束解码仅注册该单一路径，导致冷物品在训练和推理阶段几乎不可达。现有工作未同时解决**无支持分配、过早提交、推理时单路径约束**这三个耦合问题，冷启动失败根源在于“早期静态单路径提交”而非模型容量不足。

**方法**：DREAM 用一个三阶段的渐进式框架替代固定 SID 分配。
- **第一阶段 CART（协作感知 token 优化）**：引入 collaborative alignment 损失和反事实硬负例（用 LLM 生成意图翻转描述，BM25 从目录检索真实负例），训练带有 diversity 正则的 Gumbel-Softmax 量器，为每个冷物品输出一个 top-K 候选 SID 池（K=8），主路径被更新为池内最优，修复 88% 冷物品的无支持分配。
- **第二阶段 UC3（用户条件候选压缩）**：冻结推荐模型作为零成本评估器，对每个冷物品候选 SID 在多个用户上下文中计算 teacher-forced NLL，转换为置信度加权投票，仅当票数超过支持阈值且最高票与次高票差超过边距阈值时才提交新 SID，否则回退到 CART 先验，89.4% 的冷物品保持 CART 主路径。
- **第三阶段 CPDE（冷保留动态束演化）**：在 LoRA 隔离冷物品梯度的同时，保留每个冷物品的前 B 个候选作为动态束，用 soft 多目标训练和动量 EMA 更新束权重，推理时注册所有束路径到约束解码 Trie，实现多路径恢复。

**实验结果**：在 Amazon Beauty、Sports、Toys 三个基准上，DREAM 在所有 18 项冷启动指标上大幅超越 SID 生成式基线（TIGER、LETTER、LC-Rec、SpecGR）及传统序列模型，提升幅度 4.3× 到 11.5×；整体指标保持竞争力，Sports 上全面最优。消融实验证实各阶段单调贡献，CART 单独带来冷指标数十倍提升，UC3 通过 gates 进一步精炼，CPDE 多路径推理比单路径额外恢复 30–40% 冷物品命中。
