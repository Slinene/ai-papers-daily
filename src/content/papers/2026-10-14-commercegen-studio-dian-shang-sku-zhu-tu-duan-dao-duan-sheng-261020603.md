---
title: 'CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image
  Generation'
title_zh: CommerceGen-Studio：电商 SKU 主图端到端生成框架
authors:
- Xiaoli Xu
- Zhengtao Wu
- Zhengze Xu
- Tao Liu
- Yongchao Du
- Zuan Gao
- Xingjian Wang
- Hao Yan
- Mengting Chen
- Wei Li
affiliations:
- Alibaba Group
- Taobao App
- AI-Native Applications Group
arxiv_id: '2610.20603'
url: https://arxiv.org/abs/2610.20603
pdf_url: https://arxiv.org/pdf/2610.20603
published: '2026-10-14'
collected: '2026-10-15'
category: Multimodal
direction: 多模态电商主图生成 · Agent+RL+蒸馏
tags:
- e-commerce image generation
- Diffusion Transformer
- RLHF
- distillation
- multi-condition generation
- VLM agent
one_liner: 三段式 SKU 主图生成框架：PERL-Agent 提炼卖点、Layout Thinker 优化布局、SKU-DiT 多条件保真生成，已支撑每日百万级生产
practical_value: '- **PERL-Agent 的闭环提炼模式可直接迁移到电商文案/标题/搜索词生成**：用 VLM+LLM 四角色（生成-评判-归因-改写）处理多源元数据冲突，六维
  reference-free rubric 优化最差维度而非均值，支持按失败维度单点修改 prompt 并回滚到历史好版本。业务上可避免按类目写规则，也能定位
  bad case 根因。

  - **Layout Thinker Optimization 的做法值得 Agent 系统借鉴**：在结构化 TextList 和最终生成器之间插入显式布局改写层，SFT
  后做双域 GRPO——文本奖励直接评 caption，图像奖励冻结下游 SKU-DiT 渲染后评图，每次只激活一个奖励域避免梯度冲突。这样能缩小上游语义和下游生成之间的
  gap，而不是让生成器自己隐式规划。

  - **RDR 训练策略对模型加速很有参考价值**：先 RL 对齐偏好，再用 DMD2 变体做少步蒸馏（靠近干净端点随机停止、商标域 3:1 混合、对抗训练），最后对少步学生再做一轮
  RL 恢复高频细节。注意 RL 阶段用 LoRA 限制更新范围，防止奖励优化把底座能力带偏。

  - **多条件输入设计可复用于电商 AIGC 管线**：白底商品图 + 商标 crop + 结构化布局 caption 联合输入，把主体保真、logo 完整性、文字准确度显式拆成条件，并在
  reward 中加入 OCR penalty，比单一 prompt 更能满足可发布要求。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

## 动机
电商搜索从 item 粒度细化到 SKU 粒度后，商家普遍缺乏 SKU 级主图，直接投放白底商品图会拉低点击率。通用文生图/图生图模型无法处理 SKU 元数据多源冲突、信息一致性、长尾品类鲁棒性和多条件布局控制，因此需要一套能落地的端到端商业级主图生成系统。

## 方法关键点
- **PERL-Agent**：把异构 SKU 信息（item/SKU OCR、属性、标题、类目）提炼成卖点文本列表。四个角色组成闭环：Generator 生成候选，Judge 用六维 reference-free rubric 打分，Analyzer 定位最差维度，Refiner 对 prompt 做单点 diff 更新。优化目标是最差维度而非均值，最多 10 轮，支持失败归因和回滚。
- **Layout Thinker Optimization (LTO)**：在 TextList 与生成器之间插入 VLM 布局改写器，输出布局 caption 决定商品位置、背景、文字层级、logo 位置等。SFT 后做双域 GRPO：文本奖励直接评 caption，图像奖励冻结 SKU-DiT 渲染后评图，每次只激活一个奖励域避免梯度冲突。
- **SKU-DiT 与 RDR 渐进训练**：基于 Swift-Image 6B 多图编辑 DiT。阶段一 SKU 垂直域继续训练；阶段二先 DiffusionNFT 训练 complex-layout 和 subject-preservation 两个专家，再用 DiffusionOPD 在线蒸馏到学生；随后 Dynamic Backward Simulation Distillation 把采样步数降到少步，最后对少步学生再跑一轮 RL 恢复文字和主体高频细节。RL 用 LoRA 限制更新，防止偏离底座。
- **数据规模**：阶段一约 4M T2I、2.67M 单图 I2I、274K 多图 I2I；LTO SFT 20K、RFT 5K；RDR RL 轨迹 5K/2.5K、蒸馏混合数据 200K。

## 关键实验
CommerceGen-Bench 是 400 个线上 hard cases，覆盖 6 大类 15 子类，按 PF/IF/PI/ND/AD 五维由多模态 judge 打分。无 prompt enhancement 时，Ours 6B overall 单图 9.40、多图 9.44，超过所有开源 baseline，尤其在 Instruction Following 上大幅领先；有 prompt enhancement 时仍保持稳定。Ablation 显示：VLM base + SKU-DiT 50 步仅 6.509，逐步加入 SFT、RDR、LTO 后达到 8 步采样下 9.440。系统已生产部署，每日生成百万张主图，单图延迟几秒。

## 最值得记住的一句话
真正难的不是生成一张好看的图，而是让每一张图都能直接发布：先把信息抽取、布局规划、生成保真各自显式化，再用 RL-蒸馏-RL 在推理约束下保住文字精度与主体保真。
