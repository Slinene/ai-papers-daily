---
title: 'ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents'
title_zh: ToolSpace：以工具为中心的长程智能体环境合成框架
authors:
- Guanting Dong
- Zhichao Sun
- Xinyu Yang
- Rui Wang
- Xin Deng
- Jiajie Jin
- Zhixiong Yang
- Junhao Huang
- Han Han
- Mingyu Ma
affiliations:
- Renmin University of China
- Fudan University
- Shanghai Jiao Tong University
arxiv_id: '2611.05036'
url: https://arxiv.org/abs/2611.05036
pdf_url: https://arxiv.org/pdf/2611.05036
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent 工具组合与环境合成
tags:
- Tool Composition Graph
- Environment Synthesis
- Long-Horizon Agents
- MCP
- SFT-RL
- Replay Verification
one_liner: 用真实执行轨迹构建加权工具组合图，按需合成环境并生成可回放验证的长程跨域任务
practical_value: '- **用真实调用日志构建工具/服务关系图**：在电商/搜索/推荐内部，可将搜索、推荐、商品详情、购物车、优惠券、订单、客服等
  API 的相邻调用关系，按 data/state/retry 三类规则确定性挖掘，避免 LLM 主观判断带来的幻觉连接，得到可执行的跨域工作流骨架。

  - **长程 Agent 训练数据合成**：借鉴 state-aware random walk + rollback，从真实日志图采样跨域工具链，只保留可重放、断言验证通过的
  task；可用于生成「搜索→推荐→加购→下单→售后」等多步购物助手任务，保证可执行性和状态一致性。

  - **按需环境落地，节省仿真成本**：对只读/无状态工具（如商品查询、搜索、推荐）复用录制返回值或缓存，不必为每个环境合成完整数据库；论文显示文件合成量减少
  55.3%，适合内部多业务系统大量只读 API 的场景。

  - **可验证奖励用于 Agent RL**：将断言验证结果作为二元执行奖励，配合 GRPO 做 on-policy RL，可提升长程工具编排；验证脚本同时能防止
  SFT 数据污染测试集。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 Agent 环境扩展以数据为中心：先合成数据库和场景，再推导工具与任务。这导致工具接口与真实服务不一致、工具编排缺乏执行证据、任务难以跨环境。真实长期 Agent 能力增长应以工具为原子单元，而不是静态环境数据。

**方法关键点**  
- 从真实 MCP 服务与开放 Agent 语料收集 20 万+ 执行轨迹，用确定性规则挖掘相邻调用间的 data/state/retry 三类依赖，构建加权工具组合图 G_TS；不依赖 LLM 判断。
- 对图做环境聚类，得到 804 个环境、77,760 个工具调用模式节点；仅对会产生状态变更的 operation 环境按需合成数据库，state-query 环境用查询结果初始化快照，stateless 工具直接复用录制返回值，降低合成成本。
- 在图上做 state-aware random walk，按边权采样可执行后继，失败时 rollback 重采样；达到目标工具数 L 和跨环境数 K 后，反向生成不含工具名/顺序的自然语言任务，并生成断言脚本，只有从初始状态重放通过全部检查的样本才保留。
- 共合成 34,376 条 SFT 样本、653 条 RL 候选；用 Kimi K3 做 teacher trajectory 和 reverse task 合成；RL 采用 GRPO，奖励为执行验证二元结果。

**关键结果**  
在 AutomationBench、SkillsBench、JobBench、τ3-Bench Banking、BFCL V4、Harvey LAB、OfficeQA Pro 七个长程工具使用基准上：ToolSpace 将 Qwen3.6-35B-A3B 平均分从 23.0 提升到 41.0，加 RL 后 43.2；ToolSpace-744B-A40B 平均分 56.6，与 Claude Opus 5 持平，超过 GPT 5.6 Sol 的 48.9。基于该流程升级的 AutomationBench Pro 和 τ3-Bench Banking Pro 上，7 个前沿模型最高掉 38.2 分。消融显示：去掉 state/data 边平均分别掉 7.1/7.4 分；LLM-judged edges 几乎和去掉 state edges 一样差，说明真实执行见证的连接更可靠；性能随数据量和环境规模持续提升。

**最值得记住的一句话**  
真实执行轨迹中见证的工具组合关系，比先合成环境再推导工具，更能支撑 Agent 长程能力扩展。
