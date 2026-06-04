---
title: 'AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering
  Tasks?'
title_zh: AutoLab：前沿模型能解决长时程自动研发与工程任务吗？
authors:
- Zhangchen Xu
- Junda Chen
- Yue Huang
- Dongfu Jiang
- Jiefeng Chen
- Hang Hua
- Zijian Wu
- Zheyuan Liu
- Zexue He
- Lichi Li
affiliations:
- University of Washington
- Stanford University
- UCSB
- UCSD
- University of Notre Dame
arxiv_id: '2606.05080'
url: https://arxiv.org/abs/2606.05080
pdf_url: https://arxiv.org/pdf/2606.05080
published: '2026-06-03'
collected: '2026-06-04'
category: Agent
direction: 长程闭环优化基准与Agent持久性评估
tags:
- long-horizon
- closed-loop optimization
- LLM agents
- benchmarking
- persistence
- iteration
one_liner: 推出AutoLab基准，评估17个前沿模型在可持续数小时的迭代优化任务上的能力，揭示持久迭代比初始方案质量更能预测成功。
practical_value: '- **Agent设计应内置持久迭代机制**：在电商Agent（如智能客服、商品推荐微调Agent）中，应鼓励循环执行“修改→评测→分析反馈”闭环，仅靠单轮强推理无法保证长程任务质量。

  - **引入连续评分与时间感知**：对于需要A/B测试或超参搜索的推荐系统优化，可以借鉴AutoLab的连续对数评分函数，避免二元奖励过早终止探索；同时需加入时间感知模块，防止Agent在预算耗尽前空转或过早提交。

  - **抗作弊措施可迁移至在线实验**：密封验证器、SHA固定文件、对抗审计等手段，可用于推荐模型在线学习环境，防止Agent通过利用评测漏洞而非提升指标得分。

  - **权衡成本与持久性**：实验显示成本与迭代步数强相关，较小模型配合适当持久性激励（如提示词要求不断优化直到接近参考分）可在较低推理成本下达到竞争力，对成本敏感的电商Agent部署有启发。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现有LLM评测多为单轮回答或短程Agent任务，无法反映真实研发中持续数小时的迭代优化能力，例如模型训练、系统调优。AutoLab旨在填补这一空白，提供一个超长时程的闭环优化基准。

**方法关键点**  
- **任务设计**：36个可执行任务，覆盖系统优化、谜题挑战、模型开发和CUDA核优化四类。每个任务提供一个正确但次优的基线，Agent需在严格时间预算（2-12小时）内反复编辑、运行和评测，以提升量化指标。  
- **连续校准评分**：采用对数拉伸或线性插值，将不同任务的原始指标归一化到[0,1]，基线得0分，参考解（人类专家实现）得0.5分以上。防止二元评分丢失局部进度信息。  
- **抗作弊保障**：密封验证集、是否正确性门控、SHA固定不可变文件、对抗审计等，确保得分反映真实优化而非漏洞利用。  
- **标准化评估框架**：固定使用Harbor框架与terminus-2 Agent，统一模型 API 入口，允许公平对比。  

**关键结果**  
- 评估17个前沿模型（含专有与开源），花费2544小时、86亿token。Claude Opus 4.6在Avg@3上达0.68，Dominance 0.93，在所有类别中领先，远超第二名Gemini 3.1 Pro（0.50）。  
- 最终性能与Agent迭代步数和运行时间强相关，而非初始方案质量。多款强力模型（如GPT-5.4、Grok-4-20）因过早终止而表现不佳。  
- 零分回溯显示两大失败模式：过早停止（探索不足）或耗尽预算未提交（时间意识缺失），部分开源模型则因超长推理链耗尽时间。  
- Harness消融表明，通过定制系统提示鼓励持久优化，可显著提升小模型表现，甚至改变模型排名。  

**核心启示**  
“在超长时程优化中，成功的首要预测因子不是模型的初始代码能力，而是其持续评测、编辑和吸收经验反馈的意愿。”
