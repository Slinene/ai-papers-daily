---
title: Fighting Numerical Hallucinations via Data-centric Compilation for Online Financial
  QA
title_zh: 基于数据驱动编译的金融问答数值幻觉消除框架
authors:
- Hao Chen
- Xing Tang
- Qirui Liu
- Weijie Shi
- Shiwei Li
- Fuyuan Lyu
- Weihong Luo
- Xiku Du
- Xiuqiang He
affiliations:
- Shenzhen Technology University
- FiT, Tencent
- South China University of Technology
- The Hong Kong University of Science and Technology
- Huazhong University of Science and Technology
arxiv_id: '2605.31064'
url: https://arxiv.org/abs/2605.31064
pdf_url: https://arxiv.org/pdf/2605.31064
published: '2026-05-29'
collected: '2026-06-01'
category: Agent
direction: 金融问答 · 数据为中心编译 · 数值推理Agent
tags:
- Numerical Hallucination
- RAG
- Data-centric Compilation
- Structuring Agent
- Program Synthesis
one_liner: 提出数据为中心的推理编译器，通过对抗训练与编译执行消除金融QA中的数值幻觉
practical_value: '- **对抗数据构造**：在训练数据中注入可控噪声，可借鉴到电商问答Agent中提升对检索错误或无关文档的鲁棒性，减少商品价格、参数等数值误读。

  - **编译-执行推理范式**：将自然语言查询与检索文档转换为可执行程序（如SQL/Python），确保计算逻辑透明且可审计，适用于电商中的优惠叠加计算、库存统计等场景。

  - **数据结构化代理训练**：分阶段培养Agent的证据审计与程序合成能力，这种课程学习思路可用于训练电商推荐Agent的多步推理（如用户条件过滤、偏好权重计算）。

  - **数据为中心优化**：强调从数据构造端解决幻觉问题，启发我们构建面向电商任务的对抗性训练集，让Agent学会处理表格、图表等结构化文档中的噪音。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：金融问答中LLM常出现数值推理幻觉，RAG虽能引入外部知识，但仍面临检索噪声敏感、计算逻辑脆弱、结果不可审计三大挑战，现有模型中心方法未能综合解决。

**方法**：提出数据为中心推理编译器DCRC，分三步：
1. **对抗数据构造**：合成带可控噪声的训练样本，模拟真实检索错误，培养鲁棒性。
2. **多阶段训练**：训练数据结构化代理（DSA），先学习显式证据审计，再学习将审计后的证据转换为可执行推理程序（如SQL、表达式）。
3. **编译-执行推理**：DSA将用户查询与检索文档编译为可验证程序，交解释器执行，确保数值计算的可审计与精确。

**结果**：在离线基准TAT-QA等评测上大幅提升数值推理解答准确率，并已在腾讯元宝金融问答中线上部署，实现了端到端的忠实数值推理。
