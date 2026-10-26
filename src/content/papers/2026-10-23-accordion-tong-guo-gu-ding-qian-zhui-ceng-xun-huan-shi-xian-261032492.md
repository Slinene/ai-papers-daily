---
title: 'Accordion: Elastic-Depth Inference via Fixed-Prefix Layer Looping'
title_zh: Accordion：通过固定前缀层循环实现弹性深度推理
authors:
- Yudong Zhang
- Wei Ding
- Kaili Zheng
- Yuchen Ding
- Zhenyu Zhang
affiliations:
- Tsinghua University
- Baidu Inc.
arxiv_id: '2610.32492'
url: https://arxiv.org/abs/2610.32492
pdf_url: https://arxiv.org/pdf/2610.32492
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: LLM 弹性深度推理 · 固定前缀层循环
tags:
- Looped Transformers
- MoE
- Elastic Inference
- Pretraining
- SFT
- RL
one_liner: 一个 MoE 模型通过固定前缀层循环支持五个推理预算，中间预算以约 21-24% 额外时间捕获 89% 深度增益
practical_value: '- 需要线上不同 latency/cost 档位时，可训练一个模型支持多个推理预算，通过固定前缀层循环共享权重，避免维护多个模型；推理时按请求选择预算，FLOPs
  和 KV cache 线性扩展。

  - 训练时每个 micro-batch 均匀采样一个预算路径，只优化该路径 NTP，无需跨预算一致性损失；第二遍用 zero-initialized tanh
  gates，初始为恒等映射，训练稳定。预算无关参数优于 budget-conditioned 参数。

  - 多领域能力整合可采用参数组加权合并专家，再做 budget-matched 多教师在线蒸馏（MOPD），能保留各预算增益并提升整体指令遵循，适合搜索推荐中的
  Agent 多任务模型合并。

  - 资源敏感场景优先选中间预算（如 k=6）：以约 21-24% 额外 TPOT 捕获约 89% 深度增益，推荐系统在线服务可按此设计弹性档位。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
LLM 应用需要不同推理预算，但为每个预算单独训练维护模型成本高。循环 Transformer 支持弹性推理，但联合训练多深度可能损害浅层性能（one-loop tax），且弹性能力需贯穿 SFT/RL 整个训练管线。

## 方法关键点
- 架构：24 层 MoE（总 6.03B，活跃 0.54B，128 routed experts / 8 active），选择窗口 layers 7–18，五个预算 k∈{0,3,6,9,12}，重复前 k 层，层执行数 24–36。第二遍通过 zero-initialized tanh gates 加到残差，共享权重和 router，pass-specific MoE balancing。
- 训练：每个 micro-batch 均匀采样一个预算，只优化该路径 NTP 损失，无额外一致性损失。设计实验证明固定前缀层选择优于随机/center/suffix 等 8 种策略；五预算优于三/四预算；共享 router 优于分离；预算无关参数优于 budget-conditioned。
- 后训练：SFT 继续五预算联合训练；RL 训练 IF/math/code 三个专家，用 GRPO/DAPO，通过参数组加权合并初始化学生，再做 budget-matched 多教师在线蒸馏（MOPD）。

## 关键结果
- 1.61B/80B tokens 设计实验：与独立 specialists 同 token 下 loss 差距 <0.003 nats；同 FLOPs 下大预算超过 specialist 0.0068 nats。
- 主模型 3.6T tokens 预训练：k=0→k=12 五类 macro-average 提升 3.01 pp（47.05→50.06），36/37 任务提升；k=6 捕获 89% 增益，TPOT 增加约 21-24%；32K 长上下文 RULER 增益 5.47 pp（4K 仅 0.72 pp）。
- 后训练：Accordion-RL 在 IFEval 上比最强公开参考高 16.64 pp，超过每个领域专家对应域平均，数学/代码保留深度增益。

**最值得记住的一句话**：一个 MoE 模型通过固定前缀层循环支持五个推理预算，中间预算以约 21-24% 额外时间捕获 89% 的深度增益，并可贯穿预训练到 RL。
