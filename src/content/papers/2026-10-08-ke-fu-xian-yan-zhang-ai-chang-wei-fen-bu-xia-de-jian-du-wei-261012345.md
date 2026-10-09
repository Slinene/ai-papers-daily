---
title: 'Overcoming Prior Barriers: Supervised Fine-Tuning under Long-Tail Distribution'
title_zh: 克服先验障碍：长尾分布下的监督微调
authors:
- Haohui Wang
- Jiahao Xu
- Wangzhi Zhan
- Tong Zeng
- Dongqi Fu
- Hong Li
- Swastik Roy
- Naren Ramakrishnan
- Chris North
- Jian Kang
affiliations:
- Virginia Tech
- Amazon
- Meta
- MBZUAI
- Dartmouth College
arxiv_id: '2610.12345'
url: https://arxiv.org/abs/2610.12345
pdf_url: https://arxiv.org/pdf/2610.12345
published: '2026-10-08'
collected: '2026-10-09'
category: Training
direction: LLM SFT 数据选择 · 先验障碍
tags:
- SFT
- instruction selection
- long-tail
- prior barrier
- data budget allocation
- LoRA
one_liner: 提出 prior barrier 概念与 PASS 方法，自适应分配 SFT 预算以克服长尾预训练支持差异
practical_value: '- 指令微调前，先对业务指令/参考集做 response embedding 聚类，形成 capability/concept
  粒度；用预训练模型在各 concept 上生成响应，估计 support 和 prior barrier，优先给生成差且混淆多的类目分配 SFT 预算，避免按任务均分。

  - 样本打分建议从 query 相似度升级为「正确响应 vs 竞争响应」的区分证据：用正确与错误/易混淆 response 表示构建 evidence matrix，选样时同时惩罚语义重复和有害/竞争样本，适合电商客服、商品导购
  Agent 中意图边界模糊的场景。

  - 该方法采用边际增益贪心，计算成本低于 LESS/TSDS，适合大规模候选 prompt 库筛选；对已有 LoRA SFT 流程可直接插入，用于提升长尾品类/任务能力。

  - 即使不用完整 PASS，也可借鉴「先验障碍 + 自适应分配」思路：训练前用少量 reference 测模型各能力的 base 表现，按 head/tail
  设置差异化数据配额。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
SFT 面临指令池远大于微调预算，而不同目标概念从预训练获得的支撑差异很大：高频概念先验强，稀有概念弱，形成长尾 prior barrier。已有数据选择方法多按质量、相似度或梯度影响力打分，忽略概念级需求差异，导致尾概念覆盖不足。

**方法关键点**
- 定义 prior barrier B(r) 衡量预训练对目标概念相对竞争概念的支持劣势；理论推导预测风险界，显示后验集中由 SFT 证据 nϵ(r) 与 B(r) 共同决定，尾概念需要更多样本。
- PASS 分两模块：M1 用 reference response 表示做层次聚类得到概念集，为每条候选指令计算区分证据 ϵ_iθ，即正确表示与最强竞争表示相似度之差的校准值；M2 用预训练模型生成响应估计每个概念的 B_θ 与 support γ_θ，得到分配权重 A_θ∝exp(B_θ)/γ_θ。
- 选择目标同时奖励正区分证据、惩罚负证据与语义冗余，用边际增益贪心选子集。

**关键实验**
候选池 300,932 条，来自 FLAN V2/OASST1/WizardLM/Dolly/Alpaca；下游覆盖 MMLU/BBH/GSM8K/TruthfulQA/TyDiQA。在 Mistral-7B/Qwen2.5-7B、5k/10k 预算下对比 7 个 baseline，PASS 在所有设置总体最优。Mistral 5k 得分 51.5，超过所有 baseline 用 10k 的最佳 50.9；自适应分配 vs uniform 提升 +0.29 至 +0.56。

**最值得记住的一句话**
SFT 数据选择不只是找高分样本，更要按 prior barrier 把预算分配到预训练覆盖不足的长尾概念上。
