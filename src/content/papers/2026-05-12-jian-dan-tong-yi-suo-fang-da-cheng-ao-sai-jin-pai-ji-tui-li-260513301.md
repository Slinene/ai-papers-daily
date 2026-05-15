---
title: Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling
title_zh: 简单统一缩放达成奥赛金牌级推理
authors:
- Yafu Li
- Runzhe Zhan
- Haoran Zhang
- Shunkai Zhang
- Yizhuo Li
- Zhilin Wang
- Jiacheng Chen
- Futing Wang
- Xuyang Hu
- Yuchen Fan
affiliations:
- 上海人工智能实验室
- 香港中文大学
- 清华大学
- 上海交通大学
- 北京大学
arxiv_id: '2605.13301'
url: https://arxiv.org/abs/2605.13301
pdf_url: https://arxiv.org/pdf/2605.13301
published: '2026-05-12'
collected: '2026-05-15'
category: Reasoning
tags:
- LLM
- Reinforcement Learning
- Reasoning
- Olympiad
- MoE
- Test-time Scaling
one_liner: 一套 SFT-RL-TTS 统一流程将 30B-A3B 模型推向数学与物理奥赛金牌水平，并展现跨领域科学推理迁移
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**
奥赛数学与物理问题要求严格的证明搜索、自验证和长程推理，但现有模型常止步于答案正确而缺乏证明严谨性。如何用紧凑的30B-A3B模型获得金牌级奥赛实力？

**方法关键点**
- **逆向困惑度课程SFT**：从P1-30B-A3B起始，用338K条≤8K token的轨迹（含数学、科学、代码、指令跟随）进行SFT，数据按自身策略困惑度从高到低排序，先学不熟悉的证明模式，有效重塑推理行为而不丢失原有能力。
- **粗粒度RL（RLVR）**：在约9K可验证题目上使用GSPO进行序列级优化，结合分层奖励（规则校验→Math-Verify→gpt-oss-120b），提升答案搜索能力。
- **精细RL**：引入DeepSeekMath-V2作为生成式证明奖励，评价完整证明质量；加入自精炼机制（将低质量回滚转为修复提示）和经验回放（保存并重放稀有成功证明），强化证明严谨性与鲁棒性。
- **测试时缩放（TTS）**：在推理时执行自验证-自精炼循环：模型生成初解→自检漏洞并生成修要报告→判断接受或回退精炼，直至连续5次通过验证。

**关键结果**
- 可验证基准：SU-01在AnswerBench/AMO-Bench/AIME 25/26/FrontierScience-Olympiad综合得分77.3%，匹配同尺寸最强Qwen3.6-35B-A3B（77.4%）。
- 证明基准：IMO-ProofBench直接57.6%，TTS后70.2%（Basic 91.0%，Advanced 49.5%），大幅领先其他同尺寸模型并接近Gemini 3.1 Pro Thinking（72.6%）。
- 竞赛成绩：IPhO 2024/2025直接超越金牌线（23.5/20.3 vs 20.8/19.7），IMO 2025 TTS后35分（金牌线），USAMO 2026 TTS后35分（超金牌线10分），匹敌该届人类最高分。
- 推理长度：TTS下初始解中位数106K token，精炼83K token，验证28.7K token，模型可持续连贯推理超100K token。
- 跨域迁移：FrontierScience-Research综合11.7%为同尺寸最佳，展现出数学/物理训练外的科研推理能力。

一句话：紧凑的统一训练+测试时缩放流程赋予30B模型专家级奥赛证明能力，且不牺牲科学泛化性。
