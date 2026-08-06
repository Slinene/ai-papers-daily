---
title: 'When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation'
title_zh: 当教师误导时：感知虚假信号的在线策略蒸馏
authors:
- Yinuo Jiang
- Yongjie Ye
- Zhou Tao
- Xiang Zhuang
- Qiang Zhang
- Huajun Chen
- Tiankai Li
affiliations:
- Zhejiang University
- ByteDance
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.03632'
url: https://arxiv.org/abs/2608.03632
pdf_url: https://arxiv.org/pdf/2608.03632
published: '2026-08-03'
collected: '2026-08-06'
category: Training
direction: 在线策略蒸馏 · 虚假信号过滤
tags:
- On-Policy Distillation
- Spurious Signals
- Input-Groundedness
- Token-level Filtering
- LLM-VLM Training
one_liner: 提出 SA-OPD，通过过滤教师信号中输入无关的虚假成分，提升在线策略蒸馏的可靠性与效果。
practical_value: '- **蒸馏偏差诊断**：在推荐/Agent 的序列生成蒸馏中，可借鉴“移除 prompt 后教师信号变化”的探测法，判断教师是否依赖输入无关的语言先验、流行度或格式模板，而非用户/上下文真实需求。

  - **选择性掩码策略**：通过组合低输入接地性 + 高教师-学生分歧两个条件，精准滤除高冲击虚假更新，保留输入相关监督；推荐场景可类似过滤由标题党、模板短语引入的梯度噪声。

  - **动态阈值控制**：自适应调节过滤比例（约束 FLMR），防止过度丢弃有用信号，适合在训练过程不平稳的视觉或复杂 Agent 交互场景中使用。

  - **工程实现轻量**：无需额外网络参数，仅增加一次无 prompt 的 log-prob 评估，易于集成到现有 On-Policy 蒸馏流水线中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
在线策略蒸馏（OPD）通过师生分布匹配传递能力，但教师本身的语言先验、格式偏好或推理模板可能产生与特定输入无关的虚假监督信号。这些信号梯度能量大，却缺乏任务改进方向，导致学生继承教师的输入无关偏差，且传统选择标准（熵、分歧度、可学性）无法识别此类信号。

**方法关键点**  
- **输入接地性代理**：对每条 student 生成轨迹，计算原始 prompt 与移除 prompt 后教师-学生对 token 分歧的差异（`Input-Grounding Gap`）。若差异小，则信号由通用先验主导而非输入驱动。  
- **双条件过滤**：只滤除既具备低输入接地性、又具有高绝对教师-学生分歧的 token（`Bottomp1(∆IG) ∩ Topp2(|Afull|)`），移除高冲击虚假更新。  
- **动态损失质量约束**：自适应调节过滤比例，使被滤除的损失质量占比不超过阈值 β，防止移除过多有效视觉监督或推理信号。  
- **无需外部标签**：仅用无 prompt 下的师生评分即可构建过滤掩码，不引入额外可训练参数。

**关键实验与结果**  
- 在 Qwen3/Qwen3.5 系列的 VLM 蒸馏（视觉理解与推理）和 LLM 数学推理蒸馏上评估。  
- VLM 任务：SA-OPD 较 Vanilla OPD 平均提升 3.1‑3.5 分（视觉推理从 60.4→63.5，视觉理解从 50.5→54.0），且优于 TIP、FiRe-OPD 等选择性方法。  
- LLM 数学推理：Math500 提升 3.0 点，平均分从 28.5→30.4，超越所有基线。  
- 分析显示 VLM 蒸馏中虚假信号持续存在；被过滤 token 中 69.9% 为内容词，但多为上下文可预测的重复模式。  
- 动态阈值在 CountQA 上带来 +2.8 额外增益。

**核心洞见**  
输入接地性是 OPD 监督选择的关键维度；滤除高冲击但弱接地的教师信号可以显著提高蒸馏信噪比，且在大模型视觉理解这类短时波动任务中收益尤为明显。
