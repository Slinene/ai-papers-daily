---
title: 'MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems'
title_zh: MemTrace：大语言模型记忆系统的错误溯源与归因
authors:
- Xinle Deng
- Ruobin Zhong
- Hujin Peng
- Xiaoben Lu
- Yanzhe Wu
- Guang Li
- Buqiang Xu
- Yunzhi Yao
- Jizhan Fang
- Haoliang Cao
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2605.28732'
url: https://arxiv.org/abs/2605.28732
pdf_url: https://arxiv.org/pdf/2605.28732
published: '2026-05-26'
collected: '2026-05-28'
category: Agent
direction: Agent 记忆系统错误诊断 · 执行图归因
tags:
- error tracing
- execution graph
- memory systems
- failure attribution
- LLM agents
- prompt optimization
one_liner: 将记忆流水线转化为执行图，通过图遍历定位最早故障操作，实现跨会话错误自动诊断与自动提示优化
practical_value: '- **记忆系统可观测性**：通过 smartcomment 工具将任意记忆流水线的变量与操作依赖记录为执行图，可在电商对话 Agent
  中定位记忆丢失、错误更新等故障。

  - **细粒度错误归因**：MemTrace 的图遍历优先检查早期操作，避免在长程交互中盲目搜索；引入源证据和系统先验知识能显著提高操作定位准确率（+12% OIA），适用于推荐系统的对话记忆调试。

  - **自动提示优化闭环**：将错误归因作为 credit assignment，只对故障操作涉及的局部 prompt 进行优化，避免在长轨迹上做全局优化；即使归因不完美（72.5%
  OIA），仍能带来 7.62% 的端到端性能提升，适合在线自动修复。

  - **执行图的结构化诊断**：生成的诊断报告可汇总不同记忆系统（RAG、Mem0、EverMemOS）的薄弱点，例如提取模块丢失细粒度信息、重排序模块失效等，可指导电商记忆架构选型与迭代。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
记忆系统是 LLM Agent 支撑长期交互的核心组件，但错误常源于数轮之前的记忆更新、覆盖或检索偏差，难以从扁平日志中定位。现有记忆评测仅给出整体成败，无法还原故障因果链。因此，急需一种可追溯信息跨会话传播路径的自动化归因方法。  

**方法关键点**  
- **执行图建模**：自研 `smartcomment` 工具包在代码关键操作处插桩，将记忆流水线记录为变量-操作有向无环图，清晰显示记忆的创建、修改、传播与最终使用。  
- **MemTraceBench**：基于 LoCoMo、LongMemEval、RealMem 数据集，覆盖长上下文、RAG、Mem0、EverMemOS 四种记忆系统，收集 160 个带人工标注的失败 case（含故障操作 ID、错误类型及解释）。  
- **MemTrace 归因算法**：以失败案例的问题和答案进行混合检索初始化搜索起点，按时间戳优先级遍历操作子图，通过局部正确性判断向下传播，直至定位最早的最小故障操作集（Decisive Error Set）。同时提供 MemTrace-OBS 变体，将操作块排序后支持全局正则搜索，大幅降低 token 开销。  
- **闭环优化**：利用 MemTrace 归因的输出操作，仅对该操作涉及的 prompt 调用现成优化器，避免长轨迹上下文爆炸，实现多轮自动调优。  

**关键实验**  
用 GPT-4.1 mini 和 GPT-5.4 作为 agent backbone 在 MemTraceBench 上评测。错误类型预测准确率（ETA）：GPT-5.4 + MemTrace 达 54.38%；故障操作识别准确率（OIA）：GPT-5.4 + MemTrace + 源证据 + 先验知识达 58.33%。MemTrace-OBS 大幅降低成本，长上下文场景 token 用量仅为 MemTrace 的 15.25%。在 Mem0 上应用闭环优化，3 轮迭代后测试集性能提升 7.62%，即使 OIA 仅有 72.5% 仍有效。  

**最值得记忆的一句话**  
即使不完美的操作级归因信号，也能有效指导记忆系统的提示优化，为自动修复长程对话错误提供实用路径。
