---
title: 'Assign and Add: A Mechanistic Study of Compositional Arithmetic'
title_zh: 分配与相加：组合算术的机制研究
authors:
- Brady Exoo
- Alberto Bietti
- John Sous
affiliations:
- Yale University
- Flatiron Institute
arxiv_id: '2605.31497'
url: https://arxiv.org/abs/2605.31497
pdf_url: https://arxiv.org/pdf/2605.31497
published: '2026-05-29'
collected: '2026-06-01'
category: Reasoning
direction: Transformer组合泛化机制与训练动态
tags:
- compositional generalization
- mechanistic interpretability
- modular addition
- training dynamics
- transformers
one_liner: 通过变量分配与模加任务，揭示Transformer组合泛化的内部机制、训练动态和模块复用方式
practical_value: '- **多技能Agent的训练策略**：论文发现模型分三阶段学习（先原子技能模加、再组合结构、最后泛化到难样本），在训练电商Agent或多技能推荐系统时，可采用类似课程学习，先确保单一能力收敛再混合任务，避免联合训练导致的负迁移。

  - **模块复用的架构启发**：同一MLP模块在直接和间接输入下均实现模加，表明模型自发形成可复用电路。设计生成式推荐或Query改写模型时，可刻意为共享子任务预留模块化组件（如专用LoRA分支），提升参数效率和组合泛化。

  - **组合泛化的验证方法**：通过划分不相交训练集测试未见过组合的泛化能力，可作为评估推荐模型对新用户-新商品交互、新搜索词组合鲁棒性的内部基准，提前发现模型是否真正理解底层规则而非记忆。

  - **注意训练后期的“精调”阶段**：本文观察到最终阶段模型学会处理训练中未见的困难序列，暗示适当延长训练或加入类似难例挖掘的机制可能对复杂推理任务有益，对需要处理长尾查询或冷启动场景的电商Agent有参考意义。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
大型语言模型能组合已习得技能完成未见复杂任务，但组合泛化如何产生的细节仍不清楚。本文在一个可控的变量分配与模加设定下，研究Transformer中的组合泛化机制，以揭示其内部运作原理。  

**方法**  
- 构建一个简单任务：给定变量赋值（如 `a=3, b=5`）和模加运算（如 `a+b mod 7`），模型需先解析赋值再执行加法。  
- 训练数据按变量-数值组合划分为不相交集，使模型在训练中未见过某些组合，测试对未见组合的泛化能力。  
- 通过机械可解释性工具分析模型内部激活和电路，发现同一MLP模块负责模加运算，无论输入是直接给出数值还是通过变量间接传递。  
- 分析训练动态，揭示三个学习阶段：①首先学到正确的模加运算；②随后形成变量赋值解析所需的结构；③最后在精调阶段泛化到训练中未出现的困难序列。  
- 提供理论框架，解释训练动态如何自然催生组合性内部机制。  

**关键结果**  
- 小规模Transformer能在不相交训练数据下成功泛化到未见变量-数值组合，准确率达到近100%。  
- 模加运算被封装为可复用模块，在直接和间接输入条件下共享同一电路，这是组合泛化的关键。  
- 训练三阶段清晰分离，最终泛化阶段使模型在困难样本上的准确率提升，体现从死记到理解规则的转变。
