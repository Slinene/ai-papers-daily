---
title: 'Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups
  from Adaptive Teacher Guidance'
title_zh: 在失败处蒸馏：自适应教师引导恢复负RL组梯度信号
authors:
- Zhuowen Han
- Jinwei Xiao
- Zhengxi Lu
- Renren Jin
- Zhiyuan Yao
- Yuxin Liu
- Hongyan Hao
- Yueqing Sun
- Yu Yang
- Qi GU
affiliations:
- TJUNLP Lab, Tianjin University
- Meituan Longcat Team
arxiv_id: '2608.00782'
url: https://arxiv.org/abs/2608.00782
pdf_url: https://arxiv.org/pdf/2608.00782
published: '2026-07-31'
collected: '2026-08-06'
category: Training
direction: RL训练优化 · 在线蒸馏 · 梯度信号修复
tags:
- GRPO
- On-Policy Distillation
- RLHF
- LLM Reasoning
- Advantage Asymmetry
- Token Selection
one_liner: 针对GRPO中全错样本的梯度消失，用教师置信度加权OPD并选择高价值token蒸馏，辅以正确轨迹SFT，修复学习信号。
practical_value: '- **识别负零方差prompt并施加额外监督**：在GRPO训练中，当一批采样全部错误（负零方差）时，梯度消失。可借鉴本文，仅在这类prompt上启用教师蒸馏或SFT，避免对所有数据盲目使用融合损失。

  - **教师置信度加权蒸馏信号**：在应用OPD时，用教师模型在该prompt上的平均成功率作为权重，缩放token级优势。对应到业务 Agent 训练，若用更大模型打分，可将其置信度作为信号强弱指示。

  - **高价值token选择性蒸馏**：仅对高学生熵或师生概率差异大的token进行蒸馏，减缓收敛到教师上限，保留RL探索空间。可迁移到推荐话术生成、搜索改写等任务，防止模型过早模仿强模型而丧失多样性。

  - **辅以SFT注入正梯度**：对负零方差prompt，额外用教师生成的正确答案做SFT，能缓解OPD的优势不对称问题。在实际应用中，对模型反复失败的困难样本，准备少量高质量示范轨迹能有效引导。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：
GRPO 因其简单高效被广泛用于LLM推理后训练，但当一组采样全部正确或全部错误时，优势为零，梯度消失，尤其是全错样本（负零方差prompt）完全失去学习信号。在线蒸馏（OPD）能提供稠密token级监督，但直接加和GRPO+OPD竟导致性能下降，因为：①并非所有样本都受益于蒸馏；②OPD会让学生过早收敛到教师水平，破坏RL的探索；③OPD的优势天然不对称，多数token获得负优势，压制学习。

**方法**：
提出RSTG，仅在学生而教师擅长的负零方差prompt上，自适应组合三种监督：
1. **教师置信度加权OPD**：用教师对该prompt的mean@8分数作为权重，缩放OPD优势，让更可信的教师引导更强。
2. **高价值token选择**：仅对学生熵高或师生概率差大的token施加OPD梯度，用Soft-OR分数选top-k%，减缓收敛，降低噪声。
3. **辅助SFT**：对负零方差prompt，用教师预生成的正确轨迹做SFT（等价于赋予每个token恒正优势+1），注入正梯度，缓解OPD优势不对称。

**实验**：
在数学（AIME24/25, MATH500, OLMPIAD）和代码（APPS, MBPP+）基准上，使用Qwen3-1.7B/4B→4B-2507 和 Qwen2.5-3B→14B 三对师生模型。RSTG对比GRPO+OPD在数学上平均提升+4.02%，代码+3.05%，大幅优于ReLIFT、RL-ZVP等baseline。训练曲线显示RSTG收敛更慢但最终性能更高，且避免了响应长度膨胀。消融证实每个组件不可或缺。

**关键结论**：精确地在“学生失败、教师成功”的位置进行蒸馏，既能恢复消失的梯度，又能防止过早吸收教师局限，是RL+蒸馏融合的正确打开方式。
