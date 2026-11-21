---
title: 'The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception
  in Large Language Models'
title_zh: 谎言几何：用知识与人格方向检测大模型的欺骗
authors:
- Md. Abdullah Al Zami
- Suraiya Shanaz
- Mahdi Hasan
- Shoaib Ahmed Dipu
- Farig Yousuf Sadeque
- Md. Sabbir Ahmed
affiliations:
- Department of Computer Science and Engineering, BRAC University
arxiv_id: '2611.26545'
url: https://arxiv.org/abs/2611.26545
pdf_url: https://arxiv.org/pdf/2611.26545
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: LLM 欺骗检测 · 激活方向
tags:
- deception detection
- linear probe
- activation direction
- LLM safety
- role-play
- knowledge direction
one_liner: 在70B模型上验证无标签人格/知识方向检测谎言，发现对措辞敏感且跨模型不稳定
practical_value: '- 在电商客服/导购 Agent 场景，模型可能“隐瞒”已知的库存、优惠或售后政策，可借鉴无标签激活方向做轻量级实时监控：用诚实
  vs 欺骗角色对生成对比数据，取中间层激活差作为方向，无需标注数据即可得到廉价的欺骗信号。

  - 工程实现上，persona direction 只需前向计算两组角色 prompt 的中间层 hidden state 并做差，比有监督 linear probe
  更省标注成本，适合快速上线尝试；但论文显示其对回复措辞敏感，实际部署需在具体业务模型的中间层重新校准。

  - knowledge direction 提供了一种针对“知道但否认”的检测思路：对比模型可回答与无人可回答的问题，后接相同否认模板，若激活方向能分开两者，则可用于识别客服
  Agent 是否在能力范围内故意隐瞒信息。

  - 注意论文的负结果：跨模型迁移差，Qwen 上 persona 方向失效，且简单加和两个方向的收益不稳定。业务上不能直接当可靠检测器，建议作为辅助信号或与规则/检索结合。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：线性探针是最便宜的 LLM 谎言检测器，但往往难以跨谎言类型泛化。基于诚实与欺骗角色扮演的无标签方向尚未在 70B 规模、以及“知识谎”场景下验证——而知识谎中谎言与诚实否认可能措辞完全相同。

**方法**：在公开 persona bank 基础上加入“否认已知知识”角色及诚实对照；在模型中间层提取 persona direction。另设计 knowledge direction：对比模型可回答与无人能回答的问题，后接相同脚本否认，以分离“知道但否认”与“诚实不知”。在 Liars' Bench、Gender-Secret 等基准上测试 Llama-3.3-70B-Instruct、Qwen、Gemma、Mistral 四个模型。

**关键结果**：persona direction 在四模型中的三个上排序谎言优于单数据集探针，但 Qwen 失败，即使 Qwen 更常保持角色。Llama-3.3-70B 上它优于随机 persona bank，但相对公开方向的提升落在随机扩展范围内。知识谎场景中，persona direction 主要跟随回复措辞；knowledge direction 在两个模型上能分离相同措辞的谎言与诚实否认，一个勉强，一个不行，且结果部分依赖基准措辞。两方向相加在四个模型上排序谎言优于同深度有监督探针（一个近机会水平），但与 persona direction 相比无显著提升。更多样化的角色扮演问题对 Liars' Bench 无帮助。
