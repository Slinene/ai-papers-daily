---
title: 'Intern-Decision: Efficient Multimodal Decision Making with Autoregressive
  Masked Language Modeling'
title_zh: Intern-Decision：自回归掩码语言建模的高效多模态决策模型
authors:
- Tong Zhu
- Zhe Xu
- Zefeng He
- Yunkai Chai
- Xuyang Hu
- Dehong Zheng
- Yun Luo
- Yafu Li
- Qi Zhang
- Yu Cheng
affiliations:
- Shanghai AI Lab
- Shanghai Jiao Tong University
- Fudan University
- Nanyang Technological University
arxiv_id: '2610.22131'
url: https://arxiv.org/abs/2610.22131
pdf_url: https://arxiv.org/pdf/2610.22131
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 结构化决策 · 多模态小模型
tags:
- Autoregressive Masked Language Modeling
- Multimodal Decision
- Structured Output
- Calibration
- Agent Systems
- Efficient Inference
one_liner: 用单次前向的自回归掩码决策替代自由文本生成，输出结构化选择与候选概率，4B模型七套评测集平均准确率90.02%
practical_value: '- 用“掩码决策字段 + 单次前向”替代 free-form JSON 生成或逐字段循环打分，适合电商/广告中高频闭集判断：意图分类、tool
  routing、风控/安全审核、多字段表单决策等。

  - 保留 Qwen 等 causal backbone 与 native LM head，在 assistant skeleton 的 `<decision>`
  占位符前一个 token 读 logits，对 legal options 做 softmax 得到候选概率；无需额外分类头或逐字段前向，且多字段共享 state，减少重复
  prefill。

  - 对概率输出做 post-hoc temperature scaling 能显著改善 Brier / ECE；可用小模型置信度阈值触发大模型接管，适合难例路由、广告审核升级、搜索结果重排等场景，在精度和成本之间选操作点。

  - 多模态输入（文本+可选图像）输出离散动作，适合 GUI Agent、商品图审核、直播画面判断等“看截图→做选择”的闭环任务；训练时冻结 vision tower
  可低成本复用预训练视觉能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
Agent 系统中大量底层操作本质是闭集决策，如工具选择、模型路由、动作执行。现有 LLM 仍用自由文本生成处理这些结构化判断，带来额外解码延迟和模型与下游控制器的接口复杂度。需要一个能直接输出结构化结果与可靠置信度的小型决策模块。

**方法关键点**  
- 把结构化决策建模为在预设 assistant JSON skeleton 中每个字段放一个 `<decision>` 掩码的 next-token 预测。  
- 输入包含 state、可选 images、有序问题与候选选项；训练时 ground-truth 答案符号只出现在监督张量中，推理时对每个 decision marker 前一个位置的 logits 用原生 LM head 读取，所有字段共享同一次因果前向。  
- 候选概率通过对 legal option logits 做带温度 $T$ 的 softmax 得到；支持 choice / score / noul 类型，输出结构化标签和候选概率。  
- 基于 Qwen3.5 0.8B/2B/4B 初始化，冻结视觉塔和投影层，只用 17,880 条样本（23,500 个决策，其中 5,500 张图片）训练 2 epochs；另用独立校准集拟合温度缩放。

**关键实验**  
- 七个评测集非加权平均准确率：4B 达到 90.02%，超过 Jev 的 88.74%；在 Jevbench Easy/Original/Hard 上分别为 48/48、71/72、82/111；Typed Decision 为 80.55%，ToolACE 为 96.45%。  
- 固定 289 token 三字段请求在单张 RTX 4090 上，4B 平均延迟 44.16ms，0.8B/2B 约 33–34ms。  
- 96 例已知分布校准实验中，temperature scaling 将 expected multiclass Brier 从 0.628 降到 0.550，ECE 从 0.213 降到 0.089。  
- 置信度路由研究：111 道 Jevbench-Hard 中路由 42 题给大模型 Atria-Dawn-Preview，整体准确率从 73.87% 提升到 87.39%，估计耗时比大模型单独处理少约 53%。

**最值得记住的一句话**  
闭集决策可以压缩为“多字段 mask + 单 forward + legal-option softmax”，并配合温度校准与置信度升级路由，得到低延迟、结构化、概率化且可审计的 Agent 决策单元。
