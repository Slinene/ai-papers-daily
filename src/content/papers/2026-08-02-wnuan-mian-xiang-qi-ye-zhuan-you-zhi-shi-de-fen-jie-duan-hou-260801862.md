---
title: 'Wnuan: Staged Post-Training for Question Answering over Proprietary Enterprise
  Knowledge'
title_zh: Wnuan：面向企业专有知识的分阶段后训练问答系统
authors:
- Xiaofeng Shi
- Xiaosong Qiu
- Wenxin Ma
- Qian Kou
- Yiming Pan
- Longbin Yu
- Ying Liu
- Haiping Wang
- Hua Zhou
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
- Beijing District Heating Group Co., Ltd. (BDHG)
- Beijing University of Posts and Telecommunications (BUPT)
arxiv_id: '2608.01862'
url: https://arxiv.org/abs/2608.01862
pdf_url: https://arxiv.org/pdf/2608.01862
published: '2026-08-02'
collected: '2026-08-05'
category: Training
direction: 后训练 · 领域适应
tags:
- enterprise QA
- post-training
- GRPO
- residual error sampling
- SFT
- data selection
one_liner: 三阶段后训练流程将企业 QA 可接受率从 52.76% 提升至 91.51%，其中残差错误采样 RL 显著优于全量采样
practical_value: '- **残差错误采样策略**：RL 微调阶段优先选择 SFT 后仍答错的样本进行 GRPO，在固定更新预算下比全量采样或等量随机采样
  AAR 提升约 3 个百分点，可用于对话式推荐或智能客服的错误修正优先级设定。

  - **通用数据混练抑制能力退化**：在领域 SFT 中混入 48.3% 通用数据，以通用 benchmark 平均分最高为选择准则，牺牲少量领域精度换来指令跟随等通用能力的较好保持，对平衡业务专训与通用能力有直接参考。

  - **文档到 QA 的自动化构造**：将非结构化企业文档（如操作手册、技术标准）自动转化为自包含问答对，并经过规则、忠实度等多轮筛选，可用于从商品描述、活动规则等生成训练样本。

  - **多模型集成评估 + 人工校准**：采用两主评委加分歧时第三模型投票的集成判分，并用领域专家校准 90.5% 的一致性（Cohen''s κ=0.796），适合低成本构建可靠的业务离线评估体系。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
企业知识问答依赖内部策略、技术标准等专有信息，但通用大模型缺乏这些知识。需要在不损害通用能力的前提下高效融入领域知识，现有工作多单独解决，缺乏端到端流水线。

### 方法
提出 **Wnuan** 三阶段后训练流程：
1. **文档到 QA 构造**：将私有文档切块、生成自包含问题（6 种任务形式），基于 DeepSeek-V3.2 生成答案，经规则、忠实度、质量过滤，再用目标模型改写对齐风格，保留约 22 万对。
2. **SFT + 通用数据回放**：在领域 QA 上全参微调 Qwen3-32B，同时混入 48.3% 通用指令数据（以 MMLU、IFEval、C-Eval 平均分最高选择回放比例），获得 Wnuan-Inst。
3. **残差错误 RL**：用 Wnuan-Inst 筛选出仍答错的 5.6 万样本，结合语义奖励（正确性 0.6、逻辑/专业/简洁 0.3、格式 0.1）进行 GRPO，在错误集上进一步优化。

### 关键结果
- 在 707 题私有基准 WnuanBench 上，32B 路线可接受答案率（AAR）从基线的 52.76% 升至 80.06%（SFT）再至 91.51%（RL），幻觉率从 65.91% 降至 15.70%。
- 控制实验中，相同 100 更新步数下，残差采样 AAR=89.39%，显著高于全量池随机采样 86.42% 和等量随机采样 86.28%，源文档 bootstrap 区间均大于零。
- 通用能力平均下降 5.17 点，主要损失在指令遵循（IFEval），但 MMLU 和 C-Eval 微升。
- 与领域专家校准，最终集成判分一致性达 90.5%（κ=0.796）。

**核心结论**：将有限的 RL 更新预算集中在 SFT 后的剩余错误上是一种高效的企业专训策略，但需要付出一定的通用指令遵循代价。
