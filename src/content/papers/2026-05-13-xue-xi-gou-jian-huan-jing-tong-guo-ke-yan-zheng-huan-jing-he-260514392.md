---
title: 'Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable
  Environment Synthesis'
title_zh: 学习构建环境：通过可验证环境合成实现自我进化的推理强化学习
authors:
- Yucheng Shi
- Zhenwen Liang
- Kishan Panaganti
- Dian Yu
- Wenhao Yu
- Haitao Mi
affiliations:
- Tencent
arxiv_id: '2605.14392'
url: https://arxiv.org/abs/2605.14392
pdf_url: https://arxiv.org/pdf/2605.14392
published: '2026-05-13'
collected: '2026-05-15'
category: Reasoning
tags:
- RLVR
- Self-Improvement
- Environment Synthesis
- Reasoning
- GRPO
- Zero-data
one_liner: 提出EvoEnv，让语言模型自行构建可执行环境以提供稳定且随能力动态校准的奖励，将自改进从数据生成循环转为环境构建循环
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**

现有自训练方法要么依赖固定验证分布，随着策略改进逐渐饱和、奖励信号变弱，要么使用策略耦合的自生成标签，导致奖励不稳定。EvoEnv 重新审视自我改进的本质：不局限于生成更多训练数据，而是让模型学会构建可重用的、可执行的环境，这些环境能够动态采样新实例并提供由代码执行保证的稳定奖励。

**方法关键点**

- **环境接口**：每个环境是一个 Python 类，实现 `_generate`（生成实例与参考答案）、`_prompt_generate`（渲染自然语言提示）和 `scorer`（基于执行结果评分），确保奖励来自冻结代码而非模型信念。
- **验证与准入**：候选环境须通过五层机械验证（语法、执行、确定性、非平凡性、评分器契约），再经同模型多轮语义自审（识别算法错误、答案泄露等），最后进行求解器相对难度校准（要求当前策略准确率在 0~1 之间，目标 0.3）和新颖性过滤（基于嵌入相似度），防止模板崩塌。
- **联合训练**：单一策略交替扮演生成器（提出新环境）和求解器（解答环境采样的问题），通过 GRPO 优化。生成器奖励由验证质量、难度校准和新颖性探索奖励组合而成；求解器仅从已准入环境的执行反馈中学习。
- **池管理**：接受的环境进入活跃池，定期退役，退役环境可作为未来生成器的种子，保持课程的前沿性和多样性。

**关键实验**

在三个基模型（Qwen3-4B-Instruct、Qwen3-4B-Thinking、Nemotron-Cascade-8B）上，EvoEnv 均取得一致改进。最强证据来自已较强的 Qwen3-4B-Thinking：其平均 pass@1 从 72.4 提升至 74.8，而固定公开数据 RLVR（DAPO）和固定手工环境 RLVR（RLVE）分别降至 64.8 和 69.2。训练动态显示，EvoEnv 的求解器训练得分随进程下降（因生成器持续合成更难环境），但留出集准确率从 72.4% 升至 80.4%，证明难度可控且奖励信号保持有效。消融实验表明，质量奖励和多样性奖励二者缺一不可，单独移除均导致增益大幅缩小。

**核心洞察**

稳定的自改进不源于合成更多数据，而源于模型学会构建其训练的世界——那些难度在结构上持续超出自身推理能力的世界。
