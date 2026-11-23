---
title: 'Hy-MT3: More Accurate, Robust and Practical Multilingual Translation Models
  in the Wild'
title_zh: Hy-MT3：更准确、鲁棒、实用的多语言翻译模型
authors:
- Mao Zheng
- Zheng Li
- Fangxu Liu
- Tao Chen
- Bingxin Qu
- Bo Lv
- Mingrui Sun
- Hongyu Li
- Hong Huang
- Jinlong Song
affiliations:
- Tencent Hunyuan Team
- Honor of Kings Team
arxiv_id: '2611.27673'
url: https://arxiv.org/abs/2611.27673
pdf_url: https://arxiv.org/pdf/2611.27673
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 多语言翻译大模型
tags:
- Multilingual Translation
- MoE
- LLM
- Evaluation
- Game Localization
- Image Translation
one_liner: 腾讯混元第三代多语言翻译模型，以3B激活参数覆盖102种语言，误译减少43%，并开源TransRubric评估套件
practical_value: '- 多语言商品信息本地化：Hy-MT3覆盖102种语言，指令跟随错误减少40%，可直接用于跨境电商商品标题/描述翻译，将品牌词、卖点、禁用词等用户约束转为显式指令，提升生成文案的忠实度与完整性。

  - 评估方法复用：TransRubric采用rubric-based自动评估，比传统指标更稳定且与人类评价相关性更高，推荐系统的query生成、推荐理由文案、广告标题生成等任务可借鉴其rubric设计，建立更可靠的离线评估体系。

  - 垂直领域优化：游戏本地化针对专业术语和风格构建高质量领域数据及专业评估系统，电商可类似地构建行业（美妆、3C）术语表和领域评估集，提升模型在垂直类目的表现；图像翻译中对OCR错误的容忍思路可用于电商商品图文字提取与翻译。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多语言翻译在真实场景中面临误译、遗漏/添加、不遵循用户约束等问题，语言覆盖有限，且高精度模型推理成本高。

**方法关键点**：Hy-MT3系列包含1.8B、7B、30B-A3B（MoE），在Hy-MT2基础上优化准确性、完整性和指令跟随；扩大语言覆盖至102种；针对游戏本地化，与王者荣耀团队合作构建高质量游戏领域数据和专业评估系统；针对图像翻译，改进上下文理解和错误纠正以容忍OCR错误；开源TransRubric自动评估套件。

**关键结果数字**：真实场景误译减少43%、遗漏/添加减少74%、指令跟随错误减少40%；Hy-MT3-30B-A3B仅3B激活参数在非思考模式所有评估模型中总体性能最佳，超越Qwen3.8-Max、Kimi-K3.1-Pro等，接近GPT-6.1-Sol等思考模型，超越推理计算>30倍的模型；游戏本地化核心指标匹配或超越Gemini 3.1 Pro；图像翻译同规模最佳；TransRubric在WMT26指标共享任务测试集上优于其他方案。
