---
title: Transferring the Intelligence of VLMs to Robotic Control
title_zh: 将视觉语言模型智能迁移至机器人控制
authors:
- Meng-Hao Guo
- Zhe-Han Mo
- Jia-Jun Wang
- Yi Zhang
- Kejin Wang
- Yi-Xuan Deng
- Jia-Peng Zhang
- Yongming Rao
- Shi-Min Hu
affiliations:
- Tsinghua University
- Tencent Hunyuan
arxiv_id: '2609.22966'
url: https://arxiv.org/abs/2609.22966
pdf_url: https://arxiv.org/pdf/2609.22966
published: '2026-09-18'
collected: '2026-09-23'
category: Agent
direction: VLM Agent 闭环控制机器人
tags:
- VLM
- Robotic Control
- In-Context Learning
- Zero-shot
- Embodied Agent
- Discrete Actions
one_liner: 通过离散动作接口与闭环 ICL，使 VLM 零/单样本控制机器人并达 SOTA
practical_value: '- **离散动作接口设计**：将连续控制空间抽象为紧凑离散命令集，让 LLM/VLM Agent 通过标准化 API 控制底层系统（如推荐引擎参数、广告出价），提升决策稳定性和可解释性。

  - **In-context learning 快速适配**：用 1-2 个演示示例让通用大模型零样本/小样本适配新任务（如新品类推荐策略、活动文案风格），避免每任务微调，降低迭代成本。

  - **闭环反馈框架**：借鉴“观察-推理-执行-观察”闭环，构建自主优化 Agent，例如在实时推荐中根据用户行为反馈动态调整排序策略，而非静态输出。

  - **通用模型知识迁移**：论文显示通用 VLM 零样本可超越任务专用策略，启示业务中可优先用通用 LLM 处理非核心子任务（如 query 改写、解释生成），再决定是否投入专门训练。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：人类智能能在数字与物理世界间迁移，VLM 的智能是否也能从数字世界泛化到物理世界用于机器人控制？

**方法**：提出 RoboDawn，一个人类直觉接口，将机器人控制抽象为离散的平移、旋转和夹爪命令，让 agentic VLM 闭环控制机器人。VLM 观察当前视觉状态，推理下一步动作，执行并根据新状态调整后续决策。引入 in-context learning (ICL)，用少量演示让 VLM 快速掌握接口使用和任务解决策略。

**关键结果**：在 RoboTwin 2.0 C2R 和 RoboDojo 上无需任务特定机器人训练，零样本已超过多个专门训练的强策略；单样本演示进一步提升，达到 SOTA。RoboTwin 2.0 C2R 成功率从 53.2% 提升到 73.6%（对比基线 π0.5 为 46.0%），RoboDojo 从 35.67% 提升到 47.17%。框架迁移到 Franka 真实机器人，完成 block-in-basket 和 block stacking 任务。
