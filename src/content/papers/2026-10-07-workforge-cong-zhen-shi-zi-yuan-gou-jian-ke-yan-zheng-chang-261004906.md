---
title: Scaling Verifiable Environments for Long-horizon Work Agents
title_zh: WORKFORGE：从真实资源构建可验证长程工作智能体环境
authors:
- Jiazheng Zhang
- Long Ma
- Yunxian Yang
- Zhiheng Xi
- Zhikai Lei
- Yajie Yang
- Chenyang Liao
- Enyu Zhou
- Yang Nan
- Yuchen Tian
affiliations:
- Tencent
- Fudan University
arxiv_id: '2610.04906'
url: https://arxiv.org/abs/2610.04906
pdf_url: https://arxiv.org/pdf/2610.04906
published: '2026-10-07'
collected: '2026-10-15'
category: Agent
direction: Agent 长程工作环境合成与训练
tags:
- Work Agents
- Environment Synthesis
- Verifiable Supervision
- Long-Horizon
- SFT
- Scaling
one_liner: 提出 WORKFORGE，从真实工作资源合成可验证环境并生成训练轨迹，大幅提升长程智能体能力
practical_value: '- 业务中构建 agent 训练/评测环境时，优先使用真实业务文件（报表、素材、SOP、数据表等）而非 LLM 合成，保留真实噪声和跨文件依赖，能显著提升
  agent 在真实任务上的泛化。

  - 采用「专家 workflow blueprint → 资源检索 → workspace profiling → 任务+验证器生成」流水线，把专家经验变成可复用模板，批量产出带隐藏解法和双验证器的训练样本。

  - 用 workspace 可观察事实锚定任务规格与验证标准，避免 LLM judge 产生无依据的评分要求；轨迹筛选时混合 programmatic + semantic
  分数，优于单一验证。

  - 数据量和交互轮数均呈现 scaling 收益：优先收集长轨迹（41-60 轮 > 0-20 轮），训练序列长度放至 256K 并保留每轮 assistant
  loss；训练与评测 harness 对齐可带来额外提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
手工构建专业工作 agent 环境代价极高，难以扩展；现有自动合成方法往往牺牲 workspace 复杂度、真实性或可验证性。真实专业工作依赖多文件依赖和可观察工作区证据，训练代理需要可信、可验证的监督信号。

**方法关键点**
- 四阶段流水线：①工作流规格：专家把领域工作流沉淀为 Scene Blueprint，定义资源、决策、交付物；②环境合成：检索真实资源构建 workspace，并通过 profiling 提取文件角色、依赖和可观察事实；③任务生成：基于 workspace facts 生成任务指令和隐藏解方案，同时设计 programmatic verifier（检查确定性需求和 workspace 状态）与 semantic LLM judge（评估开放式交付物）；④轨迹生成：solver agent 执行任务，得到带评分的交互轨迹。
- 核心原则：可观察 workspace facts 同时锚定任务构建与验证，防止 judge 产生幻觉性要求。
- 数据规模：16.7K 环境，覆盖 40 个专业域、60 种文件类型，平均 workspace 含 42.3 个文件、279KB，平均轨迹 31.8 步、76.5K tokens。

**关键实验**
- 在 Qwen3.5-35B-A3B-Base 上 SFT，GDPval 从 45.5 提升至 73.6（+28.1），APEX 从 5.0 提升至 21.3（+16.3），WildClaw/ClawEval/ALE 也有显著提升。
- WorkForge-27B 将 Qwen3.5-27B 的 GDPval 提升至 82.4，超过 Qwen3.5-397B-A17B（79.7），接近 Claude Opus 4.8 和 GPT-5.6。
- 消融显示：混合验证优于单一验证；真实 workspace 比 LLM 合成 workspace 文件数多 5.4 倍、文件类型多 2.4 倍；训练轨迹长度越长，模型在长程任务上表现越好。

**最值得记住的一句话**
可验证的专业工作环境必须根植于可观察的 workspace 事实，这是任务生成与验证的共同锚点。
