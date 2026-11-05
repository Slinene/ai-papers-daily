---
title: 'EvoGuard: Mitigating Degradation in Online Skill Evolution'
title_zh: EvoGuard：缓解在线技能演化退化
authors:
- Yanli Wang
- Zichen Bai
- Tianyue Jiang
- Kunming Shao
- Junhao Shi
- Xueqin Liu
- Jinguo Sun
- Muye Li
- Tingting Bi
- Yanlin Wang
affiliations:
- JD.Com
- Sun Yat-sen University
- The University of Melbourne
- The Hong Kong University of Science and Technology
arxiv_id: '2611.06444'
url: https://arxiv.org/abs/2611.06444
pdf_url: https://arxiv.org/pdf/2611.06444
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 技能在线更新 · 接受/拒绝选择器
tags:
- Agent Skills
- Pairwise Preference
- LoRA
- Skill Evolution
- Position Bias
- Online Learning
one_liner: 提出 pairwise 技能选择器，用离线效用标注训练，部署时单次前向判断是否接受单轨迹改写，避免技能退化
practical_value: '- 在电商/Agent 生产中维护「任务族 → 技能/指令文档」时，可加一个 LoRA cross-encoder 做 pairwise
  接受/拒绝；每次只比较 A/B 两个标签 token 的 logits，无 rollout，延迟低，能防止 prompt 漂移。

  - 构造训练对时用私有测试集给技能打分，并 rejection sampling 只保留效用差≥δ 的 pair；同时混合 base generator 与 expert/RL
  generator 的技能，提升选择性信号。

  - 交换 A/B 位置训练 Bradley-Terry logits 目标，位置一致性可从 55.6% 提升到 98.3%；线上随机放候选减少位置偏差。

  - selector 对未见 executor 可迁移，适合后端执行模型升级时复用；可先把任务按意图/品类分族，每族维护一个技能文档。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
单轨迹改写技能文档时，约42%的改写会降低私有测试集上的成功率；每次更新都做held-out验证又太贵。在线技能演化需要廉价可靠的接受/拒绝机制。

### 方法关键点
- 每个任务族维护一个SKILL.md；每次任务后用冻结generator基于当前技能、轨迹和结果改写。
- 离线用base generator与expert generator构建技能池，在私有测试集上估计效用。
- 用rejection sampling保留同族且效用差≥δ的pair，训练pairwise selector（Qwen3-4B+LoRA），只对A/B两个label token的logits做Bradley-Terry偏好损失。
- 部署时selector一次forward pass比较当前技能与新技能，不生成token，不跑额外rollout；executor/generator/selector全冻结。

### 关键实验
- ALFWorld上平均成功率56.5%，Accept-All为45.5%，No-Skill为36.7%；对未见executor Qwen3-32B仍达69.2% vs 54.9%。
- selector在未见skill pair上准确率95.0%，parent-child准确率86.3%；位置一致性98.3% vs untrained LLM-Judge 55.6%。
- ScienceWorld成功10.2%→15.3%；LiveCodeBench达到28.4% pass rate。
- 去除expert pool或rejection sampling，平均成功率下降>4%。

**一句话**：把技能更新做成pairwise preference，用离线效用标注+rejection sampling训练轻量selector，是廉价且可迁移的在线技能守卫。
