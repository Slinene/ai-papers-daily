---
title: 'YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family'
title_zh: YOLO-PEFT：目标检测器结构感知的参数高效微调框架
authors:
- Xu Lin
- WenJie Nie
- Jinlong Peng
- Weifu Fu
- YueXiao Ma
- Xiawu Zheng
- Yong Liu
affiliations:
- Tencent
- Xiamen University
arxiv_id: '2608.07051'
url: https://arxiv.org/abs/2608.07051
pdf_url: https://arxiv.org/pdf/2608.07051
published: '2026-08-06'
collected: '2026-08-11'
category: Training
direction: 检测器微调 · 结构化放置规划
tags:
- PEFT
- YOLO
- Object Detection
- Adapter Placement
- Constraint Planning
- LoRA
one_liner: 将适配器放置形式化为可审计的约束规划问题，在实时检测器上实现结构化 PEFT，避免手动试错
practical_value: '- 该方法将适配器插入点选择从人工试错转变为基于显式约束（算子类型、语义角色、图接口）的自动化规划，可借鉴到推荐系统的大模型微调中，例如在
  Transformer 推荐模型的不同层或位置上自动选择 LoRA/Adapter 模块，避免盲目尝试。

  - 规划时引入“可审计性”和“拒绝提议”机制，对于不合理的微调请求直接拒绝并给出原因，这一安全设计可推广至线上服务中模型的增量更新场景，防止灾难性遗忘或性能断崖。

  - 资源预算约束下的模块选择策略对于电商搜索模型的多变体部署（如不同类目、不同延迟要求）有帮助，可以生成满足 GPU 内存或延迟预算的一组适配器配置，降低管理成本。

  - 整个流程保持训练-保存-合并-导出路径，确保与标准推理部署兼容，这对实际业务中快速试验和上线至关重要，可参考其工程化流水线设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：实时检测器（如 YOLO）为适应新类目、领域、传感器等需要反复微调，全量微调存储和分发成本高。然而，源自语言模型的通用 PEFT 方法（如 LoRA）直接用于检测器时易失效，因为检测器计算图异构，包含算子、检测专用组件等，放置适配器存在严格约束，手动选择目标模块耗时且不可靠。

**方法关键点**：YOLO-PEFT 将适配器放置建模为一个约束规划问题。输入检测器图、PEFT 请求和资源预算，框架先为各节点分配算子角色和语义角色，然后基于四类谓词（算子有效性、检测语义、图接口、部署约束）逐模块检查，给出拒绝原因码，最终生成一组满足预算的目标模块列表，或直接拒绝（Refuse）以防止性能灾难。规划结果可审计、可执行，并保持完整的训练-保存-合并-导出路径。

**关键结果**：在 VOC07+12 数据集上，规划选出的 RS-LoRA 配置在 YOLO11s 上达到 0.7138 mAP50-95，YOLO12s 上 0.7307，而全微调分别仅为 0.6428 和 0.6662；在 RT-DETR-L 上，所有 LoRA 变体均超出灾难阈值，框架正确返回 Refuse，建议转为全量微调。YOLO11 可控实验显示 LoRA 微调峰值显存降低 43.9%，但训练时间延长 72%。框架在已评估的检测器家族内能替代手动试错，但对未知架构的拒绝可靠性仍待验证。
