---
title: 'Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity'
title_zh: 稀疏增量记忆：以稀疏性缩放线性RNN状态
authors:
- Loïc Cabannes
- Pierre-Emmanuel Mazaré
- Gergely Szilvasy
- Matthijs Douze
- Maria Lomeli
- Ilze Amanda Auzina
- Justin Carpentier
- Gabriel Synnaeve
- Hervé Jégou
affiliations:
- Meta FAIR
- Inria Paris & ENS-PSL University
- University of Tübingen
arxiv_id: '2607.07386'
url: https://arxiv.org/abs/2607.07386
pdf_url: https://arxiv.org/pdf/2607.07386
published: '2026-07-07'
collected: '2026-07-10'
category: Training
direction: 线性RNN稀疏状态扩展
tags:
- Sparse Delta Memory
- Linear RNN
- Gated DeltaNet
- Product-Key Memory
- Long-Context
- IsoFLOP
one_liner: 通过稀疏寻址将门控线性RNN的状态容量提升千倍，在等FLOPs下大幅改善长上下文检索和训练损失
practical_value: '- **长序列Agent的记忆压缩**：SDM用常量计算量维护大规模上下文状态，适合仍需多轮对话、长推理链的电商客服/购物助手Agent，避免KV
  cache爆炸，降低推理延迟。

  - **推荐系统长序列建模**：可替代Transformer的KV缓存来处理超长用户行为序列（如数万次点击），在固定显存下支持更长的交互历史，提升序列模型对长期兴趣的捕捉。

  - **可学习初始状态用于存储领域知识**：SDM将记忆的初始状态设为可学习参数，预训练后可携带通用常识（如商品品类关系），类似隐式的知识库，可迁移到生成式推荐模型的“记忆增强”模块。

  - **稀疏更新工程实现**：论文的chunk-wise并行训练与两指针合并求稀疏内积可在业务模型（如LLaMA类）中实现高效的大容量记忆层，适合需低成本接入长上下文的场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
线性注意力（如Mamba2、Gated DeltaNet）以固定状态大小和每token恒定计算量处理任意长度序列，但状态容量受限，在长上下文检索任务上大幅落后于softmax注意力。直接增大状态会线性增加计算量，无法实用。SDM旨在用稀疏读写打破这一瓶颈：在保持等FLOPs的前提下，将状态规模提升三个数量级，从而大幅改善线性RNN的长上下文能力。

**方法关键点**  
- **稀疏键选择**：基于Product-Key Memory将读写操作限制在少量slot上。对输入投影得到两个√N维向量，做外和得到N个slot分数，取top-W写入、top-R读取。计算复杂度仅O(√N·d + k²)，与N几乎无关。
- **门控Delta写入**：仅对被选中的W个slot执行遗忘门α_t和输入门β_t的gated delta更新，其余slot保持不变，更新公式与Gated DeltaNet一致。
- **稀疏读取**：用所选R个slot的状态加权求和得到输出。W和R均设为与密集GDN的dqk相同（64），以保证等FLOPs和参数量。
- **可学习初始状态M₀**：将大状态显存的第一帧设为可训练参数，使模型在预训练时植入知识，测试时可利用该静态记忆。

**关键结果**  
- 在1.4B和8B规模上，SDM在完全匹配参数和FLOPs的条件下，训练损失均显著低于GDN，8B时甚至优于Full Attention（2.253 vs FullAttn 2.285）。
- RULER长上下文基准：1.4B模型SDM平均accurary 31.2 vs GDN 20.0；8B模型50.2 vs 34.2，在多数子任务上接近或超过FullAttn（8B FullAttn平均61.2）。
- 消融证明：状态规模是主要性能驱动，即使去掉可学习初始状态仍大幅优于GDN；学习M₀在常识推理和代码NLL上带来额外增益。
- 内存分析显示读写分布自适应：写集中在top key，读更均匀，模型根据预算动态平衡。

**核心发现**  
通过稀疏化状态更新，线性RNN能在不增加FLOPs的前提下将记忆容量扩大千倍，使其长上下文检索大幅逼近甚至超越Full Attention，同时保留常数推理开销。
