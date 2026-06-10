---
title: 'Atomic Intent Reasoning: Bringing LLM Semantics to Industrial Cross-Domain
  Recommendations'
title_zh: 原子意图推理：将 LLM 语义引入工业跨域推荐
authors:
- Zhuohang Jiang
- Yuxin Chen
- Shijie Wang
- Haohao Qu
- Zhou Jindong
- Wenqi Fan
- Li Qing
- Dongxu Liang
- Jun Wang
affiliations:
- The Hong Kong Polytechnic University
- Kuaishou Technology
arxiv_id: '2606.10357'
url: https://arxiv.org/abs/2606.10357
pdf_url: https://arxiv.org/pdf/2606.10357
published: '2026-06-09'
collected: '2026-06-10'
category: RecSys
direction: 跨域推荐 · LLM 意图缓存与检索
tags:
- Cross-Domain Recommendation
- LLM
- Intent Modeling
- Industrial Deployment
- Semantic Retrieval
- CTR Prediction
one_liner: 离线将用户行为拆解为原子意图并缓存，在线动态组合实现 LLM 级语义推理，延迟仅 20ms
practical_value: '- **离线 LLM 意图预计算 + 在线轻量聚合**：把昂贵的大模型推理完全移到离线阶段，将用户事件转化为可检索的原子意图对（action-intent
  pair），在线仅做 KV 检索和树合并。在电商/内容平台的跨域推荐中，可以直接复用这种“离线语义提炼、在线实时组合”的范式，突破 LLM 在线推理的延迟瓶颈，同时保持语义信号。

  - **层次用户意图树的构建与多行为权重**：用意图树组织 coarse-to-fine 的偏好，节点权重融合 click/order/view 等多种行为计数并引入时间衰减。在自己的业务中，可以借鉴这种多行为强度加权与时效性折损的统一方案，有效压缩超长、异构行为序列，避免喂入原始全量序列的噪声与计算开销。

  - **目标感知的意图检索与证据压缩**：根据候选商品 embedding 从意图树中检索相关链，再按语义相似度和时间有效性裁剪支持证据序列，输出一个紧凑的“意图链+行为证据”作为
  CTR 模型输入。在重排或精排环节，这可以提供高度目标相关的精简特征，代替手工构造的跨域行为序列特征，提升预测效果。

  - **多注意力融合意图表示**：将检索到的意图链 token 以 MHA 方式与目标商品 embedding 交互，不同 head 捕捉不同粒度的偏好。可以作为排序模型中一个可插拔的目标感知用户表示模块，插入到现有的
  DNN 排序塔中，只需增加较小的计算量。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业跨域推荐（如短视频→电商）面临两大难题：1) 内容域与商品域存在严重语义鸿沟，传统 ID 协同迁移难以捕捉细粒度的购买意图；2) 用户跨域行为序列极长且噪声大，直接输入模型不仅计算负担重，还会引入大量无关信号。大语言模型（LLM）虽然具备强大的语义理解和推理能力，但其在线推理延迟（秒级）无法满足毫秒级工业服务要求。为此，本文提出 AIR（Atomic Intent Reasoning）框架，通过离线 LLM 预计算与在线轻量检索组合，在保证语义一致性的同时，将推理延迟降至 20ms，吞吐提升约 400 倍。

**方法关键点**
- **原子意图对生成**：离线利用 LLM（Qwen3-4B）将每个用户事件（动作、物体、用户画像）转化为一组层次化的意图路径（如“猫视频→宠物用品→猫窝”），并按动作类型分别缓存为行为-意图对。
- **实时统一意图树构建**：在线将用户近期行为对应的所有意图路径快速聚合为一棵加权意图树，节点权重融合多种行为频次（click/order/view）和时间衰减，支撑轻量级实时更新。
- **目标感知意图检索**：给定候选商品，通过其文本 embedding 与意图树节点计算语义相似度，自顶向下检索出目标相关的意图链，并按权重裁剪出紧凑的支撑行为证据序列，有效滤除噪声。
- **MHA 意图抽取与融合**：将检索到的意图链 token 与目标商品 embedding 送入多头注意力，得到目标条件化的意图表示，拼入现有 CTR 预测模型。

**关键实验**
在公开数据集 Amazon Movie-Book 和 Food-Kitchen 上，AIR 的 HR@10 分别达到 0.151/0.215 (Movie/Book) 和 0.437/0.452 (Food/Kitchen)，显著优于 LLMCDSR、C2DSR 等 SOTA 基线，尤其在冷启动和非重叠用户场景提升突出。工业级 A/B 测试在快手电商真实流量中运行，相较生产基线，GMV 提升 +3.446%，GPM 提升 +3.662%，付费订单数提升 +1.043%。消融实验证明目标感知检索和意图树是两个强耦合的核心模块，同时移除会导致性能剧烈下降 40% 以上。在线延迟分析显示，AIR 推理耗时仅 20.134ms，相对直接调用 LLM 的 8s 延迟实现了约 400× 吞吐增益。

**核心结论**
“通过离线 LLM 原子意图缓存与在线层次意图树组合，能够在工业推荐系统中实现等效实时 LLM 推理的语义信号，同时满足毫秒级延迟和低计算成本，显著提升跨域转化效果。”
