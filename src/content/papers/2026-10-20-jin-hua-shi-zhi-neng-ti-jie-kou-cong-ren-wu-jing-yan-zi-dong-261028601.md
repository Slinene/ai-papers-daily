---
title: Evolving Agent Interfaces
title_zh: 进化式智能体接口：从任务经验自动构建工具
authors:
- Saaket Agashe
- Yuzhe Yang
- Gonzalo Gonzalez-Pumariega
- Bhuvan Chandra Koduru
- Chih-Lun Li
- Jiachen Yang
- Ang Li
- Xin Eric Wang
affiliations:
- University of California, Santa Barbara
- Cornell University
- Carnegie Mellon University
- Simular
arxiv_id: '2610.28601'
url: https://arxiv.org/abs/2610.28601
pdf_url: https://arxiv.org/pdf/2610.28601
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent 接口自动进化
tags:
- Agent
- Interface Evolution
- Computer Use
- Population-based Evolution
- Tool Synthesis
- OSWorld
one_liner: 让智能体自主进化计算机操作接口，27B开源模型以低成本超越GPT-5.5和Claude Opus 4.8
practical_value: '- 将「接口/工具库」作为可进化资产：不要只靠人工预先设计固定工具集。可以从 Agent 在业务任务（如广告后台操作、选品数据拉取、报表生成）中的轨迹里自动提炼可复用
  API 或脚本，让模型从低频、低效的 GUI 操作转向结构化调用，直接降低任务成本并提高成功率。

  - 分离构造证据与选择证据：进化时只用无标签训练轨迹驱动工具修改，用独立的 validation 任务做选择，能显著降低对训练任务的过拟合。这在用 Agent
  自动生成推荐/广告流程工具时可直接复用：不要让生成工具的模型看到最终评分或测试集。

  - 低成本模型 + 进化工具层可以逼近甚至超越更强模型：论文用 Qwen3.8-27B 加上进化出的接口库，在 OSWorld V2 超过 GPT-5.5 和
  Claude Opus 4.8，成本仅 4.3% 和 1.5%。业务上可以优先在工具层做自动搜索，而不是一味换更大模型。

  - 重复验证对长程 Agent 任务很重要：ScienceBoard 上单次验证分数噪声大，平均多次验证后才选中稳定高分的仓库。业务里做 Agent 工具选择或在线评估时，对长流程任务应做多次重复评估，避免一次偶然高分误导。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机

计算机使用智能体的接口（能观察什么、能执行什么操作）长期由人工固定设计。这种静态接口无法跟上任务多样性和模型演进，导致智能体在不适配的接口上浪费大量推理预算：比如为了完成一个 shell 任务，要点击终端窗口、逐字符输入命令、从截图读取输出，而直接 shell 接口会快得多。已有方法要么靠 test-time 采样硬扛接口不匹配，要么在固定接口上做技能组合，无法扩展接口本身。核心问题是：接口设计被当作部署前的静态决策，而不是可以从智能体自身经验中持续改进的对象。

## 方法关键点

- **核心设定**：保持任务智能体的模型和 harness 不变，只进化其可用接口库。接口以代码形式存在于仓库中，包含可执行操作、观察格式、复用工作流和用法知识。
- **进化流程**：任务智能体在 synthetic 训练任务上执行并产生轨迹，不依赖 ground-truth 成功标签；meta-agent 分析这些轨迹，形成关于接口缺失或低效的假设，通过 mutation 或 crossover 修改仓库。
- **种群进化与不对称评估**：维护多个仓库变体，用 hidden validation 任务的分数做二元锦标赛选择父代，后代加入种群且保留父代。训练轨迹只给 meta-agent 看，validation 任务、轨迹和分数对 meta-agent 隐藏，只用于选择，从而降低对训练任务的过拟合。
- **可选的 scratch VM**：meta-agent 可以在相同 AMI 的虚拟机中打开应用、测试接口代码，提升 App-specific 和 Cross-App 接口的数量和质量。
- **任务集**：OSWorld V2 使用 30 个 synthetic 训练任务 + 15 个官方 validation 任务；ScienceBoard 使用 48 个 synthetic 训练任务 + 15 个 validation 任务。

## 关键实验结果

- **OSWorld V2（108 个任务）**：Qwen3.8-27B 加上进化出的接口库，binary success 达到 **21.30%**，超过 GPT-5.5 的 13.0% 和 Claude Opus 4.8 的 20.6%，成本仅为后两者的 **4.3%** 和 **1.5%**（$1.10 vs $25.50 vs $72.40）。
- **与固定接口同模型比较**：同样 Qwen3.8-27B，从 Qwen CUA 固定接口的 5.56% binary 提升到 21.30%；partial score 从 20.69% 提升到 46.90%（无 scratch VM）或 51.06%（有 scratch VM）。
- **ScienceBoard（169 个任务）**：独立进化后 success rate 从 seed 仓库的 55.03% 提升到 **58.58%**，较 Qwen CUA 的 41.4% 提升明显；KAlgebra 子集从 48% 提升到 68%。
- **进化策略对比**：population-based 比 linear evolution 在 partial score 上更高（51.06% vs 47.17%），而最佳 binary 来自无 scratch VM 的 population search。

## 一句话记住

**接口本身就是可进化的智能体能力，固定模型可以通过进化出的接口库在低成本下超越更强模型。**
