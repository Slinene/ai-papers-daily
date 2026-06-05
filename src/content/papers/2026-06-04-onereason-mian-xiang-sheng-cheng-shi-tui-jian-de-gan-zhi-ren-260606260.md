---
title: OneReason Technical Report
title_zh: OneReason：面向生成式推荐的感知-认知推理模型
authors:
- OneRec Team
- Biao Yang
- Boyang Ding
- Chenglong Chu
- Dunju Zang
- Fei Pan
- Han Li
- Hao Jiang
- Honghui Bao
- Huanjie Wang
affiliations:
- Kuaishou
arxiv_id: '2606.06260'
url: https://arxiv.org/abs/2606.06260
pdf_url: https://arxiv.org/pdf/2606.06260
published: '2026-06-04'
collected: '2026-06-05'
category: GenRec
direction: 生成式推荐 · Semantic ID · 推理增强
tags:
- Generative Recommendation
- Chain-of-Thought
- Itemic Token
- Perception-Cognition
- RL
- Multi-Domain Rec
one_liner: 通过多粒度预训练、层次化 CoT SFT 和“先专后统”RL，首次在生成式推荐中让思考模式稳定超越非思考模式
practical_value: '- **多粒度预训练数据设计**：将推荐语料构建成 token→item→relational→user 四个层次，其中 token
  级构造组合语义预测、item 级做容量感知的caption粗粒化、relational 级生成兴趣流转解释、user 级混入跨域时间线与text替换。电商/短视频场景可直接复用这种分层来强化物品语义表示和用户理解。

  - **推荐 CoT 模板与监督**：定义 R0（感知）→R1（推导）→R2（演化）→R3（推荐）的层次化 SFT，每条 CoT 先压缩用户历史为兴趣状态，再基于状态推理下一交互。实际业务中，可以参照该模板用
  LLM 为历史序列打标兴趣点，构建带推理痕迹的训练数据，提升模型的解释性与准确率。

  - **“先专后统”RL 策略**：在多模块推荐场景中，先在每个单域做 RL 解锁思考模式增益，再通过拒绝采样微调或多教师蒸馏跨域平衡。对于电商/广告/直播等多业务线融合训练，可避免域间干扰，稳定提升整体收益。

  - **CoT 监督向非思考模式的迁移**：论文发现将 CoT 推荐数据混入训练，可以提升非思考直接生成的性能。对于线上延迟敏感、无法实时推理的场景，可在训练阶段使用
  CoT 数据，推理时丢弃思考过程，既保持低延迟又获得效果提升。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：OneRec 系列生成式推荐模型在多个业务中验证了 Scaling 红利，但即便引入了跨模态的思考链（CoT），思考模式并未在推荐基准上展现出稳定优势。受多模态 LLM 中推理脆性研究启发，指出生成式推荐的有效推理需要两个支柱：感知（将 itemic token 与底层语言语义对齐）和认知（将用户行为序列重组为连贯的潜在兴趣点）。

**方法关键点**：
- **预训练**：设计了 token / item / relational / user 四粒度推荐语料，实现从子词组合语义到用户时序行为的跨模态融合。token 粒度引入组合前缀语义预测与部分到整体推理；item 粒度做容量感知的 caption 粗粒化与多视角 QA；relational 粒度利用搜索-播放表、共现图构造并解释物品间兴趣流转；user 粒度按域分组或时序交织行为序列，并以 caption 随机替换 itemic token 来强化对齐。
- **SFT**：构建 R0 感知（双向 item↔caption 映射 + 属性 QA）→R1 推导（单跳 item-to-item 关联）→R2 演化（从抽取相关行为到生成兴趣演化链）→R3 推荐（综合压缩与判断的完整 CoT）的四级推理监督。CoT 格式先压缩历史为兴趣状态，再基于状态推理下一动作。
- **RL**：采用“先专后统”策略：先在各单域进行推荐导向 RL 解锁思考模式优势，再通过拒绝采样微调或多教师在线蒸馏进行跨域平衡。

**关键实验**：
- 多粒度预训练消融显示，每增加一层粒度都能带来 R0~R3 任务的渐进提升，其中用户粒度对跨域推荐的增益最大（Cross-Live 从 3.25% 升至 8.56%）。
- 在快手四个业务域（短视频、电商、广告、直播）的 OneReason-Bench 上，OneReason-8B 的思考模式全面超越非思考模式，达到 SOTA 性能。
- 用 CoT 监督数据替换等量的纯推荐数据，非思考推理的指标在多个域上也得到提升，表明推理信号可迁移至直接解码。
