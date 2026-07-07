---
title: 'ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster,
  Video, and Blog'
title_zh: 研究最后一公里自动化：从论文到海报、视频与博客的智能生成流水线
authors:
- Lingao Xiao
- Yalun Dai
- Yangyu Huang
- Qihao Zhao
- Wenshan Wu
- Hugo He
- Ruishuo Chen
- Jin Jiang
- Qianli Ma
- Jiahuan Zhang
affiliations:
- Microsoft Research
- National University of Singapore
- Nanyang Technological University
- Tsinghua University
- Peking University
arxiv_id: '2607.04438'
url: https://arxiv.org/abs/2607.04438
pdf_url: https://arxiv.org/pdf/2607.04438
published: '2026-07-04'
collected: '2026-07-07'
category: Other
direction: 多技能 Agent 组合与内容生成流水线
tags:
- content-generation
- agent-skills
- multimodal
- poster-automation
- video-generation
- blog-generation
one_liner: 将论文自动转化为可编辑的海报、视频与博客，通过共享提取器和硬性渲染门控保证可用性
practical_value: '- **共享上游解析器 + 可组合技能设计**：在电商场景中，可以复用同一套商品/内容分析结果，分别生成商品标题、详情文案、广告短视频脚本和直播口播稿，避免重复调用大模型，降低延迟与成本。

  - **硬性渲染门控保证产出可用**：生成推荐理由或广告语时，可引入格式校验（如字数、必含关键词）作为硬性检查点，避免产生无法直接上线的空泛描述。

  - **可编辑的中间产物**：生成推荐文案、商品标题时输出PPTX或DOCX等可编辑格式，便于运营人员二次修改，而非一次性渲染，保留人工干预入口。

  - **跨模态内容联动导航**：灵感可用于商品详情页，点击不同卖点段落时自动跳转至对应的讲解视频片段、图片位置或用户评价，提升交互体验。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：将论文手动制作成海报、演讲视频和博客的“最后一公里”仍效率低下。现有自动化方案各自为政，需反复解析论文，生成物多为一次性渲染，无法在PowerPoint或Word中再次编辑，且质量仅靠VLM偏好分评估，关键段落常为空泛。

**方法关键点**：提出基于技能组合的流水线ResearchStudio-Reel，包含五个Claude Code和Codex技能。核心是共享提取器`Paper2Assets`（一次性解析论文产出结构化资产），三个可编辑生成器`Paper2Poster`、`Paper2Video`、`Paper2Blog`分别生成符合打印标准的海报、同步演讲视频和双语博客，并通过硬性渲染门控（pass/fail检查）保证可用性；`Paper2Reel`交互层将所有产物整合进HTML，支持点击跳转联动。

**关键结果**：在Paper2Poster基准上，在审美与信息完整性各子项上均优于已有自动系统和单次调用前沿LLM，在两台独立VLM裁判下审美得分甚至超越作者手工制作的海报，整体胜出率达到84%-93%。能力审计表明，该流水线是唯一能输出所有三种可编辑产物的方案。
