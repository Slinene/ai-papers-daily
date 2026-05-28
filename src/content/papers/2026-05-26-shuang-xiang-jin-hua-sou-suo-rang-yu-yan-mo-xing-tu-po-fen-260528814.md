---
title: Self-Improving Language Models with Bidirectional Evolutionary Search
title_zh: 双向进化搜索：让语言模型突破分布边界自我改进
authors:
- Guowei Xu
- Zhenting Qi
- Huangyuan Su
- Weirui Ye
- Himabindu Lakkaraju
- Sham M. Kakade
- Yilun Du
affiliations:
- Harvard University
- MIT
arxiv_id: '2605.28814'
url: https://arxiv.org/abs/2605.28814
pdf_url: https://arxiv.org/pdf/2605.28814
published: '2026-05-26'
collected: '2026-05-28'
category: LLM
direction: 双向进化搜索 · 自改进采样
tags:
- self-improvement
- evolutionary search
- bidirectional search
- LLM agents
- training data generation
- tree search
one_liner: 提出双向进化搜索框架，用进化算子突破模型候选分布局限，通过后向目标分解提供密集反馈
practical_value: '- **进化算子重组轨迹，逃离模型概率高熵壳**：在前向搜索中引入组合、转位、删除、交叉四种算子，将不同候选的部分轨迹拼接/编辑，生成单次自回归不易产生的多样化样本。电商
  Agent 的复杂多步推理中，可借鉴这种思路从已有交互日志中合成新候选，提升长尾问题覆盖率。

  - **后向目标分解提供密集验证信号**：通过递归拆解任务为可检查子目标（例如多跳 QA 可分成“检索第一跳事实”“验证中间结论”等），为部分完成的轨迹输出细粒度得分。可用在电商多轮对话或
  Tool-use Agent 的中间步骤评分，避免稀疏奖励导致训练不稳定。

  - **即插即用的采样替代方案**：BES 可替换任何 RL 后训练（如 GRPO）中的 i.i.d. 采样阶段，为困难任务发现高奖励训练样本，使基座模型获得明显提升（如
  MuSiQue 上 +3.8%）。电商搜索 Agent 的训练中可直接集成，无需修改原有 RL 算法。

  - **工程实现灵活**：进化算子既可直接编辑 token 序列，也可用 LLM 提示实现（本文在代码生成任务中采用后者）；子目标验证器支持规则、代码执行、嵌入相似度或
  LLM 评判，易于根据业务场景快速适配。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
当前 LLM 自改进的主流采样方法（best-of‑N、树搜索）受限于两个瓶颈：（1）验证信号稀疏，仅靠最终答案评分，难以引导中间步骤；（2）候选生成全靠自回归扩展，局限在模型自身的高概率区域，无法触及低概率但正确的解。针对这一问题，本文提出双向进化搜索（BES），融合前向进化算子与后向目标分解，同时突破候选分布和验证信号的质量边界。

**方法**  
- **前向搜索**：维护候选轨迹集合，每步以 Boltzmann 分布选父节点，随机应用扩张（模型生成新步骤）或四种进化算子 —— 组合（拼接不同轨迹的后缀）、转位（用一条轨迹的单步替换另一条）、删除、交叉（交换前后缀），产生难以由单次 rollout 到达的新候选。  
- **后向搜索**：将原问题递归分解为子目标树，每个子目标有独立验证器；用自底向上加权平均为部分轨迹计算密集得分 `s(n)`，并为两两节点计算互补得分，驱动前向搜索选择与配对。  
- **理论支撑**：证明纯扩张搜索的候选几乎被限制在熵为 `H_T` 的狭窄壳内，而 k‑次进化候选的期望对数概率超越壳边界；后向子目标信号可将所需样本数从 `O(1/∏p_i)` 指数降至 `O(p_min^{−1} log m)`。

**实验**  
- **后训练**：在 Knights‑and‑Knaves 逻辑推理上，GRPO/MaxRL 几乎无提升，BES 持续提升验证准确率；在 MuSiQue 多跳 Agent 任务上，BES 使 Llama‑3.2‑3B 准确率从 4.0% 升至 7.0%（+3.0%），Llama‑3.1‑8B 从 6.6% 升至 10.4%（+3.8%），均显著优于 Tree‑GRPO，且模型学会主动搜索而非猜测。  
- **推理**：在 Circle Packing (Square/Rect) 和 Heilbronn 开放问题上，BES 的平均分与最佳分均超过所有开源框架（OpenEvolve、GEPA、ShinkaEvolve），且跨运行方差更低，稳定性更强。  
- **消融与成本**：移除进化算子或答案重加权均导致性能下降；与 Tree‑GRPO 相比，BES 不到 30% 的额外时间开销换取了大幅精度提升。  

**核心洞见**  
> 将搜索从模型的自回归延伸转变为"重组+验证"的进化过程，并利用子目标分解把稀疏奖励变成密集信号，是让 LLM 在困难任务上稳定自改进的关键。
