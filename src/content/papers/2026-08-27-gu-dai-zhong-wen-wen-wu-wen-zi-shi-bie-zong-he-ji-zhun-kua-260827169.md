---
title: 'Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script
  Benchmark for Ancient Chinese Artifact Text Recognition'
title_zh: 古代中文文物文字识别综合基准：跨千年、多媒介、多书体
authors:
- Hiuyi Cheng
- Nuo Xu
- Yuyi Zhang
- Xuhan Zheng
- Wei Pan
- Jing Zhang
- Dezhi Peng
- Minghui Liao
- Yihua Teng
- Jihao Wu
affiliations:
- South China University of Technology
- Huawei Technologies Co., Ltd.
arxiv_id: '2608.27169'
url: https://arxiv.org/abs/2608.27169
pdf_url: https://arxiv.org/pdf/2608.27169
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: 古代文字识别基准与模型评估
tags:
- OCR
- Benchmark
- Ancient Chinese
- Vision-Language Models
- Document Recognition
- Evaluation
one_liner: 构建2700张古代中文文物图像基准，覆盖三千年文字演变、九类媒介与七种书体，评估VLM与OCR专家模型并揭示未解难题
practical_value: '- 对电商商品详情图、包装图上的长尾字体、异体字、艺术字识别场景有直接警示：通用 VLM 在低频字符和特殊符号上幻觉严重，生产环境应结合
  OCR 专家模型或规则兜底。

  - 论文的符号标准化、字符标准化、解析标准化三套标注规范可迁移到电商多源异构数据（如商品吊牌、质检报告、广告图）的评估集构建，统一不同媒介的标注口径。

  - 评估思路值得借鉴：在同一基准上对比通用 VLM 与 OCR 专家模型，能快速定位业务中识别任务的模型选型与能力边界。

  - 主要面向文化遗产数字化，业务可借鉴点有限；若业务涉及古籍、印章、书法等垂直领域，该基准可作为预训练或微调前的领域能力测试。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：古代中文文物文字识别是文化遗产数字化的基础，但现有基准碎片化严重，时间跨度、媒介类型、书体覆盖均不完整。

**方法关键点**：Ancient-Bench 包含 2700 张古代中文文物图像，围绕三个维度构建：Millennial 跨 3000 年文字演变、Multi-medium 覆盖九类文物（如甲骨、青铜、简牍、印章等）、Multi-script 覆盖七种历史书体。为适配异构媒介的公平评估，定义了符号标准化、字符标准化、解析标准化三类标注标准。

**关键结果**：在 Ancient-Bench 上对通用视觉语言模型（VLM）和 OCR 专家模型进行广泛实验，显示古代中文文物文本识别仍远未解决，异体字、专用符号和幻觉是持续挑战。
