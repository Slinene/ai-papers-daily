---
title: 'PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction'
title_zh: PraMem：基于实践的经验记忆用于长程行为预测
authors:
- Zhuoqun Li
- Boxi Cao
- Jiawei Chen
- Hanshu Zhou
- Ruoxi Xu
- Guiping Jiang
- Ruotong Pan
- Tingting Gao
- Han Li
- Xiangyu Wu
affiliations:
- 中国科学院软件研究所
- 中国科学院大学
- 复旦大学
- 快手科技
arxiv_id: '2607.02881'
url: https://arxiv.org/abs/2607.02881
pdf_url: https://arxiv.org/pdf/2607.02881
published: '2026-07-02'
collected: '2026-07-07'
category: RecSys
direction: 长程行为预测·经验记忆演化
tags:
- Experiential Memory
- Long-horizon Prediction
- LLM
- User Modeling
- Self-review
- Practice-based Learning
one_liner: 将长历史序列化为练习样本，通过迭代试错构建可演化的模式经验与偏差警告，显著提升 LLM 长程行为预测准确性
practical_value: '- **化负担为资源**：把用户长行为序列当作带标签的实践样本，通过预测→反思→调整的闭环提炼经验。电商推荐中可用同样思路，利用历史行为数据持续优化用户画像，而不是只做一次离线建模。

  - **双重经验结构**：Pattern Experience 刻画用户偏好模式，Bias-alert Experience 显式警告模型容易犯的错误（如近因偏差、从众偏好）。在推荐系统的
  prompt 或知识库中可引入类似的“纠偏模块”，让 LLM 在推理时主动避开已知偏见。

  - **自审机制保证质量**：通过扰动历史序列检验提议的 groundedness，生成虚拟场景检验 generalizability，过滤不可靠的经验修改。生成式用户画像或动态
  prompt 优化中可以直接借鉴，防止模型拟合噪声或过拟合单一交互。

  - **共识驱动更新稳健**：由多个提议共同支持才修改记忆，避免偶然行为干扰。适用于实时更新用户状态的场景（如会话推荐、动态创意优化），可防止因单次异常交互导致画像漂移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
长程行为预测是推荐系统的核心问题，LLM 受限于隐性模式归纳困难和自身认知偏差（如近因偏好、从众倾向）。传统记忆管理（压缩、摘要、检索）仅减轻上下文负担，未直面这两大挑战。本文提出范式转变：把长历史视为可开采的资源，通过事先实践构建经验记忆，辅助 LLM 预测。  

**方法关键点**  
1. **经验记忆结构**：包含 Pattern Experience（用户行为模式）和 Bias-alert Experience（对 LLM 可能犯错的警报），用户专属且随时间演化。  
2. **迭代实践流程**：  
   - 现有经验测试：从历史中采样构造带标签的练习样本，LLM 在现有记忆下进行显式思考并预测，暴露不足。  
   - 反思性提议生成：对比预测与真实标签，生成修改/补充/修剪记忆的候选提议，经自审机制过滤后进入提议池。  
   - 共识驱动调整：每 T 轮集中处理提议池，仅采纳多个提议共同支持的操作，避免偶然行为干扰。  
3. **自审机制**：  
   - Groundedness review：扰动历史序列，若提议在扰动后仍成立则视为缺乏事实依据，滤除。  
   - Generalizability review：生成多个虚拟场景，若提议能唯一确定真实场景则说明过度特化，滤除。  
4. **训练无关**：全程用 LLM 进行，无需训练，可离线构建记忆，评估时跨不同 LLM 主干均有效。  

**关键结果**  
- 数据集：OmniBehavior（快手视频/直播/广告/电商）和 MovieLens-1M。  
- 基线：Long-context、Truncation、RAG、Summary、Mem0、MemOS、ProEx。  
- OmniBehavior 上，GPT-OSS-120B 主干下 PraMem ACC 达 84.7（Truncation 73.5），F1 达 31.6（Truncation 24.7），显著超越所有基线。Qwen3.5-35B-A3B 主干下同样大幅领先。MovieLens-1M 混淆矩阵对角线集中度明显优于基线，F1 达 49.6。  
- 消融：去除深层思考、反思提议、共识调整任一部件均导致性能下降；只保留 Pattern 或 Bias-alert 单一经验也变差；自审机制的两项检查均对最终效果有正向贡献。  

**核心洞察**  
“记忆”不应仅是压缩后的事实记录，而应是从历史中蒸馏出的可执行经验：既总结模式，又预判并警告认知偏差。这种双重经验记忆是让 LLM 胜任长程行为预测的关键。
