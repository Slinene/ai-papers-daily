---
title: 'Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential
  Recommendation'
title_zh: 重要处再深想：序列推荐中物品级自适应递归计算
authors:
- Zhanshuo Cao
- Jiakai Tang
- Yuqi Zhou
- Sunhao Dai
- Jun Xu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2610.30128'
url: https://arxiv.org/abs/2610.30128
pdf_url: https://arxiv.org/pdf/2610.30128
published: '2026-10-20'
collected: '2026-10-22'
category: RecSys
direction: 序列推荐 · 自适应计算深度
tags:
- Sequential Recommendation
- Adaptive Computation
- Early Exit
- Recursive Block
- LoopRec
one_liner: LoopRec 把序列推荐从固定深度改为逐 item 可退出递归，无需深度标签即可适应多 backbone 并稳定提升效果
practical_value: '- 行为序列建模可借鉴：用单个权重共享 block 替代固定堆叠层，在每层后为每个 item 加轻量 gate 做 exit/continue
  二选择，既省计算又可提升效果，适合 Transformer、SASRec 等 backbone 改造。

  - 训练无需物品级深度标签，工程上更易落地：可先固定最大递归深度 K，让 gate 自动学习哪些 item 需要深计算；如果要控制算力，可以在损失里加预算正则或直接设置更小的
  K。

  - 诊断结论可迁移到电商序列/CTR 模型：序列里多数历史 item 浅层就稳定，少数关键 item 需深推理；可对低频商品、近期交互、高相关商品分配更多计算或额外交叉深度。

  - 部署时注意动态递归带来变长计算：同一 batch 内不同 item 退出步数不同，可考虑按深度分组推理或设置最大深度兜底，低延迟场景尤其重要。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
现有序列推荐对用户历史序列中的每个 item 分配相同计算预算，忽略其对最终预测的贡献差异。文章先给出两项诊断：同一序列内不同 item 所需计算量差异很大，多数浅层处理即收敛，少数关键 item 到全深度才稳定；若有目标 item 的 oracle 信息，非均匀深度分配一致优于固定深度，说明固定计算既在已收敛 item 上浪费算力，又牺牲整体推荐质量。  

**方法关键点**  
LoopRec 用一个权重共享 block 递归建模序列，并在每个递归边界引入轻量 gate，对每个 item 独立做退出或继续的二值决策。表示已经足够成熟的 item 提前退出，需要更深推理的 item 继续进入下一轮递归。固定全局深度因此转换为逐 item 的学得属性，无需额外深度标签，也能适配多种 backbone。  

**关键结果**  
在公开基准、四类 backbone 上的实验显示，LoopRec 一致优于匹配的固定深度版本。进一步分析表明，学到的深度分配与 oracle 分析一致：低频 item 和更近的交互自然获得更深计算。代码已公开。
