---
title: 'optimize_anything: A Universal API for Optimizing any Text Parameter'
title_zh: 优化一切：通用文本参数优化 API
authors:
- Lakshya A Agrawal
- Donghyun Lee
- Shangyin Tan
- Wenjie Ma
- Karim Elmaaroufi
- Rohit Sandadi
- Sanjit A. Seshia
- Koushik Sen
- Dan Klein
- Ion Stoica
affiliations:
- UC Berkeley
- MIT
arxiv_id: '2605.19633'
url: https://arxiv.org/abs/2605.19633
pdf_url: https://arxiv.org/pdf/2605.19633
published: '2026-05-18'
collected: '2026-05-21'
category: MultiAgent
direction: LLM 驱动的文本优化统一框架
tags:
- LLM optimization
- evolutionary search
- text artifact
- agent architecture
- side information
- Pareto search
one_liner: 单一 LLM 优化系统横跨六个领域（代码、提示、Agent 架构、调度等）达到 SOTA，首次实现文本优化的通用范式。
practical_value: '- **用统一的优化 API 迭代业务提示/策略/逻辑**：只需提供初始候选文本、评分函数和可选诊断信息，即可让 LLM 自动优化。对于电商推荐中的排序规则、Agent
  的决策逻辑、提示工程都可用同一套代码调用 optimize_anything，避免为每个任务写独立搜索逻辑。

  - **引入“侧信息 (Side Information)”加速优化**：在评分函数中返回编译器错误、运行日志、渲染图像等诊断反馈，比只给一个标量分数能快 4-6
  倍收敛，最终效果也更好。在生成式推荐中，可以设计评估器输出点击率的同时，额外给出哪些特征未生效、哪一步解码失败等，显著提升优化效率。

  - **多任务搜索：跨问题共享优化模式**：如果有一批相关任务（如多个 CUDA 核、多个推荐场景的 prompt），用 multi-task 模式共享帕累托前沿，比单独优化每个任务效果更好，尤其适合团队维护多个业务线的
  prompt 或 Agent 配置。

  - **帕累托精英保留避免陷入局部最优**：按细粒度指标（如每个测试样本的得分）建立帕累托前沿，保留不同专长的候选，避免仅凭平均分剪枝导致模式丢失。在推荐系统中，可保留点击率高但转化率低的候选与转化率高但点击率低的候选，在后续迭代中重组出更优组合。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 LLM 优化系统（FunSearch、AlphaEvolve、GEPA 等）都局限于单一领域（代码、提示等）和单一模式（单任务或泛化），未实现跨领域的通用文本优化。实际业务中，推荐排序策略、Agent 架构、CUDA 核、调度算法等本质上都是“改进一个文本工件并获得评分”的循环，若能统一 API 将大幅简化工程投入。

**方法关键点**
- **统一接口**：用户提供种子文本、评估函数（返回分数 + 可选的诊断信息）和可选数据集，系统自动处理搜索策略。支持单任务、多任务、泛化三种模式。
- **侧信息（SI）作为一等公民**：评估函数可返回编译器错误、渲染图像、细粒度子分数等，LLM 据此进行针对性反思与改进，而非盲目的标量梯度下降。
- **帕累托搜索**：基于细粒度目标（如每样本得分、多指标）维护帕累托前沿，避免平均聚合掩盖互补优势。候选按前沿出现频率加权采样，通过反思产生新候选。新增精炼步骤修复代码格式错误，并支持内容寻址缓存减少重复评估。
- **扩展到任意文本工件**：在 GEPA 提示优化算法基础上，添加单任务/多任务前沿类型、精炼步骤、SI 类型及后端适配层，从而支持代码、Agent 架构、SVG 图像等多种文本形式。

**关键实验**
- 在 6 个主要领域验证，每个领域均实现 SOTA：
  - **ARC-AGI Agent 架构（泛化）**：从朴素 10 行代码进化到 300+ 行 4 阶段流水线，测试准确率 32.5% → 89.5%。
  - **云调度算法（泛化）**：CloudCast 节省 40.2% 成本；Can’t Be Late 节省 7.8%，均超过 ADRS 榜单冠军。
  - **CUDA 核生成（多任务）**：87% 核达到 PyTorch 基准，25% 提速 20%+，多任务模式优于单任务。
  - **AIME 提示优化（泛化）**：GPT-4.1-mini 准确率 46.67% → 60.00%，超过 MIPROv2。
  - **圆包装（单任务）**：超越 AlphaEvolve 已发布解，在受控对比中用更少评估次数超越 OpenEvolve。
  - **消融实验**：侧信息使提示优化收敛快 4-6 倍，最终得分 86.32 vs 82.5；多任务搜索随相关任务数量增加收益放大，但不相关任务（如不同 N 的圆包装）会引入噪声。
- **核心一句话**：将任何文本改进问题形式化为“评估、反思、进化”的循环，并通过统一的 API 让 LLM 自动完成跨领域的优化，首次证明文本优化是一种通用的问题求解范式。
