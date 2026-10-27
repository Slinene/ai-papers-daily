---
title: 'Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in
  Patent Examination'
title_zh: PatEx-Gym：面向专利审查新颖性评估的智能体现有技术搜索框架
authors:
- Qiyao Wang
- Xinyi Chen
- Hongbo Wang
- Jiayuan Lu
- Jianhang Li
- Minghuan Tan
- Yuan Lin
- Min Yang
affiliations:
- 中国科学院深圳先进技术研究院
- 中国科学院大学
- 大连理工大学
- 深圳理工大学
arxiv_id: '2610.33503'
url: https://arxiv.org/abs/2610.33503
pdf_url: https://arxiv.org/pdf/2610.33503
published: '2026-10-23'
collected: '2026-10-27'
category: Agent
direction: Agentic 搜索与轨迹合成
tags:
- Agentic Search
- Patent Examination
- Trajectory Synthesis
- SFT
- Prior-Art Retrieval
one_liner: 构建专利审查 agent 基准与轨迹合成方法，训练 4B 模型在现有技术搜索上接近大模型效果
practical_value: '- PASS 以文档访问作为隐式相关性信号来自动合成搜索轨迹，无需人工标注；可借鉴到电商搜索中，用用户点击、停留、加购等行为日志构造
  agent 训练数据，省去昂贵标注

  - 将搜索过程分解为 query 内部行为、query 间进展、轨迹级证据质量三个层次，可迁移到商品对比、选品 Agent 的 reward 设计或数据筛选，提升搜索策略学习效率

  - 4B 小模型仅靠 SFT 合成轨迹即可达到大模型 agent 的竞争性能，适合业务中低延迟、低成本的部署约束，可先训一个轻量 agent 再逐步扩展

  - 其 harness runtime 支持迭代搜索、文档访问、OA 生成的完整闭环，对搭建自营 agent 评测环境有参考意义，尤其适合需要复杂检索和推理链路的场景'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
专利审查要求 agent 在跨领域语料中发现稀疏现有技术、迭代改写查询、检查技术证据并生成审查意见，但现有评测只给静态候选集，未覆盖完整搜索-推理-评估过程。  

**方法关键点**  
- PatEx-Bench：1K 真实审查任务，两个大规模检索语料（>1M 专利、52K 科学论文），以及支持迭代搜索、文档访问、推理和 OA 生成的运行时。  
- PASS：免标注的 Prior-Art Agentic 搜索轨迹合成框架，利用文档访问作为隐式相关信号和证据获取锚点，建模 query 内部行为、query 间进展和轨迹级证据/结果质量，产出 PatEx-SynData。  
- PatEx-Agent：在合成轨迹上对 4B 模型做 SFT，得到轻量基线。  

**关键结果数字**  
实验表明最终决策准确率不能完全反映审查质量；现有技术在强前沿模型上也很难被发现。PatEx-Agent 在现有技术检索上达到与远大于自身的通用 agent 相当的性能，证明通过合成数据训练，紧凑 4B 模型可作为专利审查的竞争性基线。
