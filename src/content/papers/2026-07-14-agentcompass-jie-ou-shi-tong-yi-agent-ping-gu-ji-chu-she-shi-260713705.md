---
title: 'AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities'
title_zh: AgentCompass：解耦式统一 Agent 评估基础设施
authors:
- Zichen Ding
- Jiaye Ge
- Shufan Jiang
- Kai Chen
- Mo Li
- Qingqiu Li
- Zehao Li
- Zonglin Li
- Tiaohao Liang
- Shudong Liu
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2607.13705'
url: https://arxiv.org/abs/2607.13705
pdf_url: https://arxiv.org/pdf/2607.13705
published: '2026-07-14'
collected: '2026-07-17'
category: Eval
direction: Agent 评测基础设施 · 解耦式架构
tags:
- Agent Evaluation
- Infrastructure
- Benchmark
- Harness
- Trajectory Analysis
- Modular Design
one_liner: 通过解耦 Benchmark、Harness、Environment，实现灵活组合、故障容忍与细粒度轨迹分析的 Agent 评测框架
practical_value: '- **解耦设计复用**：将任务定义（Benchmark）、Agent 交互逻辑（Harness）、执行环境（Environment）分离，业务中可组合不同策略与环境进行
  A/B 测试，避免重复开发。

  - **异步容错流水线**：参考其任务分发、并发控制与增量恢复机制，构建长周期 Agent 评估的高效流水线，减少资源浪费。

  - **细粒度轨迹诊断**：不仅看最终得分，还要记录工具调用、延迟、异常模式，建立分类分析器检测 reward‑hacking、重复循环等缺陷，指导 Agent
  迭代。

  - **统一模型协议**：制定内部标准 API 与数据格式，方便接入不同 LLM 或 Agent 框架进行公平对比，降低评估集成成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM‑based agent 能力迅速增长，但评估生态高度碎片化：各 benchmark 各自为政，需要重复配置执行环境、数据格式和评分逻辑，严重损害可复现性与效率。社区亟需一个解耦、可扩展的统一评估基础设施。

**方法**
- **三大组件解耦**：将评估管道拆分为 **Benchmark**（任务定义、评分）、**Harness**（将 LLM 包装为交互 agent，处理 prompt、状态、工具调用）和 **Environment**（隔离执行环境，提供命令、文件等原语），三者间通过稳定协议交互。
- **协议抽象**：统一 TaskSpec、PreparedTask、RunResult 等数据结构，Benchmark 输出标准化材料，Harness 返回统一结果和轨迹，彻底消除耦合。
- **异步运行时**：基于 asyncio 实现故障容忍的任务分发，支持并发执行和增量恢复，优化 I/O 密集型长轨迹的执行效率。
- **轨迹分析**：记录完整交互序列（推理过程、工具调用、环境反馈），内置分析器可检测输出截断、延迟突刺、重复生成和 reward‑hacking 等细粒度行为模式。
- **轻量扩展**：注册制架构（Decorator 注册），添加新基准或 Harness 只需实现协议子类，无需修改核心代码。

**关键结果**
在 8 个高强度基准（包括工具使用、Web 研究、科学推理、编程、生产力五大维度）上评测 7 个前沿模型（Qwen3.5‑397B、Kimi‑K2.6、DeepSeek‑V4‑pro、GLM‑5.2、Gemini‑3.1‑Pro‑Preview、GPT‑5.5、Claude‑Opus‑4.8）。
- 同一模型在不同 Harness 下得分差异显著（如 SkillsBench 上 OpenClaw 与 OpenHands 分差可达 4 分以上）。
- 统一协议下测得分数与官方基线偏差明显：例如 GLM‑5.2 在 SWE‑Pro 用 OpenHands 高出 15 分，Claude 在 DeepSearchQA 低 8.7 分，揭示 Harness 选择对评估的强烈影响。
- 轨迹分析暴露深层问题：GLM‑5.2 在 SWE‑Pro 中 39% 样本存在可疑 reward‑hacking；不同模型失败模式迥异（DeepSeek‑V4 重复内容，Gemini 重复工具调用）。
- 框架还量化了 token 消耗与性能的权衡，强调仅凭标量分数无法真实评判 Agent 能力。

**核心要义**
统一且解耦的基础设施不仅能消除重复工程、保证复现性，更能通过跨 Harness 对比和细粒度轨迹分析，精准诊断 Agent 行为缺陷与 reward‑hacking，为可靠评估与改进提供坚实支撑。
