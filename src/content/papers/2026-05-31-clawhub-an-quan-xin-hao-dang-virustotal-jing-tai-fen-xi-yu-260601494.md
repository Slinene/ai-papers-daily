---
title: 'ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector
  Disagree'
title_zh: ClawHub 安全信号：当 VirusTotal、静态分析与 SkillSpector 产生分歧
authors:
- Vincent Koc
- Patrick Erichsen
- Jacob Tomlinson
- Agustin Rivera
- Michael Appel
- Nir Paz
affiliations:
- OpenClaw Foundation
- NVIDIA
arxiv_id: '2606.01494'
url: https://arxiv.org/abs/2606.01494
pdf_url: https://arxiv.org/pdf/2606.01494
published: '2026-05-31'
collected: '2026-06-03'
category: Agent
direction: Agent 技能安全与扫描器分歧研究
tags:
- agent skills
- security scanning
- scanner disagreement
- skill governance
one_liner: 揭示 Agent 技能安全扫描器间高度分歧，提倡分层治理而非依赖单一扫描器放行/拦截
practical_value: '- 在电商 Agent 集成社区技能时，切勿依赖单一安全扫描器（如 Virustotal）做放行/拦截决策；应组合病毒扫描、静态分析、语义风险扫描等多维度信号，并预期扫描器间高质量分歧。

  - 设计分层安全治理：将自动化扫描作为信号输入，而非黑白判定；对打包可执行代码技能侧重恶意代码检测，对纯指令/工具调用技能侧重语义风险检测（如越权、提示注入）。

  - 若自建 Agent 技能市场或注册表，参考该数据集的分歧模式，构建「扫描结果 → 风险分 → 人工审核」的分诊流程，避免因单一扫描器漏报而引入恶意技能。

  - 可直接利用此公开的脱敏数据集训练面向技能安全分类的专用模型，作为电商 Agent 技能上线审核的辅助工具。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent 技能已成为 AI 智能体的可复用软件层，但其安全评估仍停留在孤立扫描，缺乏对扫描器间分歧的系统分析。该工作旨在揭示不同安全检测方法在真实技能数据上的交叉覆盖与盲区。

**方法**：基于 ClawHub 注册表中 67,453 个最新公开 OpenClaw 技能版本，构建脱敏数据集 ClawHub Security Signals。每行包含脱敏的 SKILL.md 内容、捆绑文件及自动判定结果，对比三类扫描器——VirusTotal（文件恶意代码声誉）、静态启发式分析、NVIDIA SkillSpector（语义代理风险提示）——的一致性与分歧。

**关键结果**：
- 扫描器重叠极低：任意两两扫描器的共同阳性技能不超过其合并阳性的 10.4%，仅 0.69% 的技能被三者同时标记；81.9% 的被标记技能仅由单一扫描器检出。
- 分歧按攻击面分化：SkillSpector 对“可疑”行（非恶意，共 25,504 行）的阳性率为 75.3%，但对“恶意”行（共 206 行）仅 6.8%；相反，VirusTotal 对恶意行的阳性率达 72.8%，符合打包代码中的恶意证据。
- 结论：Agent 技能安全需要分层治理，单一扫描器无法胜任。数据集以自动化注册判决为标签（白银标准），作为早期版本发布，鼓励进一步研究技能安全分类模型。
