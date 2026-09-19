---
title: 'When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation'
title_zh: 当 EOS Token 不一致：理解 On-Policy 蒸馏中的长度膨胀
authors:
- Yuxiao Yang
- Tianrun Yu
- Shangzhe Li
- Kaixiang Zhao
- Xuchao Zhang
- Chetan Bansal
- Huaxiu Yao
- Taylor W. Killian
- Weitong Zhang
affiliations:
- University of North Carolina at Chapel Hill
- Brigham Young University
- Microsoft
arxiv_id: '2609.20511'
url: https://arxiv.org/abs/2609.20511
pdf_url: https://arxiv.org/pdf/2609.20511
published: '2026-09-16'
collected: '2026-09-19'
category: Training
direction: On-policy 蒸馏终止 token 失配
tags:
- on-policy distillation
- EOS mismatch
- length inflation
- LLM training
- semantic EOS
- special tokens
one_liner: 发现 base 学生与 post-trained 教师的终止 token 失配是 OPD 长度膨胀主因，语义 EOS 聚合对齐终止概率可有效缓解
practical_value: '- 在电商/推荐/Agent 场景用小模型蒸馏大模型生成推荐理由、query 改写或对话回复时，务必检查学生和教师模型的 EOS
  token 配置及实际概率分布；即使声明停止集相同，也可能分别偏好 `<eos>` 与 `<end_of_turn>`，导致生成不停止、重复输出。

  - 修复不能只改 decoding 的 stopping set，要在训练目标层把语义等价的终止 token 概率求和，作为同一个 `stop` 动作进行监督（semantic
  EOS aggregation）；否则学生已有的停止动作会被负梯度持续压制，且教师偏好的 token 因采样概率极低几乎得不到直接监督。

  - OPD 训练中应监控 response length、clipping ratio、termination probability 三条曲线；若正确答案早已出现但长度继续增长、终止概率骤降，优先怀疑
  EOS 失配，而不是先调学习率或换 KL 目标。

  - 多轮 Agent 或工具调用场景不要盲目聚合所有特殊 token：需定义 context-dependent termination classes，区分
  end-of-turn、tool call、document boundary、message completion，否则会破坏交互控制流。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
On-policy distillation（OPD）用小模型自身 rollout 从大模型获得逐 token 监督，是高效迁移 post-trained 能力的方法。但多个模型家族都出现学生回复长度持续膨胀、甚至耗尽生成预算的问题，且正确答案往往早已出现，后续是重复或冗余内容。已有工作从 reverse-KL 目标、rollout 质量退化等角度解释，但本文发现一个更底层、可诊断的原因：base 学生与 post-trained 教师的**终止 token 失配**。

## 方法关键点
- 采样 token OPD 中，学生采样的 token 才会被教师打分。若学生采样的 EOS token 正是教师不偏好、但语义等价的另一个终止 token，学生会收到负监督，自身的停止动作被持续压制。
- 在 Qwen3 中，base 学生偏好 `<|endoftext|>`，post-trained 教师偏好 `<|im_end|>`；学生对教师偏好 token 的概率约 1e-11，几乎无法被采样，导致教师偏好的终止形式难以迁移。
- 系统比较四种修正：① shared-set decoding 仅扩展解码停止集；② teacher-side EOS mapping 将教师所有终止 token 概率映射到学生原生 EOS；③ **semantic EOS class** 将终止等价 token 聚合为单一 `stop` 动作，用总停止概率监督；④ canonical single-EOS action space 进一步约束学生动作空间。
- 在 Llama 3.2 和 Gemma 3 上验证；Gemma 3 的 PT/IT 声明同一 EOS 集合，但实际概率分别偏向 `<eos>` 和 `<end_of_turn>`，说明失配不限于声明集差异。
- 用 K2-Horizon 的 pretrain/mid/SFT/final 检查点作为学生初始化，固定 final 为教师，观察终止偏好随训练阶段的演变。

## 关键结果
- Qwen3 vanilla OPD 长度上升并频繁达到 7,168 token 预算；学生原生 EOS 概率从约 0.8 降至接近 0。
- Fix1（仅解码层对齐）与 vanilla 几乎一致失败；Fix2/3/4 在概率层对齐后，长度和 clipping ratio 显著靠近教师参考，终止概率不再崩溃。
- 跨模型家族：semantic EOS 修正在 Qwen3、Llama 3.2、Gemma 3 上均大幅缓解长度膨胀，但恢复动态不同，Llama 3.2 残余 gap 较大。
- K2-Horizon Pretrain-to-Final 显示，即使教师偏好终止 token 已迁移，晚期仍出现长度再膨胀和终止概率崩溃，semantic correction 下也保留此现象，说明 EOS 失配不是唯一机制。
- 模板和 grader 敏感：DAPO 训练用 TTRL 评估长度更低；原始 DAPO grader 把 Qwen3-4B teacher 评为 6.28% Avg@16，扩展解析后为 24.34%，提示 OPD 评估需同步适配格式。

## 最值得记住的一句话
在 on-policy distillation 中，仅对齐解码停止集远远不够，必须在训练目标层把语义等价的终止 token 聚合为同一个 `stop` 动作进行概率监督，否则学生的停止概率会被持续压制，长度膨胀几乎必然发生。
