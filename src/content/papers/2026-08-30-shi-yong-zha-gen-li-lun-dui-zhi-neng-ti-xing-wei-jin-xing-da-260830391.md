---
title: Using Grounded Theory for Agent Behavior Analysis at Scale
title_zh: 使用扎根理论对智能体行为进行大规模分析
authors:
- Zhuoran Lu
- Yangyang Yu
- Zhuoyan Li
- Yibo Meng
- Nan Jiang
- Chengxi Zang
- Jie Gao
- Ziang Xiao
affiliations:
- Purdue University
- Stevens Institute of Technology
- Cornell University
- University of Texas at El Paso
- Johns Hopkins University
arxiv_id: '2608.30391'
url: https://arxiv.org/abs/2608.30391
pdf_url: https://arxiv.org/pdf/2608.30391
published: '2026-08-30'
collected: '2026-09-05'
category: MultiAgent
direction: 多智能体扎根理论轨迹分析
tags:
- Grounded Theory
- Agent Behavior Analysis
- Multi-Agent
- Trajectory Analysis
- LLM
- Taxonomy
one_liner: 提出 AutoTraceGT，首个用多智能体流水线自动执行扎根理论分析智能体轨迹，生成行为分类法
practical_value: '- 对电商搜索/推荐中的 Agent 轨迹（如购物助手、推荐对话、自动选品 agent）可部署 AutoTraceGT 自动生成失败/成功行为分类法，替代依赖人工标注
  taxonomy 的冷启动。

  - 借助扎根理论的饱和准则，用迭代编码自动判断何时停止标注，降低大规模轨迹审计成本，同时保留从数据到结论的可审计链路，便于业务复盘。

  - 生成的 codebook 可作为下游失败预测的特征空间，显式提供可解释的行为维度；在缺少高质量标注时，其效果优于直接对原始轨迹做 zero-shot/few-shot
  LLM 判断。

  - 该流水线能发现人工分类法遗漏的行为模式，适合探索推荐 agent 中长尾失败模式或新出现的异常行为，尤其是多步决策中的局部合理但全局失败链条。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 智能体在复杂任务中仍会失败，现有轨迹分析要么依赖预定义分类器，难以发现长尾/新行为模式，要么依赖人工定性分析，规模受限。论文将社会科学中的扎根理论引入 agent 轨迹分析，提供饱和准则与可审计的数据→理论路径。

方法：提出 AutoTraceGT，首个多智能体流水线。它迭代执行开放式编码、主轴编码与理论编码，直到达到饱和，输出面向具体任务的行为分类法。多个 LLM agent 分工完成编码、比较、归纳与理论构建，保留可追溯的编码决策。

结果：在 6 个轨迹语料上，AutoTraceGT 生成的 codebook 恢复人工标注失败模式的 73-91%，并发现人工分类法遗漏的额外模式；产生的理论叙述与专家既有解释一致。将 codebook 作为演绎特征空间用于下游失败预测时，优于 zero-shot 和 few-shot LLM 基线。
