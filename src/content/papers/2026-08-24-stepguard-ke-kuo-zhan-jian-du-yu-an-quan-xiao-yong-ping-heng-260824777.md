---
title: 'StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility
  Balancing'
title_zh: StepGuard：可扩展监督与安全-效用平衡的步骤级护栏
authors:
- Zhijie Zheng
- Yu Li
- Chen Qian
- Yuqian Fu
- Yanwei Fu
- Lu Sheng
- Jing Shao
- Dongrui Liu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Beihang University
- Fudan University
- Renmin University of China
- KAUST
arxiv_id: '2608.24777'
url: https://arxiv.org/abs/2608.24777
pdf_url: https://arxiv.org/pdf/2608.24777
published: '2026-08-24'
collected: '2026-08-31'
category: Agent
direction: Agent安全护栏 · step-level监督与效用平衡
tags:
- Agent Safety
- Guardrails
- Step-Level Supervision
- Safety-Utility Balance
- Synthetic Data
- GRPO
one_liner: 4B步骤级agent安全护栏，通过prefix-aligned合成数据与Balance-GRPO在低误杀下将平均ASR降低77.3%
practical_value: '- 对电商/广告Agent的高风险工具调用（改价、退款、批量发消息、导出数据）增加执行前step-level guard，4B模型即可取得接近GPT-5.4的判别能力，单次检查约600ms/195
  tokens，适合在线部署。

  - 用prefix-aligned合成数据构造“同一前缀、不同安全动作分支”的对比样本，并加入benign tool-reuse轨迹，能明显降低guard对工具身份的误判，防止把易感工具一律当成风险。

  - 训练时用Balance-GRPO：根据rollout batch中safe/unsafe两类accuracy差距动态reweight advantage，可把safe-unsafe
  gap从13.0压缩到8.0，在AgentDojo/AgentDyn上utility提升最多6.7点而ASR仅升0.3；这比固定class weight更稳。

  - 如果业务中有安全与转化/体验的trade-off，可以借鉴按类别感知的on-policy校准策略，不必改prompt或reward，只需对优势做加权；另外保留step-level标注和风险定位输出，便于审计与策略调优。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM-based agents通过工具调用可执行修改文件、泄露信息、未授权交易等真实后果动作。现有护栏多在完整轨迹后审计，缺少执行前step-level监控；同时guard普遍存在over-defense或under-defense偏差，难以平衡安全与任务效用。主要障碍是缺乏大规模高质量step-level监督，以及训练方法无法根据safe/unsafe accuracy gap显式控制平衡。

**方法关键点**：
- **StepGen数据引擎**：先构造带risk anchor i*的unsafe轨迹，再从anchor前共享prefix分支生成Refuse / Aware两种safe轨迹，并单独生成benign tool-reuse轨迹；每个action标注Safe/Unsafe与风险类别，rule + LLM过滤。最终产出3K SFT + 4K RL数据。
- **StepGuard模型**：基于Qwen3-4B-Instruct，冷启动SFT学习guard格式与风险推理，再做在线RL优化。
- **Balance-GRPO**：扩展GRPO，在normalized advantage上乘class-count因子c_i和accuracy-gap因子ω_i，对当前accuracy较低的类给更大更新权重；不修改prompt和原始reward，并通过KL正则保持稳定。

**关键结果**：
- 静态评估：trajectory-level 83.0 acc / 83.3 F1，step-level 84.8 acc / 84.1 F1，为open-weight guard中最高，性能接近GPT-5.4。
- 守卫Agent评估：相对no-guard平均ASR降低77.3%，utility仅降2.8；AgentDojo上ASR 1.2 / utility 90.7，AgentDyn上ASR 9.3 / utility 66.7。
- Ablation：Balance-GRPO将safe-unsafe accuracy gap从13.0降到8.0，utility最多提升6.7点而ASR仅升0.3；StepGen的prefix监督和benign tool-reuse分别显著提升轨迹级与step-level F1。
- 推理开销：单次guard调用599.9ms、195.5 tokens，占AgentDojo任务时间7.24%。

**最值得记住的一句话**：step-level执行前护栏 + prefix-aligned正负样本 + 面向类间accuracy gap的动态优势加权，是在不显著牺牲任务效用下大幅压低agent攻击成功率的关键组合。
