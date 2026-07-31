---
title: 'SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based
  Program Synthesis from Scratch'
title_zh: SpecFirst：行为规范提取优先的两阶段从零程序合成框架
authors:
- Yihao Chen
- Shi Chang
- Feng Lin
- Khaled Chawa
- Boyuan Chen
- Shaowei Wang
- Ahmed E. Hassan
affiliations:
- Huawei Canada
- Queen’s University
- University of Manitoba
- Concordia University
arxiv_id: '2607.27167'
url: https://arxiv.org/abs/2607.27167
pdf_url: https://arxiv.org/pdf/2607.27167
published: '2026-07-28'
collected: '2026-07-31'
category: Agent
direction: Agent 规范驱动程序合成
tags:
- Specification Elicitation
- Program Synthesis
- LLM Agents
- Behavioral Oracle
- Two-Stage Framework
- ProgramBench
one_liner: 将需求工程引入LLM Agent，先提取行为规范再合成代码，从零编程通过率提升6.9%-21.3%
practical_value: '- **复杂搜索/推荐策略从零构建时，可引入强制分阶段规范提取**：让Agent先通过有限行为试探（如A/B黑盒探查推荐接口的响应规律）输出结构化Spec，再生成策略代码，避免直接编码导致的理解漂移。

  - **将行为Oracle思想用于推荐Agent评测**：设计黑盒环境（如模拟用户反馈的oracle），迫使Agent先探索行为边界再生成策略，提升策略的鲁棒性。

  - **在多步推理任务中应用“规范-实现”解耦**：例如，电商搜索Query意图理解与改写，可先让Spec Agent明确意图分类与改写约束，再由Code Agent生成规则或模型调用逻辑。

  - **工程化时重视中间产物的稳定性**：SpecFirst证明了提前固化的结构化规范能减少后续交互中的误解，在长上下文Agent任务中值得借鉴，如用JSON
  Schema约束中间输出格式。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM Agent在处理从零程序合成时，将文档阅读、行为探索与代码生成混在一个循环中，导致探索不充分、上下文漂移、早期误解被传播到实现中，ProgramBench上最先进模型解决率不足1%。受传统需求工程启发，提出将行为规范提取作为独立阶段。  
**方法**：SpecFirst两阶段框架。第一阶段，Spec Agent独立对可执行二进制进行黑盒探测，结合自然语言文档，生成结构化行为规范（前置条件、后置条件、边界案例等）。第二阶段，Code Synthesis Agent仅依据该规范实现程序，不直接接触原始文档或二进制。这样在编码前消除文档歧义，并为合成提供稳定的行为参考。  
**结果**：在ProgramBench全部200个实例上，使用GPT-4o、Claude等4个模型，SpecFirst相较单循环基线测试通过率提升6.9%-21.3%（如GPT-4o从8.5%提升至15.5%），二进制探索覆盖率提升9.4%-18.5%，均统计显著。行为分析显示，先有规范使代码构造更早开始且更持续。
