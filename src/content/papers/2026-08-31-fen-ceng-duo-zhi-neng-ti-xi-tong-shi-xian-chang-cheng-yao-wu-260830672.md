---
title: 'HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote
  Sensing Task Solving'
title_zh: 分层多智能体系统实现长程遥感任务可靠求解
authors:
- Boyang Mu
- Zhiwei Wei
- Mugen Peng
- Wenjia Xu
affiliations:
- Beijing University of Posts and Telecommunications
- Hunan Normal University
arxiv_id: '2608.30672'
url: https://arxiv.org/abs/2608.30672
pdf_url: https://arxiv.org/pdf/2608.30672
published: '2026-08-31'
collected: '2026-09-07'
category: MultiAgent
direction: 多智能体分层协作与强化学习优化
tags:
- MultiAgent
- Hierarchical RL
- Tool Use
- Remote Sensing
- Verification
- SFT
one_liner: 提出 Manager-Specialist 分层多智能体架构，通过步骤级验证和分层强化学习大幅提升小模型长程工具调用与任务成功率
practical_value: '- 复杂长链路业务（选品→人群定向→素材生成→投放→复盘）可借鉴 Manager-Specialist 分层：Manager 负责全局规划、步骤级验证和失败重规划；Specialist
  按业务阶段分组工具（如召回/排序/出价），减少跨域工具混淆。

  - 在中间产出设置 schema/一致性/约束检查，维护结构化中间状态，支持 fail 重试、uncertain 交叉验证，避免错误在长链路中传播；这对广告投放、推荐策略生成等容易因上游错误导致下游失效的场景尤其有用。

  - 训练技巧可复用：两阶段 SFT 先注入领域知识再做 workflow 对齐，能低成本提升小模型业务能力；强化学习时对工具调用按 tier 给分（幻觉工具 -1，域内错误工具
  -0.5，正确工具 0.5+执行分），比只奖励最终成功提供更稠密训练信号；Manager/Specialist 分开计算 advantage 后合并 loss，共享
  backbone + LoRA 减少部署成本。

  - 在小模型上通过结构化层次和验证控制即可接近大模型效果，业务资源受限时不必盲目上大参数量模型。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
遥感任务正从单步感知走向长程复杂工作流，但现有单体智能体框架存在三类 mismatch：workflow mismatch（不建模阶段依赖）、knowledge mismatch（缺乏 RS 领域知识）、control mismatch（缺少中间验证与恢复），导致错误跨阶段传播。长程 RS 任务本质是多阶段依赖，中间结果质量直接决定最终成败，因此需要显式建模工作流结构、领域约束和步骤级控制。

### 方法关键点
- **分层架构**：Manager Layer 由单个 Orchestrator Agent (OA) 负责全局规划、路由、记忆和验证；Specialist Layer 按遥感处理链光谱解析→物理反演→统计分析分为 SPA、PRA、SAA 三个专家智能体，工具按阶段分组，减少跨域混淆。
- **步骤级验证与自适应控制**：OA 维护结构化全局记忆 H_t，验证返回 pass/uncertain/fail；fail 触发 replan/repair，uncertain 触发交叉验证，pass 提交记忆，形成历史感知闭环。
- **两阶段 SFT（Expert-tuning）**：Stage I 注入 RS 知识（3 级 taxonomy，1583 chunks，5687 样本）；Stage II 对齐工作流（684 workflow MCQ + 309 workflow order）。
- **VG-HRL 分层强化学习**：Manager 使用轨迹级奖励（route/final/len）；Specialist 使用分级门控奖励：tier1 幻觉工具 -1.0，tier2 域内错误工具 -0.5+0.2R_exec，tier3 正确工具 0.5+0.2R_exec+0.3R_args；按 task 和 (task, step index) 分别分组计算 advantage，混合 loss λ=0.5，共享 backbone + LoRA，GRPO group size=4。

### 关键结果
- Earth-Bench：Qwen3-4B Accuracy 从 15.73/10.08 提升至 43.95/45.56，Tool-Exact-Match 从 0.00/8.63 提升至 31.67/34.64；Qwen3-8B Accuracy 达 48.39/53.62。
- ThinkGeo：Qwen3-4B Inst./Tool./Arg. 从 18.35/8.54/1.24 提升至 73.73/47.87/8.51，Ans. 从 6.07/7.79 提升至 11.28/13.77；其中 Ans. 为所有对比方法最佳。
- 领域适配：RS-EXPERT-BENCHMARK 总体从 73.35 提升至 87.60，通用能力基本保留。
- 消融：Expert-tuning 提升 Exact/Accuracy；VG-HRL 继续大幅提升；移除 verification 使 Exact 下降 11.30/12.43，Accuracy 下降 4.03/2.82。

> 最值得记住的一句话：显式建模领域工作流结构和中间步骤验证，比单纯扩大模型规模更能提升长程任务可靠性。
