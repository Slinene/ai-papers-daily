---
title: Unpaired Modality-Agnostic Generative Recommendation
title_zh: 未配对模态无关的生成式推荐
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Meng Yuan
- Yuqin Lan
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2608.02477'
url: https://arxiv.org/abs/2608.02477
pdf_url: https://arxiv.org/pdf/2608.02477
published: '2026-08-03'
collected: '2026-08-04'
category: GenRec
direction: 生成式推荐 · 未配对多模态语义ID学习
tags:
- Semantic ID
- Generative Recommendation
- Multimodal
- Unpaired Learning
- Residual Quantization
- Modality-Agnostic
one_liner: 让生成式推荐从配对、纯图、纯文混合数据中学习统一的语义ID空间，消除多模态配对瓶颈
practical_value: '- **利用未配对商品数据直接优化语义ID**：电商商品图、文经常独立维护，配对覆盖率不足。可借鉴 UnpairGR 的共享 Transformer
  主干和残差码本设计，让只有图片或只有标题的商品也能参与训练相同的离散 tokenizer，不依赖特征补全或独立码本。

  - **轻量输入端投影 + 共享编码器**：将模态特定处理限制在浅层投影层，后续深层网络和码本完全共享。这样即使模态缺失，表征依然落在统一的量化空间，工程实现简单，避免多套
  tokenizer 和 fallback 逻辑。

  - **基于熵的可靠性加权共识**：对于配对商品，通过码本赋值的熵动态评估各模态置信度再做加权融合，优于简单平均。在商品描述质量参差不齐的场景（如标题噪音大、主图不清晰）可直接复用。

  - **分层码本 + 交叉观测一致性正则**：利用粗粒度语义对齐（早期码本）和细粒度差异容忍（后期码本）的特性，配合 JS 散度约束，能在未配对训练下保持同一商品不同模态输入生成相似前缀语义
  ID，这对后续的生成式检索或 Agent 工具调用中的 item 表示一致性很有用。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多模态生成式推荐（MM-GR）通常依赖商品级图像-文本配对数据来学习语义 ID，但真实电商场景中图文覆盖不均：卖家上传图片和运营编辑标题往往独立进行，大量有用数据以纯图或纯文形式存在，无法被现有方法直接利用。直接引入未配对数据会导致量化边界处微小表征偏移即产生不兼容的离散 ID，破坏生成式推荐器的 token 序列一致性。因此亟需让语义 ID 学习从配对、图像仅、文本仅三种观测中稳健地构建统一离散空间。

**方法**  
- **模态无关量化架构**：仅保留轻量的模态特定投射层 `P_v`、`P_t`，其后共享 Transformer 主干 `Φ_θ` 和 L 层残差码本 `{C^(l)}`，保证所有观测条件的表征都经过相同语义变换和量化。  
- **可靠性加权跨模态共识**：对配对商品，用各模态在共享码本上的赋值熵估计置信度，动态加权融合视觉和文本表征，抑制噪声模态干扰。  
- **混合监督训练**：统一量化损失 `L_mix` 同时处理配对、图像仅、文本仅样本；配合交叉观测一致性正则（JS 散度对齐软赋值 + 跨模态表征 L2 对齐）和码本使用率均衡正则（KL 散度），防止码本崩塌并保持不同观测下的 ID 兼容性。  
- **两步训练**：先固定 tokenizer 得到语义 ID，再用一个自回归推荐器以标准 next-item 方式生成 ID 序列，推理时根据商品可用模态选择统一 tokenizer 的分支，无需模态补全或回退模型。

**实验结果**  
在 Amazon Arts、Games、Instruments 三个数据集上：  
- 全量模态下，相比最强基线 SynGR，HR@1 提升 22.86%（Arts）、17.14%（Games），NDCG@5 提升 16.17%（Instruments）。  
- 模态缺失鲁棒性：不同缺失比例（×25%~100%）下 HR@10 均稳定优于 SynGR、MACRec 等；纯文本或纯图像极端情况下优势更明显（如 Games 纯图像 SynGR 仅 0.0364，UnpairGR 达 0.0904）。  
- 语义 ID 一致性：同商品的不同模态输入共享超过 87% 的粗粒度前缀码（P1），远超随机排列，保障单一推荐器可同时理解各种模态来源的 token。  
- 冷启动：纯单模态 token 生成即可实现有效推荐，无需额外模态重建。  
- 效率：相比 SynGR，训练时间减少 18%~42%，推理延迟降低 8%~21%，收敛更快。

**核心 insight**  
让成对和不成对数据共享同一个预量化变换和码本，比任何针对缺失模态的补救策略都更直接有效地维持离散 ID 空间的统一性——这个思路可以迁移到任何需要将异构信号离散化并保持一致性的生成式建模场景。
