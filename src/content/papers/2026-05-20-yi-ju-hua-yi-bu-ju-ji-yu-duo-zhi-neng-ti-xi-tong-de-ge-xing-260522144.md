---
title: 'One Sentence, One Drama: Personalized Short-Form Drama Generation via Multi-Agent
  Systems'
title_zh: 一句话，一部剧：基于多智能体系统的个性化短剧生成
authors:
- Yufei Shi
- Weilong Yan
- Naixuan Huang
- Yucheng Chen
- Chenyu Zhang
- Tao He
- Si Yong Yeo
- Ming Li
affiliations:
- Nanyang Technological University
- National University of Singapore
- Beijing Institute of Technology
- Tsinghua University
- University of Electronic Science and Technology of China
arxiv_id: '2605.22144'
url: https://arxiv.org/abs/2605.22144
pdf_url: https://arxiv.org/pdf/2605.22144
published: '2026-05-20'
collected: '2026-05-22'
category: MultiAgent
direction: 多智能体短剧生成与3D空间一致性
tags:
- MultiAgent
- Short-Drama Generation
- 3D Grounding
- Spatial Consistency
- Narrative Pacing
- Video Generation
one_liner: 层次化多智能体框架将单句创意转为完整短剧，融合多智能体辩论、3D锚定首帧与多阶段评审，实现叙事节奏、空间一致性与制片质量协同优化。
practical_value: '- 多智能体辩论与多阶段评审循环的设计可直接借鉴到电商/Agent场景的复杂内容生成（如商品创意脚本、虚拟主播对话），通过独立评委评比与局部修正提升输出质量，避免全盘重生成。

  - 3D场景锚定与共享坐标系维持空间一致性的思路，可迁移至虚拟试穿、虚拟直播间的商品展示一致性，用简单3D重建约束多帧生成，防止物品漂移。

  - 检索增强的剧本原子库（Pattern Bank、Logic Bank）为个性化推荐解释或创意生成提供了一种结构化知识复用模式，尤其适合高频、强节奏的内容创作。

  - 但整体偏视频生成，与推荐、Agent优化的核心业务直接耦合度较低，价值主要在生成式内容的工程化与质量控制思想。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前短剧生成流水线多采用一次性LLM输出脚本，缺乏对短剧特有的快节奏钩子、密集反转、空间一致性与制片质量控制，导致叙事弱、空间漂移、需大量人工修正。本文提出“One Sentence, One Drama”框架，仅凭用户一句创意，自动生成完整短剧视频，解决叙事节奏、空间漂移和内容可信度三重挑战。

### 方法
- **多智能体辩论式故事生成**：从约300部高分短剧脚本构建原子剧本库（Pattern Bank、Logic Bank），通过事实、逻辑、模式三路检索注入，再由三位LLM独立评审、GPT-5.4 Pro裁决、局部改写，显式强化开场钩子、冲突升级、结尾悬念；废弃创意存入Idea Bank以备恢复。
- **3D锚定首帧生成**：为每一场景生成360°全景图并重建3D场景，注册生成的首帧和角色网格到同一坐标系；下一镜头首帧通过几何-语义双过滤的相机采样、角色条件生成及VLM修复，保持跨镜头空间一致。
- **多阶段评审循环**：在提示、关键帧、视频三个阶段分别检查空间合理性、物理合理性、道具连续性和动作连续性，自动触发局部修正。
- **转场与BGM**：基于时空与人物运动选择直切、文字叠化、空镜或运动桥接转场；从8122首BGM中按16个功能桶，由LLM选曲、GPT-Audio评分，并做对话感知的动态混音。

### 实验
在自建**Short-Drama-Bench**（50条提示，7大类17子类，共239分钟生成视频）上对比了MovieAgent、ScriptAgent、StoryMem、Toonflow、Xiao Yun Que。方法在开场钩子(4.26 vs 3.86)、结尾钩子(3.75 vs 3.66)、叙事连贯性(4.62 vs 4.21)等指标均优势显著；消融实验证实多智能体辩论、3D首帧、多阶段评审、转场BGM四个模块各自独立贡献。人工评分亦全面领先。

**最值得记住的一句话**：单句创意到完整短剧，靠的不是更大的生成模型，而是结构化分解、3D空间锚定与多智能体闭环评审的组合拳。
