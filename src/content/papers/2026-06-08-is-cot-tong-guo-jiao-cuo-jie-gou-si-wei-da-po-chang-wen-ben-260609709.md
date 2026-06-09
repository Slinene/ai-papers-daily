---
title: 'IS-CoT: Breaking the Long-form Generation Collapse via Interleaved Structural
  Thinking'
title_zh: IS-CoT：通过交错结构思维打破长文本生成崩溃
authors:
- Zechen Sun
- Yuyang Sun
- Zecheng Tang
- Juntao Li
- Wenpeng Hu
- Wenliang Chen
- Zhunchen Luo
- Guotong Geng
- Min Zhang
affiliations:
- Soochow University
- PLA Academy of Military Science
arxiv_id: '2606.09709'
url: https://arxiv.org/abs/2606.09709
pdf_url: https://arxiv.org/pdf/2606.09709
published: '2026-06-08'
collected: '2026-06-09'
category: LLM
direction: 长文本生成 · 动态规划与反思
tags:
- Long-Form Generation
- Chain-of-Thought
- Dynamic Planning
- Reflection
- Length Control
- SFT
one_liner: 提出交错式Plan-Write-Reflect循环，让8B模型在长文本生成上超越大模型，打破长度崩溃。
practical_value: '- 在生成长文本（如商品详情、营销软文）时，可采用 Plan-Write-Reflect 循环：每写一段后反思当前进度并调整后续计划，避免偏离主题或长度失控。

  - 对于多步对话 Agent（如导购助手），可借鉴全局大纲+局部规划+反思的结构，让模型在长对话中维持目标一致性，防止上下文遗忘。

  - 训练时保留完整的推理链（计划、反思 token），通过 SFT 直接让模型学习动态规划，小模型也能获得强长度控制与连贯性，适合低资源业务定制。

  - 多教师蒸馏的设计可提升数据多样性，避免生成风格单一，对构建特定领域（如电商）的高质量“带思考过程”数据集有直接参考价值。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：
LLM 在生成长文本（>2000 words）时会出现严重的长度和内容质量崩塌——既达不到目标字数，也丧失连贯性。现有模型多在生成前做一次性静态规划，随着篇幅增加，初始规划的引导力急剧衰减。作者希望引入动态交错的规划-写作-反思循环，让模型在生成过程中持续自我调整。

**方法关键点**：
- **IS-CoT 框架**：在生成过程中嵌入 `<global_plan>` → `<step_plan>` → `<content>` → `<reflection>` 的循环，每一步都重新对齐全局目标。
- **三阶段数据合成**：(1) 指令精炼：平衡中英文，为无长度约束的 prompt 补充长度要求；(2) 交错结构合成：双教师（DeepSeek-V3.2、Qwen3-235B）蒸馏生成带完整推理轨迹的长文，通过启发式控制保证格式和长度合规；(3) 质量过滤：采用长度得分 Sl>90 + LLM 评判 + 人工核验，得到约5000条高质量样本。
- **训练**：基于 Qwen3-8B 做 SFT，不剥离中间推理 token，学习整个 Plan-Write-Reflect 序列。

**关键实验**：
- 在 LongBench-Write 上，IS-Writer-8B 平均分 88.25，比 DeepSeek-V3.2（671B）高 +3.08，比 Gemini-2.5-Flash 高 +4.58；在超长区间 [4k,20k] 长度得分 86.75，远超其他模型（如 DeepSeek-V3.2 仅 53.22）。
- 在 WritingBench 上与 DeepSeek-V3.2 打平（8.60），在金融和政治领域达到最优。
- 消融表明去除反思或交错规划会使增益大幅下降（+2.45 和 +0.55），验证了组件必要性。

**值得记住的一句话**：*有效的长文本生成需要不断更新的规划与反思，而不是一次性静态蓝图——这正是 IS-CoT 用 Plan-Write-Reflect 循环打破长度崩溃的核心思想。*
