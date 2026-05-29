---
title: 'LiteCoder-Terminal: Scaling Long-Horizon Terminal Environments for Learning
  Language Agents'
title_zh: LiteCoder-Terminal：长时终端Agent的零依赖环境合成与训练
authors:
- Xiaoxuan Peng
- Kaiqi Zhang
- Xinyu Lu
- Boxi Cao
- Yaojie Lu
- Hongyu Lin
- Xianpei Han
- Le Sun
affiliations:
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2605.29559'
url: https://arxiv.org/abs/2605.29559
pdf_url: https://arxiv.org/pdf/2605.29559
published: '2026-05-27'
collected: '2026-05-29'
category: Agent
direction: 终端Agent训练 · 零依赖环境合成与SFT/DMPO
tags:
- Language Agents
- Synthetic Environments
- SFT
- DMPO
- Zero-dependency Synthesis
one_liner: 提出零依赖合成框架，自主生成可执行终端环境与专家轨迹，训练出的Agent大幅超越基座模型
practical_value: '- **领域驱动的任务合成**：利用Magpie-style高温采样，仅从领域描述自动生成大量任务，无需外部数据源，适合快速为电商客服、导购等Agent场景定制训练任务池。

  - **多阶段因果环境构建管线**：指令精炼→环境素材化→参考解→对抗式验证器→资源配置，每一步基于前置执行轨迹确保一致性，可直接复用于搭建电商交易模拟或推荐系统仿真环境，避免人工构造的漂移与错误。

  - **DMPO多轮偏好优化**：使用合成环境自带的自动验证器作为奖励信号，对长程Agent轨迹进行偏好学习，提升复杂任务表现；电商场景中的多轮对话式推荐Agent可借鉴此思路，利用可自动校验的虚拟用户行为进行RL训练。

  - **能力短板定向弥补**：零依赖架构天然支持按需合成特定领域训练数据，当电商Agent在售后纠纷、订单修改等弱项上表现不足时，可针对性地生成相关任务轨迹，数据效率高（本文仅用11K轨迹即逼近50万条轨迹方法的性能）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
训练能驾驭长时间、多步骤终端任务的Agent，需要大量可交互环境，但现有方法依赖爬取GitHub、Stack Overflow等外部仓库，不仅领域多样性差、环境可控性低，还无法针对性地强化模型的具体能力短板。为解决此问题，本文提出LiteCoder-Terminal-Gen，一种零依赖（zero-dependency）合成管线，能从领域规格出发全自动生成可执行、可验证的终端训练环境，提供可扩展的监督信号。

**方法关键点**  
- **领域→任务生成**：设计领域系统提示，利用对齐LLM的自回归特性（Magpie-style），不提供任何用户输入直接采样出任务描述，再经可行性检查过滤。  
- **五阶段可执行环境合成**：①指令精炼——将任务描述重写为可测试的规格，约束文件路径与输出格式；②环境初始化——基于Ubuntu Docker模板生成Dockerfile和输入工件；③解决方案合成——生成solve.sh证明任务可解；④验证器构建——通过“草案-攻击-精炼-定稿”四轮对抗迭代产出鲁棒的pytest测试集；⑤资源配置——分析所有产出估算并写入task.toml。每阶段都条件于前序执行日志，保证因果一致性。  
- **轨迹收集与过滤**：使用MiniMax M2/M2.1等多教师模型在Terminus 2、Claude Code、OpenHands等脚手架上收集交互轨迹，经LLM Judge按适应性、根基性、持久性和明确拒绝四个维度过滤，最终保留11,255条专家轨迹。  
- **SFT与DMPO训练**：先做SFT，后在自建RL环境上应用DMPO（Direct Multi-turn Preference Optimization），利用合成验证器提供的奖励信号对4B模型进行多轮偏好优化。

**关键结果**  
在Terminal Bench 1.0/2.0/Pro上评估：SFT后，32B模型分别达到29.06%、18.54%、34.00% pass@1，较基座Qwen2.5-Coder-32B-Instruct提升16.87、>4倍和20.5个百分点；30B-A3B和4B变体同样全面超越对应基座。仅用11.2K轨迹，性能已接近数据量为其40倍以上的TerminalTraj-32B（50.7K轨迹）和Nemotron-Terminal-32B（490.5K轨迹）。在DMPO后，4B模型在TB-2和TB-Pro上进一步从4.78%/21.50%提升至6.10%/23.00%。消融实验表明各领域的贡献分布均匀，模型在测试时多采样下的pass@k提升显著，且所学终端技能可泛化至SWE-bench（4B模型从1.2%升至5.2%）。

**一句话记忆**：依赖零外部数据，仅从领域定义出发自动生成批量的可执行、可验证环境与高质量轨迹，为语言Agent提供了“按需合成”的规模化训练范式。
