---
title: 'EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis
  and Robust RL'
title_zh: EnvFactory：通过可执行环境合成与鲁棒RL扩展工具使用智能体
authors:
- Minrui Xu
- Zilin Wang
- Mengyi DENG
- Zhiwei Li
- Zhicheng Yang
- Xiao Zhu
- Yinhong Liu
- Boyu Zhu
- Baiyu Huang
- Chao Chen
affiliations:
- LARK, HKUST (GZ)
- Huawei Technologies Co., Ltd
- University of Cambridge
- UCL
- HKUST
arxiv_id: '2605.18703'
url: https://arxiv.org/abs/2605.18703
pdf_url: https://arxiv.org/pdf/2605.18703
published: '2026-05-18'
collected: '2026-05-19'
category: Agent
direction: Agent 工具使用训练环境与数据合成
tags:
- Environment Synthesis
- Agentic RL
- Tool-Use
- Trajectory Generation
- MCP
- Topology-aware Sampling
one_liner: 全自动构建有状态可执行工具环境并生成自然多轮隐式意图轨迹，高效训练工具使用Agent
practical_value: '- **电商代码沙盒环境自动化构建**：借鉴EnvFactory的Search-Code-Test多Agent协作，可针对电商核心API（商品搜索、下单、物流查询等）自动生成可执行的MCP服务器，用于训练智能客服或购物助手，确保执行可靠且状态隔离。

  - **自然隐式意图的多轮数据合成**：拓扑感知采样与校准细化策略可将多个API调用链转换为含歧义、省略参数的真实用户请求，例如“帮我查一下最近那个订单”，要求Agent自行推断订单ID。这种数据对训练Agent的上下文推理能力十分有效，可直接用于电商场景SFT数据增强。

  - **复合奖励函数设计**：论文提出的轨迹匹配奖励 + 最终状态等价奖励 + 长度惩罚的复合RL奖励框架，可避免单一奖励偏差。在电商智能体中训练工具调用策略时，可保证正确执行的同时控制冗余工具调用。

  - **资源高效训练范式**：仅用85个环境、2500+条轨迹即可大幅提升小模型（1.7B/4B）的多轮工具使用能力，为电商业务中快速迭代、低成本训练提供参考：优先保证环境验证质量与轨迹自然度，而非盲目追求数量。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前基于强化学习（Agentic RL）训练工具使用Agent面临两大瓶颈：一是缺乏可扩展、稳定且执行正确的交互环境，现有方案要么依赖昂贵、高延迟的真实API，要么使用易产生幻觉的LLM模拟器；二是合成训练轨迹往往过度指定，像“指令清单”而缺乏人类请求中常见的隐式意图、指代歧义等自然沟通特征，导致训练出的Agent推理能力受限。

### 方法关键点
- **EnvGen全自动环境构建**：由Search Agent从真实网络资源挖掘工具概念并生成蓝图，Code Agent实现Pydantic模式的状态数据库和可执行Python代码，Test Agent迭代验证并生成修正报告，最终产出稳定、可会话隔离的MCP工具服务器。
- **依赖工具图与拓扑感知采样**：通过语义嵌入匹配输入输出参数构建工具间依赖图，并引入LLM精炼逻辑关系。采样时递归解析工具必需的内部依赖（如`hotel_id`来自前一步输出），并支持随机分支实现非线性工具链，确保生成的多步逻辑连贯。
- **自然查询合成与校准细化**：QueryGen先规划情景、生成初始状态，再将工具链切分为多轮对话。通过子目标分解、意图表达后，施加隐性指代、动作压缩、歧义引入、目标扩展四种校准操作，将生硬指令转化为自然、隐晦的用户请求。随后在沙盒中执行并筛选出可通过工具正确解决的轨迹作为监督信号。
- **两阶段训练与复合奖励**：首先用细化的SFT轨迹进行监督微调冷启动，然后使用GRPO进行RL，奖励函数融合轨迹级动作匹配、最终数据库状态等价以及长度惩罚，权重均衡（α=0.5）效果最佳。

### 关键实验
EnvFactory仅用85个环境、842个工具，生成1622条SFT和953条RL轨迹，显著少于对比方法AWM和EnvScaler（环境多5倍以上）。在Qwen3-1.7B/4B/8B上，SFT后BFCL多轮得分分别提升至23.25、44.25、46.50，MCP-Atlas pass率提升近一倍；RL进一步拉高至28.38、48.50、49.00，并在对话式基准τ2-Bench和VitaBench上带来稳定增益。消融实验证实RL前SFT冷启动不可或缺，校准细化提升了长上下文和缺失功能场景下的泛化，而复合奖励中的轨迹与状态信号需平衡配合。

### 核心洞见
**即使训练环境与数据量远少于先前工作，通过自动构建可验证的有状态环境并合成自然隐式意图轨迹，仍能高效训练出具有强工具调用能力的Agent。**
