---
title: 'Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact
  Agents'
title_zh: Evoflux：为紧凑型代理推理时演化可执行工具工作流
authors:
- Kushal Raj Bhandari
- Ling Yue
- Ching-Yun Ko
- Dhaval Patel
- Shaowu Pan
- Pin-Yu Chen
- Jianxi Gao
affiliations:
- Rensselaer Polytechnic Institute
- IBM Research
arxiv_id: '2606.12674'
url: https://arxiv.org/abs/2606.12674
pdf_url: https://arxiv.org/pdf/2606.12674
published: '2026-06-09'
collected: '2026-06-12'
category: Agent
direction: Agent 工具使用 · 工作流演化
tags:
- Tool Agent
- Workflow Evolution
- Inference-Time Search
- Compact LM
- MCP
- Execution Feedback
one_liner: 在少量教师轨迹下，推理时进化搜索让小型模型工具可用性从~3%升至17-24%，优于等量微调。
practical_value: '- 工具调用/API编排场景下，用进化搜索+执行反馈替代单次生成，可大幅提升小型模型在工具选择、参数填写的正确性，尤其适合低延迟、高隐私的部署需求。

  - 结构化编辑操作（工具替换、参数修正、依赖调整）直接针对常见失败模式，可作为通用变异算子嵌入到现有Agent工作流优化中。

  - 自适应强度控制（基于增长信号动态调节探索/利用比例）是一种轻量级控制策略，可借鉴到其他推理时搜索算法中，避免无谓的随机探索。

  - 在标注数据极度有限时，不要急于微调，推理时执行驱动的修复可能比权重更新更稳定，能规避灾难性遗忘风险。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
小型语言模型（1.5B-4B）因低延迟、低成本、可本地部署等优势，被寄望于构建工具使用代理。但在 MCP 协议下，代理需要从动态目录中发现工具、满足 schema、维护中间输出依赖、并将答案扎根于执行结果，小型规划器极易产生看似合理却在解析、校验或执行中失败的工作流。传统方案通过大量教师轨迹蒸馏来提升效果，但在仅有数百条轨迹的预算下，微调只能学到表面格式，难以覆盖修复过程，甚至引发灾难性遗忘。因此，论文转而研究：在同样稀缺的监督预算下，将计算投入推理时搜索是否比微调更可靠。

### 方法关键点
- **问题建模**：将紧凑代理的工具使用视为可执行工作流的修复问题，而不是一次性生成。
- **Evoflux 框架**：把小型模型当作提议算子，在推理时进行有界进化搜索。每个任务启动一个种群，通过结构化编辑（工具交换、参数编辑、节点插入/删除/重排等）进行变异，利用编译、静态检查、执行日志和 LLM 评分作为适应度，迭代优化工作流图。
- **自适应强度与元引导**：基于近期改进量计算“增长信号”，动态调节探索概率；当局部变异停滞时，触发元引导，重新设计整体工作流。
- **多样性修剪**：按动作结构哈希分桶，轮选保留，避免种群坍缩为相似方案。

### 关键实验
- **数据集**：MCP-Bench，包含 28 个实时 MCP 服务器和 250 个工具，任务需模糊发现、多跳执行。将数据分为搜索集和留出评估集。
- **基线**：零样本生成、SFT（用搜索集最佳候选）、SFT+DPO、ReAct。所有训练基线使用相同的小量教师轨迹。
- **核心结果**：在留出集上，4 个紧凑模型（Llama-3.2-3B、Qwen3.5-4B、SmolLM3-3B、DeepSeek-R1-Qwen-1.5B）的初始执行可行性仅约 3%，Evoflux 可提升至 17–24%；SFT 和 SFT+DPO 要么持平，要么低于零样本，甚至降至 0%；ReAct 在强规划器上得分更高，但方差和 token 成本显著增加。

### 核心启示
在稀缺教师轨迹预算下，将推理计算用于执行反馈驱动的修复，比用于权重更新更可靠；当标注数据不足以覆盖错误恢复模式时，优先考虑测试时搜索。
