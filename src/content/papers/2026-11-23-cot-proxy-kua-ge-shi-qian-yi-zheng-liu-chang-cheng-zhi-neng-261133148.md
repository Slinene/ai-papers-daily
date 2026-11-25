---
title: 'CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies'
title_zh: CoT-Proxy：跨格式迁移蒸馏长程智能体策略，无需教师思维链
authors:
- Dawid J. Kopiczko
- Tijmen Blankevoort
- Yuki M. Asano
affiliations:
- University of Technology Nuremberg
- NVIDIA
arxiv_id: '2611.33148'
url: https://arxiv.org/abs/2611.33148
pdf_url: https://arxiv.org/pdf/2611.33148
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: Agent 策略蒸馏 · 跨格式迁移
tags:
- Policy Distillation
- CoT-proxy
- Cross-format Transfer
- LoRA
- Replay Regularization
- Long-horizon Agents
one_liner: 仅用教师动作与短 CoT 摘要即可将长程智能体策略蒸馏到小推理模型，学生用自己的推理执行教师策略
practical_value: '- 蒸馏闭源强模型做电商/搜索/工具 Agent 时，不要依赖隐藏 CoT：直接用可观察动作/API 输出/Reasoning
  summary 训练。CoT-proxy 可把 API 返回的 reasoning summary 放在空 think block 后，能稳定提升任务成功率。

  - 防微调灾难遗忘：用 replay buffer + KL 正则，replay 数据必须来自目标域之外，训练时按 15% 比例混入；LoRA 下只需额外前向，工程成本低，适合保护原有推理/指令能力。

  - 数据构造上，剥离教师可见文本、只保留解析后的 action 更有效；CoT-proxy 摘要可廉价用同尺寸 Instruct 模型生成，不一定需要大教师。

  - 若业务在意模型推理风格/措辞延续，action-only 与 CoT-proxy 能保留学生自己的推理模式，避免 Full-CoT 训练让学生措辞完全向教师靠拢。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长程智能体策略通常靠 RL 或 SFT 教师轨迹。标准 SFT 同时模仿教师 CoT 和动作，但最强教师是闭源 API，CoT 被隐藏；且小模型学习强推理轨迹效果有限。需要一种只从可见输出中蒸馏策略、同时不破坏学生原有推理能力的方法。

方法关键点：
- 训练目标分三种：Full-CoT 监督思维链+动作；Action-only 预填空 think block，仅监督动作；CoT-proxy 在空 think block 后加 <summary> 摘要再跟动作。
- 跨格式迁移：训练时推理块为空且无损失，推理时开启思考，学生用自己的 CoT 执行学到的策略。
- Replay 正则：每个 batch 混 15% 学生初始模型在域外 prompt 上的生成，对这些位置做 KL(p_init||p_theta)，LoRA 下只需额外前向。
- 闭源教师仅用可见输出与 API 返回的 reasoning summary 构造 CoT-proxy；所有目标都剥离教师可见文本，只保留解析后的 action。

关键结果：开放教师 Qwen3.6-27B 上，Action-only 使 Qwen3-4B 在 AppWorld TGC 从 7.3% 到 17.9%，Qwen3-32B 从 11.5% 到 25.4%；CoT-proxy 进一步提升 Qwen3-4B 到 34.5%。闭源 GPT-5.6 Luna 上，Qwen3-4B Action-only 到 35.1%，CoT-proxy 到 48.2%；SWE-bench Verified 从 2.7% 提到 27.8%。消融显示 replay 必须域外；summary 放在 think 块内降到 23.4%（开放）/33.9%（闭源），不如放外面；保留可见文本会明显损害 Action-only 和 CoT-proxy。

最值得记住：策略可蒸馏，思维链不必模仿；用空推理块训练、推理时开启思考，学生用自己的推理执行教师策略，短 CoT-proxy 再额外补强。
