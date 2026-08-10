---
title: 'Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits'
title_zh: 扩散大模型的安全机理漏洞：作为目标与攻击者
authors:
- Elena Dumitrescu
- Gert Lek
- Lydia Y. Chen
- Jérémie Decouchant
affiliations:
- Delft University of Technology
- University of Neuchâtel
arxiv_id: '2608.07430'
url: https://arxiv.org/abs/2608.07430
pdf_url: https://arxiv.org/pdf/2608.07430
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: 扩散LLM安全机理与攻击
tags:
- Diffusion LLMs
- Safety Alignment
- Jailbreak
- Neuron Pruning
- Black-box Attack
- Transfer Attack
one_liner: 发现扩散LLM安全对齐稀疏且可迁移，提出SN-Guided Diffusion黑盒越狱框架，以极低成本实现高转移攻击成功率
practical_value: '- 论文揭示的安全神经元稀疏性和跨架构可迁移性，可用于生成式推荐模型（如采用扩散LLM）的安全审计，识别并加固关键安全单元。

  - SN-Guided Diffusion 框架的黑盒、离线、低生成成本特性（仅需20次生成/提示），可借鉴其对电商推荐或Agent的安全性快速评估，无需访问模型内部即可检测越狱风险。

  - 安全神经元剪枝方法表明，少量神经元控制安全行为，可触发针对性的模型对齐测试，在推荐系统上线前作为红队测试手段。

  - 整体上虽然偏学术安全研究，但攻击思路可迁移：对扩散生成过程的引导损失设计，可能启发在可控文本生成（如广告文案）中绕过内容策略的攻防演练。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散大语言模型（DLLMs）采用并行去噪替代自回归生成，但其内部安全机制尚不明确。本工作同时将DLLMs作为攻击目标和攻击工具，系统暴露扩散对齐的机理漏洞。

**方法关键点**：
- 发现DLLMs的安全对齐稀疏且跨架构可迁移：从自回归模型初始化的DLLMs继承了源模型的安全神经元足迹，可直接进行安全神经元映射和剪枝。
- 自剪枝攻击：移除LLaDA和Dream中识别的少数安全神经元，攻击成功率（ASR）分别从2.6%升至73.8%、1.9%升至86.6%。
- 跨模型迁移剪枝：利用Qwen2.5的安全神经元剪枝，将Dream的ASR从1.9%升至73.2%，Fast-dLLM从7.0%升至86.3%。
- 提出SN-Guided Diffusion：完全离线的黑盒越狱框架，通过加权安全神经元损失将扩散过程导向远离安全触发区域，仅需每提示20次生成即可实现高转移ASR。

**关键结果**：
- 针对Llama-3-8B-Instruct转移ASR达77.1%，Qwen2.5-7B-Instruct达86.9%，Gemini-2.5-Flash-Lite达74.3%。
- 安全提示判别AUROC达1.0，对抗性提示与良性提示几乎完全可分。
- 与之前越狱方法相比，生成成本降低数个数量级，同时保持有竞争力的迁移性。
