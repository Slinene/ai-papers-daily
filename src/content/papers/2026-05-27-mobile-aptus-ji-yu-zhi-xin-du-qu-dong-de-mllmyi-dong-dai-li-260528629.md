---
title: 'Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based
  Mobile-Using Agents'
title_zh: Mobile-Aptus：基于置信度驱动的MLLM移动代理主动鲁棒交互框架
authors:
- Zheng Wu
- Pengzhou Cheng
- Zongru Wu
- Yuan Guo
- Tianjie Ju
- Aston Zhang
- Gongshen Liu
- Zhuosheng Zhang
affiliations:
- Shanghai Jiao Tong University
- Meta (GenAI)
arxiv_id: '2605.28629'
url: https://arxiv.org/abs/2605.28629
pdf_url: https://arxiv.org/pdf/2605.28629
published: '2026-05-27'
collected: '2026-05-28'
category: Agent
direction: 移动代理 · 置信度驱动交互
tags:
- Mobile Agent
- Confidence Calibration
- Human-Agent Interaction
- DPO
- Multimodal LLM
- Over-soliciting
one_liner: 提出通用置信度集成框架，结合有监督微调与基于语义相似检索和DPO的置信度偏差校正，同时缓解移动代理的过度执行和过度请求问题
practical_value: '- 可借鉴如何通过**置信度分数**让 agent 自主判断何时请求人工介入，避免因模型能力边界不清晰导致盲目执行或频繁打扰，适合电商售后、Agent
  助理等场景，可复用 confidence-aware 的输出结构设计。

  - 提出的**两阶段训练流程**（先 SFT 赋予置信度生成能力，再通过语义相似检索构建 DPO 对进行偏差校正）具有通用性，可直接迁移到推荐对话交互或生成式推荐中需要模型自省置信度的任务，提升模型自我评估的准确性。

  - 在构建 DPO 正负例时，**仅针对模型置信度预测错误的样本**并利用语义相似度检索 top-k 相关样本构造对比对，能高效利用数据，避免全量标注；该数据增强
  trick 可用于其他需要置信度校准的指令微调场景。

  - 实验表明，用**多智能体系统替代人工介入**可在不牺牲任务成功率的前提下减少打断次数（TASK成功率提升32.91%，平均额外延迟仅0.56s），这为电商业务流程中人类介入环节的自动化提供了可行架构：部署一个云端多智体系统，在本地
  agent 不确定时接管步骤。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：  
全自动移动代理（如 GUI 操作）常因模型能力边界模糊而**过度执行**（over-execution），在应请求帮助时强行操作；现有交互式代理虽能请求人类干预，但又频繁**过度请求**（over-soliciting），造成不必要的打扰。这两个矛盾尚未被统一解决。

**方法关键点**：  
- 提出**通用置信度集成框架**，分两阶段训练：自适应交互集成阶段和置信度偏差校正阶段。  
- **第一阶段**：利用 OS-Kairos 数据集中的置信度标注（对 OS-Atlas-Pro-7B 标注每个动作的置信度分数 1-5），通过有监督微调（SFT）使代理在预测动作的同时输出该动作的置信度分数，且不损害原有动作生成能力；训练目标为联合概率分解的下一 token 预测损失。  
- **第二阶段**：针对过度请求，设计**基于语义相似检索的 DPO 置信度偏差校正**。仅对置信度预测错误的样本，用文本和视觉编码器计算输入相似度，检索 top-k 最相似样本；当相似样本的置信度仍错误时，构造真值（ground-truth action+confidence）为 chosen，模型错误预测为 rejected；若相似样本置信度正确，则人为生成最远离真值的错误分数作为 rejected，形成 DPO 三元组进行偏好优化，鼓励模型在合适的时机才请求干预。  
- 最终模型 Mobile-Aptus 依据用户设定的干预阈值γ，灵活决定是否执行动作或请求干预。

**关键结果**：  
- 在 OS-Kairos、AITZ、Meta-GUI、AndroidControl 四个基准上，Mobile-Aptus 平均任务成功率（TSR）比最强基线提升**17.47%**，其中 OS-Kairos 上 TSR 达 68.32%（全自动 OS-Atlas 为 14.29%）。  
- 与交互式基线 OS-Kairos 相比，干预精度（IP）从 70.75% 提升到 84.83%，平均干预步数（AIF）从 1.59 降至 1.06，显著缓解过度请求。  
- 动态真机评估中，Mobile-Aptus 比 OS-Kairos 相对效率（RE）提升 6.67%，AIF 降低 0.32。  
- 用多智能体系统（GPT-4o）替代人工介入时，TSR 仍可提升 32.91%，且仅增加 0.56 秒延迟。  
- 消融实验验证了检索和 DPO 的贡献：仅 SFT 时 IP 71% 且 AIF 高，加入检索+DPO 后 IP 升至 84.83%，过度请求减半。

**最值得记住的一句话**：通过让代理学会生成置信度并用语义相似检索+DPO 精调置信度判断，可同时解决“乱执行”和“乱求助”问题，为实际部署中的人机协作提供实用范式。
