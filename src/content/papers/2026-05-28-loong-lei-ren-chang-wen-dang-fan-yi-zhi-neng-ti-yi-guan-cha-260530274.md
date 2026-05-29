---
title: 'Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive
  Context Selection'
title_zh: Loong：类人长文档翻译智能体，以观察-行动自适应上下文选择
authors:
- Yutong Wang
- Xuebo Liu
- Derek F. Wong
- Zhilin Li
- Rongqing Jiang
- Min Zhang
- Shimin Tao
- Daimeng Wei
- Min Zhang
affiliations:
- Harbin Institute of Technology, Shenzhen
- University of Macau
- Huawei Translation Services Center
arxiv_id: '2605.30274'
url: https://arxiv.org/abs/2605.30274
pdf_url: https://arxiv.org/pdf/2605.30274
published: '2026-05-28'
collected: '2026-05-29'
category: Agent
direction: 文档级翻译智能体·上下文选择
tags:
- Document-Level Translation
- Agent
- Reinforcement Learning
- Context Selection
- Multi-Granularity Memory
one_liner: 用类人记忆与深度推理筛选多粒度上下文，结合RL优化翻译策略，大幅提升长文档翻译质量
practical_value: '- 多粒度记忆模块（Essence/Exemplar/Entity）可迁移到对话/推荐系统的用户记忆与上下文建模，结构化存储摘要、示例与实体，减少冗余噪声。

  - 观察-行动推理框架（Observe-and-Act）可用于智能体上下文选择，通过逐步过滤无关信息提升决策质量，避免“全量注入”带来的噪声与效率问题。

  - 利用RL（DPO）优化上下文选择与利用策略，从轨迹采样构造偏好数据，这一思路可泛化至推荐系统的上下文排序或个性化策略学习。

  - 对齐强制翻译算法（递归分裂保证句子级对齐）可用于需要严格对应关系的生成任务（如多语种商品标题对齐、语义ID生成保序）。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长文档翻译中，大语言模型受限于上下文窗口，且直接注入全部历史信息会引入噪声，损害翻译质量。现有方法或忽略跨段连贯性，或不加选择地使用所有记忆，导致性能瓶颈。

**方法关键点**：
- **3E记忆模块**：维护Essence（摘要）、Exemplar（句子对）、Entity（实体记录）三类记忆，检索后供智能体选择。
- **观察-行动推理**：将上下文选择分解为三个顺序步骤（先Essence、再Exemplar、最后Entity），每一步推理出各候选项的语义相关性，仅保留有益项。
- **策略优化**：并行采样多条推理-翻译轨迹，以COMET分数为效用信号构建选择策略与利用策略的偏好数据，通过SFT+DPO进行RL优化。
- **对齐强制推断**：递归分裂段落直至句子级对齐，确保源目标严格匹配，便于评估与记忆更新。

**关键实验**：在News Commentary和WMT24++的英⇔中、德、法六个方向上，搭配Qwen2.5/3、Llama3.1等不同骨干模型，LOONG平均提升最高达13.0分（sCOMET+dCOMET+LLM-Judge综合）。在超长文档（《西游记》翻译）中，基线方法因上下文超限失败，而LOONG保持稳定高质量。消融表明移除任一记忆组件或省略推理步均导致性能下降。跨域（文学、演讲）和跨语言（未见语种）测试验证了强泛化性。

**值得记住的一句话**：多粒度记忆与一步一步推理筛选的智能体设计，让长文本生成不再被冗余信息淹没，反而能稳定提取真正有用的上下文。
