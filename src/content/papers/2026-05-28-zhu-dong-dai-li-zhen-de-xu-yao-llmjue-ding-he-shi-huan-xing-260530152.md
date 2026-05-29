---
title: Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?
title_zh: 主动代理真的需要LLM决定何时唤醒与锚定吗？
authors:
- Xiaoze Liu
- Ruowang Zhang
- Amir H. Abdi
- Michel Galley
- Zhikai Chen
- Siheng Xiong
- Xiaoqian Wang
- Jing Gao
affiliations:
- Purdue University
- Microsoft
- Michigan State University
- Georgia Institute of Technology
arxiv_id: '2605.30152'
url: https://arxiv.org/abs/2605.30152
pdf_url: https://arxiv.org/pdf/2605.30152
published: '2026-05-28'
collected: '2026-05-29'
category: Agent
direction: 主动代理的触发决策优化
tags:
- Proactive Agents
- Temporal Graph Learning
- Trigger Detection
- On-device Deployment
- LLM Efficiency
one_liner: 用小型时间图学习模型代替LLM做触发决策，显著提升效率与准确性
practical_value: '- 电商智能助手的主动推送场景：将用户行为事件转化为动态图，用TGL模型实时计算触发概率和实体重要性，只在概率超过阈值时才调用LLM生成文案，大幅降低推理成本。

  - 推荐系统召回/排序的触发环节：借鉴TGL的图结构建模用户实时行为演化，生成触发信号与路由分数，可实现低延迟的个性化触发，适合部署在移动设备边缘端。

  - 隐私敏感场景的设备端部署：220MiB BF16的极低内存占用和13.99ms的端侧推理速度，适合在用户设备本地处理活动流，避免原始数据上传，保护隐私。

  - 架构设计思路：将原生的结构化事件流直接作为图输入，避免“结构化→文本→结构化”的冗余转换，可以用GNN替代LLM做事件的语义理解与重要性评估，业务中类似的结构化日志场景可复用此范式。'
score: 9
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有主动代理（proactive agents）将用户活动文本化，并在每个事件上调用LLM判断是否干预，但用户活动本身是操作系统以图形式维护的(actor, verb, object, timestamp)结构化事件流，转为文本再让LLM解析是一种冗余的往返。**方法**：提出将事件流视为动态图更新，采用小型时间图学习（TGL）模型作为编码器，通过时序图神经网络（如TGAT、TGN）建模事件序列，一次前向传播直接输出每个事件的触发概率和涉及实体的路由分数；只有触发概率超过阈值时，才调用下游LLM将结构化交接转换为面向用户的流畅语句。**关键结果**：在14个基线模型上（包括LLM触发方案），TGL将F1平均提升16.7，最高提升46.0；在触发架构对比中，单个TGL检查点取得最高的触发AUC，且部署阈值稳定性最优；推理速度在GPU上为11.13ms/事件，在消费级笔记本上为13.99ms/事件，比所有单次LLM触发方案快4–7倍（服务器）和12–83倍（笔记本）；模型BF16驻留内存约220MiB，可设备端部署并与隐私敏感的活动流共同运行。
