---
title: 'From Plans to Pixels: Learning to Plan and Orchestrate for Open-Ended Image
  Editing'
title_zh: 从计划到像素：学习规划与编排以实现开放式图像编辑
authors:
- Anirudh Sundara Rajan
- Krishna Kumar Singh
- Yong Jae Lee
arxiv_id: '2605.15181'
url: https://arxiv.org/abs/2605.15181
pdf_url: https://arxiv.org/pdf/2605.15181
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 多模态图像编辑 · 奖励驱动的规划编排
tags:
- image editing
- planning
- orchestration
- reward learning
- vision-language judge
- long-horizon
one_liner: 通过基于奖励的规划-执行耦合，让模型自主学会分解并执行抽象多步编辑指令
practical_value: '- **电商商品图自动化**：可将“让图片更吸引素食者”这类抽象指令自动分解为替换肉类、添加植物元素、调整色调等子任务，并选择适当的修图工具（如背景移除、目标替换）逐步执行。

  - **RL + VL 判官范式**：借鉴用视觉语言模型（如 CLIP）作为奖励函数的做法，在创意生成、广告设计等场景中，将人类偏好量化为 VL 相似度或文本对齐分数，训练执行策略。

  - **规划器与执行器解耦**：规划器（生成步骤序列）与执行器（选择区域和工具）分离，可利用历史成功轨迹微调规划器，实现迭代改进；在电商多步素材生成中可类似分离“构思步骤”与“执行修图”。

  - **从演示学习转向体验学习**：避免手工规则或模仿教师，直接根据最终图像质量反馈来优化编排策略，这一思路可迁移到其他 Agent 系统，如对话式商品推荐中的多轮交互规划。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有图像编辑模型擅长单步修改，却难以应对“把这张广告变得更素食友好”这类开放式多步指令。此前基于 Agent 的方法虽能分解任务，但依赖手工管道或教师模仿，未能根据实际编辑结果优化，灵活性差。

**方法**：提出一种体验式长程编辑框架，由 Planner 将抽象指令分解为结构化的原子编辑步骤，Orchestrator 为每一步选择工具（如修补、更换背景）和操作区域。编辑后，一个视觉语言 Judge（如 CLIP）根据指令遵循度和视觉质量给出奖励。Orchestrator 通过强化学习最大化该奖励，无需人工标注。累积的成功轨迹再用于监督微调 Planner，形成“规划→执行→评判→反思”的闭环。

**结果**：在多种抽象编辑任务上，该方法生成的编辑序列比单步模型或基于规则的多步基线更连贯、更可靠，产生的图像更符合复杂指令的意图。消融实验证实了奖励驱动编排和 Planner 迭代优化的有效性。
