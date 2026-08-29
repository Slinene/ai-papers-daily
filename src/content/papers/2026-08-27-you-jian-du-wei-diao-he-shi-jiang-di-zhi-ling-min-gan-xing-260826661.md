---
title: When Does Supervised Fine-Tuning Reduce Instruction Sensitivity?
title_zh: 有监督微调何时降低指令敏感性？
authors:
- Jaekeol Choi
affiliations:
- Hankuk University of Foreign Studies
arxiv_id: '2608.26661'
url: https://arxiv.org/abs/2608.26661
pdf_url: https://arxiv.org/pdf/2608.26661
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: LLM 指令敏感性 · SFT 训练指令依赖
tags:
- instruction sensitivity
- supervised fine-tuning
- prompt robustness
- LLM ranking
- evaluation protocol
- LoRA
one_liner: SFT对指令敏感性的影响随模型规模、训练指令和评估协议变化，不一定降低鲁棒性
practical_value: '- 在电商搜索相关性/排序模型的 LLM 微调中，上线前用 10+ 条语义等价指令变体评估，报告指令敏感度（标准差），避免单条
  prompt 造成的假象；尤其对于 1.7B/4B 小模型，固定指令 SFT 本身就能大幅降低敏感度，可以作为快速鲁棒化手段。

  - 对于 >8B 模型的 LoRA 微调，训练指令的选择会影响鲁棒性：在 Qwen3-8B 上简短指令（TA）比详细指令（TB/TC）带来更低的 post-SFT
  敏感度，且差异显著；因此在大模型任务适配时，应尝试多个训练 prompt 并用 bootstrap 检验敏感性差异。

  - 评估协议选择会直接改变鲁棒性结论：在 ESCI 上自由生成（greedy+prefix）显示 SFT 后更敏感，而强制选择（label likelihood）没有该问题，即使
  valid-label 率 >99.8%。在搜索排序场景用 likelihood scoring 比生成式解码更稳定，能减少评估伪影。

  - 任务效果和指令鲁棒性要分开监控：SFT 可以提升 nDCG/准确率但可能增加指令敏感性（如 Qwen3-8B + TB），不要用平均指标代替鲁棒性评估。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 对同一任务的不同指令表述会产生显著性能差异，但常规固定指令 SFT 是否会改变这种指令敏感性尚不明确。在搜索相关性判断/重排场景中，指令变化会直接影响相关性分数和排序结果，单条指令评估可能掩盖部署可靠性问题。

**方法关键点**：
- 定义指令敏感性为同一任务下 10 个语义等价指令变体上任务性能的标准差。
- 使用 Qwen3 1.7B/4B/8B 进行规模化分析，Mistral-7B 和 Gemma-2-9B 做跨模型验证。
- 在 MS MARCO 上做 passage ranking，SFT 用两种/三种不同训练指令（TA、TB、TC），LoRA 微调；评估用 TREC DL 2019 nDCG@10，无训练指令重叠。
- 用 paired query-level bootstrap（10k 重采样）计算 ΔS 和 D 的置信区间。
- ESCI-English 上对比自由生成（greedy decode + prefix match）与强制选择（label likelihood）两种评估协议。

**关键结果**：
- SFT 前 Qwen3 指令敏感性随规模急剧下降：1.7B S=0.0905，4B S=0.0332，8B S=0.0126。
- 1.7B 和 4B 上固定指令 SFT 可靠降低敏感性：1.7B 降 70.7%（TA）/67.0%（TB），4B 降 57.1%/54.3%，置信区间全在 0 以下。
- 8B 上单个敏感性变化不显著（TA ΔS=-0.0039，TB ΔS=+0.0063），但训练指令对比 D=0.0103，95% CI [0.0021,0.0173]，P(D>0)=0.996，且三种子一致；TC-TA 也类似。
- 跨模型：Gemma-2-9B 方向同 Qwen3-8B（D=0.0024，CI 含 0），Mistral-7B 无此模式。
- ESCI 上两种协议平均准确率相近（约 0.656 提升至 0.672），但自由生成显示 SFT 后敏感性上升（0.0121→0.0141/0.0171），强制选择不上升（0.0136→0.0119/0.0138），valid-label 率 0.9983，说明是评估协议差异而非格式失败。

**最值得记住的一句话**：SFT 并不总是降低指令敏感性，其鲁棒性效果依赖模型规模、训练指令和评估协议，平均任务性能提升不能替代鲁棒性评估。
