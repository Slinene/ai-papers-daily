---
title: 'EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making'
title_zh: EVOKE：通过目标多样性引出世界知识以提升 Agent 可迁移决策
authors:
- Yuhan Guo
- Jinming Liu
- Liang Xu
- Ziqiang Li
- Jianguo Huang
- Zhicheng Wang
- Hu Zhu
- Qiuyu Chen
- Yuntao Wei
- Xin Jin
affiliations:
- Shanghai Jiaotong University
- Hong Kong Polytechnic University
- Eastern Institute of Technology, Ningbo
arxiv_id: '2609.38334'
url: https://arxiv.org/abs/2609.38334
pdf_url: https://arxiv.org/pdf/2609.38334
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: Agent 后训练 · 世界知识引出
tags:
- LLM Agents
- World Knowledge
- Post-training
- Goal Diversity
- Contrastive Ranking
- Transferability
one_liner: 固定状态与历史、切换目标并对同一组动作做排序监督，迫使策略调用预训练世界知识做决策，而非依赖单目标习惯
practical_value: '- 在电商/导购 Agent 中，可以对同一页面（商品详情、购物车、结算页）构造多个互斥目标（立即下单、修改地址、比价、取消订单），让策略在相同
  state/history 下对同一组候选动作排序；只要不同目标偏好反转，就能强制模型使用动作后果知识，而不是记住单目标下的页面习惯，提升未见过活动页/新商城环境的泛化。

  - 用「策略当前高分但被环境反馈判定为不推进目标」的动作作为 hard negative，结合 pairwise + listwise ranking，而不是只对
  positive 做 SFT，能显著抑制线上 Agent 的惯常错误动作，减少无效点击和重复访问；电商搜索 Agent 可直接用日志反馈构造这类负样本。

  - 训练时用 LLM 标注器对真实执行结果做 grounded 标注（实际执行后的 next page/结果），不把预测状态喂给策略；推理时部署标准 policy，无世界模型/规划模块，适合低延迟线上服务。可以借鉴「标注用执行结果，推理零额外开销」的设计。

  - 数据效率高：ALFWorld 上仅用约 9% 的演示步数做多目标排序，unseen success 从 60.4% 拉到 91.8%；用当前策略 rollout
  并 DAgger 式多轮聚合 policy-favored negatives，适合在电商仿真器/线上日志中低成本持续迭代。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent 在多步决策中通常跨环境迁移差。世界模型方法通过预测未来观察来获取动作后果知识，但训练成本高、且预测误差会在规划中累积。对数字环境中的 LLM Agent，大量后果知识已在预训练中内部化，问题更多在于如何引出而不是重新获取。单目标监督容易让策略依赖上下文习惯，训练分布内有效，换环境就失效。

### 方法关键点
- **目标干预**：在策略 rollout 收集的状态上，保持 state、history、available actions 不变，替换成多个可达到的替代目标，形成多目标上下文。
- **接地动作评估**：对每个候选动作在环境中实际执行并观察结果，由 LLM 标注器判断是否推进当前目标，而非预测未来状态。
- **对比排序监督**：用 mean token log-prob 给动作打分，采用 listwise + pairwise ranking loss；优先把策略当前高分但被判定为不推进目标的动作作为 hard negatives。
- **迭代聚合**：DAgger 式多轮训练，每轮用当前策略在线交互收集新状态，把新错误加入训练集，LoRA 更新。

### 关键结果
- ALFWorld Unseen 上，Qwen2.5-3B/7B/Qwen3-1.7B 分别为 91.1/93.1/84.6，超过各自最佳 baseline 约 5-9 个点；WebShop 7B score/success 达 90.6/85.9。
- 消融显示：去掉 goal intervention，unseen 从 91.8 降到 82.8；同样目标数据只用 SFT 只能到 84.3，说明 ranking 和多目标压力是关键。
- 线性探针表明预训练 backbone 已经能高度解码动作后果，但 πboot 只解决 60.4% unseen；EVOKE 将 habitual error 从 23.3% 降至 6.4%，说明知识被引出而非新增。
- 数据效率：用 60% 标注状态即可超过全量 SFT。

### 值得记住的一句话
对 LLM Agent，固定状态上的多目标偏好排序比额外训练世界模型预测未来更轻，更能把预训练已有的世界知识逼出来用于决策。
