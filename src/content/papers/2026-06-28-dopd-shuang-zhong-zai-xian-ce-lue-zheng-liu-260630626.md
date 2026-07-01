---
title: 'DOPD: Dual On-policy Distillation'
title_zh: DOPD：双重在线策略蒸馏
authors:
- Xinlei Yu
- Gen Li
- Qingyi Si
- Guibin Zhang
- Yuqi Xu
- Congcong Wang
- Shuai Dong
- Kaiwen Tuo
- Xiangyu Zeng
- Kaituo Feng
affiliations:
- NUS
- MMLab, CUHK
- PKU
- Explore Academy, JD
arxiv_id: '2606.30626'
url: https://arxiv.org/abs/2606.30626
pdf_url: https://arxiv.org/pdf/2606.30626
published: '2026-06-28'
collected: '2026-07-01'
category: Training
direction: 在线策略蒸馏·动态路由监督
tags:
- On-policy Distillation
- Privilege Illusion
- Advantage-aware Routing
- LLM Distillation
- VLM Distillation
one_liner: 提出优势感知双蒸馏，缓解特权信息导致的“特权幻觉”，动态路由教师与学生的token级监督
practical_value: '- 蒸馏中引入额外上下文（如用户特征、长期行为）时，需警惕特权幻觉：学生无法获取的输入会导致模仿不可达信号。可借鉴优势感知路由：根据教师与学生的优势差距动态选择监督来源，学生自身生成的部分用自我监督，避免能力与信息不对称混淆。

  - token级监督非均匀，优势高的token（如推荐理由中的关键词）承载关键能力。可仿照DOPD，对高优势token加强教师监督，低优token用学生自我蒸馏，提升训练效率与生成质量。

  - 框架适用于on-policy样本生成场景（如LLM生成推荐文案、解释），采样学生轨迹后，可同时运行特权教师和特权学生，按token概率比与优势差实时分配监督，工程上易集成至现有RLHF或蒸馏管线。

  - 实验中持续学习与分布外泛化提升明显，对推荐模型频繁更新的场景（如新品冷启、热点事件）有参考价值，能稳定性能并缓解灾难性遗忘。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
在线策略蒸馏（OPD）用学生自生成轨迹的密集token级信号进行知识迁移，提升压缩模型能力。引入特权信息（如更长上下文、多模态输入）可增强监督，但会导致特权幻觉——学生分不清哪些是应学的能力差距，哪些是因信息不对称而永远无法复制的模仿。token级监督本身也具有非均匀性，少量关键token承载核心能力。

**方法**  
提出DOPD，优势感知的双重蒸馏。运行特权教师（有额外输入）和特权学生（同样有额外输入，但结构与学生一致），对每个生成token计算两者的优势差距及概率比，动态选择监督来源：当教师优势大且学生概率低时，采用教师强监督；否则用学生自我监督或两者混合。不同token获得不同强度、目标和策略的监督，学生既能接收可信的能力信号，又避免过度模仿不可达的信息。

**结果**  
在LLM（Qwen3-8B→1.7B）和VLM（Qwen3-VL-8B→2B）蒸馏上，DOPD平均得分分别达58.4和65.2，显著超过Vanilla OPD（LLM 52.8, VLM 60.4）及ExOPD、Uni-OPD等变体。在稳定性、鲁棒性、持续学习和分布外任务上均表现更优，验证了缓解特权幻觉的有效性。
