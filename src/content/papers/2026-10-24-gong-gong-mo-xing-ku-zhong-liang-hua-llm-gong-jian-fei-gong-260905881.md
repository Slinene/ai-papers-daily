---
title: 'Broken on Arrival: Non-Functional Quantized LLM Artifacts in Public Model
  Registries and How to Catch Them'
title_zh: 公共模型库中量化 LLM 工件非功能性失效及其检测
authors:
- Aditi Patodiya
affiliations:
- Independent Researcher
arxiv_id: '2609.05881'
url: https://arxiv.org/abs/2609.05881
pdf_url: https://arxiv.org/pdf/2609.05881
published: '2026-10-24'
collected: '2026-10-31'
category: LLM
direction: LLM 量化模型验收与发布测试
tags:
- quantization
- GGUF
- model registry
- acceptance testing
- LLM deployment
one_liner: 审计 Ollama 与 Hugging Face 量化模型发现 2.3% 低比特小模型功能失效，并证明校准可修复
practical_value: '- 发布内部量化/蒸馏模型到模型库或线上前，构建轻量功能 smoke test（如代码生成 15-50 条业务相关 prompts）拦截“看似正常但输出失效”的模型，尤其对
  2-4bit 小模型。

  - 量化配方要作为模型元数据记录并在发布前验证：是否使用 importance matrix/calibration 数据；对低比特小模型优先做校准，论文中 Qwen2.5-Coder-3B
  从 0 提升到 76-113/164，说明校准是关键开关。

  - 模型验收不能只校验 hash/张量一致性；该研究显示 registry 文件与原权重张量完全一致但仍功能失效，需在目标推理栈上跑端到端任务，而非只做格式或数值对比。

  - 对线上 Agent/推荐 LLM，建议建立“模型健康度回归集”，按量化级别和参数规模分层采样测试；低比特（≤4B 参数）模型发布应强制功能测试，避免上线即不可用。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：开发者从公共 registry 下载量化 LLM 本地运行，但 Ollama 与 Hugging Face 页面和文件元数据均未记录功能测试，量化转换后模型是否保持功能未知。

**方法**：审计 Ollama 官方库 15 个模型线全部 305 个 code-capable GGUF tags 及 22 个流行的 Hugging Face 社区文件；先以 15 个代码任务做筛查，可疑对象再在全部 164 个 HumanEval+ 任务上重测。重建 5 个可疑文件并与 registry 文件逐张量对比，进一步验证 importance matrix 校准的影响。

**关键结果**：7 个官方 tag（2.3%）最多只能解决 6/164 个任务，全部是低比特量化且参数不超过 4B 的模型。5 个重建文件与 registry 文件张量完全一致，说明文件未损坏；但精确复现不等于功能正常。固定权重、工具链和张量混合不变，加入 importance matrix 后 Qwen2.5-Coder-3B 在三个量化级别从 0 提升到 76-113/164；而同一未校准配方对更小的 Qwen2.5-Coder-1.5B 仍有效，表明配方本身不能预测失败。66 个通过筛查的采样 tag 无一出现非功能问题。研究发布了审计数据和 quantcheck 工具，建议发布前筛查低比特 tag，校准或不予发布。
