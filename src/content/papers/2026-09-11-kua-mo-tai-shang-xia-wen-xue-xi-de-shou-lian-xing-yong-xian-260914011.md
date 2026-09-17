---
title: Convergent Emergence of In-Context Learning Across Modalities
title_zh: 跨模态上下文学习的收敛性涌现
authors:
- Nathan Breslow
- Seungwook Han
- Daniel Hyunsoo Lee
- Aayush Mishra
- Anqi Liu
- Daniel Khashabi
affiliations:
- Johns Hopkins University
- MIT
- University of Illinois Urbana-Champaign
arxiv_id: '2609.14011'
url: https://arxiv.org/abs/2609.14011
pdf_url: https://arxiv.org/pdf/2609.14011
published: '2026-09-11'
collected: '2026-09-17'
category: LLM
direction: 跨模态涌现的 in-context learning 规律
tags:
- In-Context Learning
- Cross-Modal
- Few-Shot
- Foundation Models
- Emergence
- Generalization
one_liner: 在六种模态中验证 few-shot ICL 普遍涌现，且任务难度效应在五个模态间相关，支持部分收敛涌现假设
practical_value: '- 跨模态 ICL 在时序、基因组等非文本序列上有效，提示在电商推荐中可将用户行为序列、商品曝光序列视为另一种模态，用 few-shot
  示例进行下一个交互预测或兴趣迁移。

  - 论文中的 paired-mapping 任务套件可作为统一评测框架，业务上可构建类似的「输入-输出映射」任务集，快速测试不同基础模型在推荐/搜索数据上的 few-shot
  适配能力，筛选适合 ICL 的任务类型。

  - 任务效应在多数模态间相关，说明任务难度的跨模态一致性；在为新业务场景选择可 ICL 的任务时，可以参考其他模态（如文本）上的难度排序，降低试错成本。

  - 对无法用自然语言指令描述的非语言任务（如 ID 序列、embedding 序列），few-shot ICL 可能是唯一有效的条件化机制，值得在搜索/推荐中储备这类能力以应对冷启动或新任务快速上线。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：ICL 在 LLM 中已被广泛研究，近期在基因组模型中也观测到 few-shot ICL。这引出一个问题：ICL 是否跨领域广泛涌现？如果涌现，是否存在共同的跨模态结构？作者提出 **Convergent Emergence Hypothesis**：当 ICL 涌现时，不同模态上的任务难度分布应趋于一致——在一种模态上受益于 ICL 的任务，在其他模态上也应受益。

**方法**：构建受控跨模态框架，在六个模态（语言、基因组、整数序列、时间序列、图像、蛋白质）上实例化同一组 paired-mapping 任务，比较 ICL 与受控基线，并计算各模态间任务效应的相关性。

**结果**：paired-mapping ICL 在六个模态中均涌现，且性能超过受控基线；五个模态之间任务效应呈显著相关。这为 Convergent Emergence Hypothesis 提供了部分支持，但并非所有模态都符合，说明 IC 的涌现具有跨域通用性但也存在模态特异性。
