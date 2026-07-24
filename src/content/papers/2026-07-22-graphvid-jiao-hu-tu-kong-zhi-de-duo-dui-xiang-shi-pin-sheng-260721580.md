---
title: 'GraphVid: Interactive Graph-Controllable Video Generation'
title_zh: GraphVid：交互图控制的多对象视频生成
authors:
- Vedant Shah
- Onkar Susladkar
- Tushar Prakash
- Kiet Nguyen
- Tianjio Yu
- Adheesh Juvekar
- Muntasir Waheed
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
- Sony Research India
arxiv_id: '2607.21580'
url: https://arxiv.org/abs/2607.21580
pdf_url: https://arxiv.org/pdf/2607.21580
published: '2026-07-22'
collected: '2026-07-24'
category: Multimodal
direction: 结构化场景图控制视频生成
tags:
- Scene Graph
- Video Generation
- Diffusion Model
- Controllable Generation
- Image-to-Video
one_liner: 提出用可编辑场景图作为条件，实现精确多对象交互的图像到视频生成
practical_value: '- **商品互动视频生成**：在电商场景中，利用图关系描述商品之间的使用关联（如「手机–支付终端–用户」），自动化生成展示商品动态交互的营销视频。

  - **轻量可控生成框架**：冻结视频扩散骨干，仅训练图条件注入模块，大幅减少参数量和训练数据需求，能快速适配到特定领域（如试穿、3C 产品演示）。

  - **非专业用户交互设计**：通过拖拽编辑场景图节点和边，使无动画背景的用户也能生成多物体动态视频，降低内容制作门槛。

  - **可解释的条件控制**：图结构天然对应知识图谱，在推荐系统中可与商品图谱结合，实现可解释的「条件」推荐内容生成（例如按用户兴趣图谱生成个性化短视频）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：文本或轨迹控制难以精确描述多物体间交互，尤其在遮挡、重叠场景下轨迹绘制不精确且扩展性差。需要一种更直观、结构化的控制方式。

**方法关键点**：
- **图条件生成框架**：从输入帧自动构建场景图（实体+关系），用户通过交互式界面编辑图来指定期望的对象动态；编辑后的图编码为条件令牌，注入冻结的视频扩散模型（类似I2VGen-XL）的交叉注意力层。
- **数据集**：专门构建了GraphVid-Bench，包含大规模交互为中心的视频及结构化关系标注，支撑模型训练。
- **轻量设计**：仅训练图编码器和条件注入适配器，冻结扩散主干，显著降低训练成本和参数量。

**关键结果**：
- 相比Motion-I2V，FID降低39.9%，FVD降低37.6%，PSNR从9.87升至15.98，SSIM从0.38升至0.61。
- 使用更少训练数据与参数，即达到更强可控性和视频质量。
