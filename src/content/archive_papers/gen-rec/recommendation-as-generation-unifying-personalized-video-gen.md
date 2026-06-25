---
title: 'Recommendation as Generation: Unifying Personalized Video Generation and Recommendation
  at Industrial Scale'
authors: Yanhua Cheng, Bo Wang, Haotian Zhang, Xinyuan Gao, Zhihui Yin, et al. (20
  人)
date: 2026-06
venue: arXiv
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: 提出推荐即生成(RaG)范式，通过解耦语义ID(D-SIDs)统一推荐与视频生成，利用视频生成Agent协作规划和SCRL跨域奖励学习闭环优化，在广告场景增收5.46%。
paperUrl: https://arxiv.org/abs/2606.25496
codeUrl: null
tags:
- Recommendation As Generation
- Disentangled Semantic IDs
- Video Generation Agents
- Synergistic Cross-Domain Reward Learning
- Industrial Scale
unverified: true
---

## 核心思路
将推荐从检索固定视频池转变为基于用户兴趣直接生成个性化视频，用解耦语义ID（D-SIDs）作为统一接口，驱动GRM预测兴趣SIDs，IM和VGAs可控生成视频，并通过SCRL闭环优化质量、对齐和用户反馈，实现工业级增收。

## 整体实现思路
端到端Pipeline：
```
用户上下文 → GRM预测content+creative SIDs → IM将SIDs+可选元数据转为生成指令 → VGAs (视觉规划Agent → 音频对齐Agent → 特效增强Agent，含反思循环≤2次) 生成视频 → 基于用户反馈/质量/对齐奖励的SCRL优化整个框架
```

## 子模块实现（可复现细节）

### 1. 解耦语义视频编码器 (Disentangled Semantic Video Encoders)
**输入**: 视频v，含视觉帧、标题/OCR/ASR等。

**处理**:
1. 视觉编码：Qwen2.5-VL-7B-Instruct视觉编码器提取视觉token序列 $H \in \mathbb{R}^{N\times d}$。
2. 生成解耦文本描述：内部密集描述模型CapModel生成内容描述 $D_{content}$ (实体、主题)和创意描述 $D_{creative}$ (风格、节奏、氛围)。
3. 文本编码：通过Qwen2.5-VL文本tokenizer得到 $Q_m \in \mathbb{R}^{L_m\times d}, m\in\{content,creative\}$。
4. 多模态融合：将 $H$ 和 $Q_m$ 输入Qwen2.5-VL-7B-Instruct，取最后一层最后token的hidden state池化，L2归一化得 $z_m \in \mathbb{R}^d, \|z_m\|_2=1$。
5. 训练目标：
   - 对比损失(每模态): $\mathcal{L}_m = -\log\frac{\exp(sim(z_i^m, z_j^m)/\tau)}{\sum_k \exp(sim(z_i^m, z_k^m)/\tau)}$，$z_j^m$为正对。
   - 正交损失: $\mathcal{L}_{orth} = \|z_{content}^T z_{creative}\|_2^2$。
   - 总损失: $\mathcal{L} = \mathcal{L}_{content} + \gamma_1 \mathcal{L}_{creative} + \gamma_2 \mathcal{L}_{orth}$。
6. 离散化为SIDs：对每个 $z_m$ 独立应用残差量化K-Means (RQ-KMeans, 层数 $L=4$, 每层码本大小8192)，得到离散代码序列 $s_m^{1:L}$ 和量化嵌入 $e_m = \sum_{l=1}^{L} c_l^m(s_l^m) \approx z_m$。拼接为 D-SIDs = $[s_{content}^{1:L}; s_{creative}^{1:L}]$，共 $2L$ token。

**超参**: $\gamma_1,\gamma_2$ 未公开；VLM冻结或微调未详；RQ-KMeans的 $L=4$，码本8192。

### 2. 生成式推荐模型 (Generative Recommendation Model, GRM)
**输入**: 用户上下文 $c_{user}$ (静态属性+行为序列)，目标item的prefix SID序列 $[BOS, s_{content}^1, s_{content}^2, s_{creative}^1, s_{creative}^2]$ (实际 $L$ 可能为2)。

**架构**: 类似GR4AD[27]。每个SID token通过稀疏嵌入表映射为768维向量，送入7层LazyDecoder (hidden 768, FFN 3072, heads 12, vocab 8192)，使用FlashAttention。

**训练**: 自回归预测完整D-SIDs序列，token级交叉熵损失；8 GPUs, batch size 8192, Adam lr=1e-4。后续加GDPO强化学习微调。

**推理**: 波束搜索beam=512，吞吐130 QPS。

**输出**: 预测的D-SIDs序列。

### 3. 指令模型 (Instruction Model)
**输入**: GRM预测的D-SIDs和可选元数据 $D_{meta}$ (产品信息等，缺失则mask)。

**处理**:
1. 重构连续嵌入：将离散SIDs通过RQ-KMeans量化嵌入求和得 $e_{content}, e_{creative} \in \mathbb{R}^d$，拼接为 $e_{D\text{-}SIDs} \in \mathbb{R}^{2\times d}$，经可学习投影层 $\phi$ 映射到LLM嵌入空间：$h_{D\text{-}SIDs} = \phi(e_{D\text{-}SIDs}) \in \mathbb{R}^{2\times d'}$。
2. 元数据编码：LLM tokenizer产生 $Q_{meta} \in \mathbb{R}^{L_{meta}\times d'}$。
3. 自回归生成指令：$\hat{D}_{inst} = LLM(h_{D\text{-}SIDs}, Q_{meta})$ (基础模型Qwen3-8B，$d'$ 为LLM hidden size)。
4. 监督信号：利用Gemini2.5 Pro对视频生成shot级脚本 $D_{inst}$ 作为目标。
5. 损失：$\mathcal{L}_{NTP} = -\sum_{t=1}^{L_{inst}} \log P(y_t | y_{<t}, h_{D\text{-}SIDs}, Q_{meta})$。

**三阶段训练**: (1) 冻住LLM，仅训练投影层；(2) 联合微调投影层和LLM；(3) 引入SCRL强化学习。

### 4. 视频生成智能体 (Video Generation Agents, VGAs)
**共享主干**: Qwen2.5-32B，三个角色共享参数，仅通过状态 $S_t$ 中的 $\text{PROMPT}_{role}$ 和attention mask区分工具。

**序列化状态**: $S_t = [\hat{D}_{inst}; D_{tool}; O_{<t}; \text{PROMPT}_{role}]$，其中 $D_{tool}$ 为工具描述，$O_{<t}$ 为前序智能体的输出累积。

**三个子智能体**:
1. **视觉规划(VPA)**: Prompt=$\text{PROMPT}_{visual}$，输出 $I_{visual}$ (片段级故事板、布局、时间边界)。
2. **音频对齐(AAA)**: Prompt=$\text{PROMPT}_{audio}$，$O_{<t}$ 追加VPA输出，输出 $I_{audio}$ (时序对齐的语音、音乐)。
3. **特效增强(AEEA)**: Prompt=$\text{PROMPT}_{effect}$，$O_{<t}$ 追加AAA输出，输出 $I_{effect}$ (字幕、视效、CTA)。
最终视频 $V = G(I_{visual}, I_{audio}, I_{effect})$。

**反思循环**: 整个流程执行后，可进行最多2次反思再规划(Observe→Think→Act)。

**KV-Cache复用**: 因状态前缀追加式增长，下游智能体仅编码自己的 $\text{PROMPT}_{role}$，大幅降低推理延迟(单次生成约180秒，见表5)。

**训练**: 智能体策略 $\pi_{\theta}$ 通过SCRL的GDPO优化，奖励信号涵盖质量、对齐和用户反馈。

### 5. 跨域协同奖励学习 (Synergistic Cross-Domain Reward Learning, SCRL)
**奖励组成**:
- 视频质量 $R_{quality} = R_{visual} + R_{audio} + R_{effect}$，分别评估视觉美学、音画同步、特效对齐，由各自奖励模型(Transformer)给出。
- 兴趣对齐 $R_{align} = R_{instr\text{-}align} + R_{rep\text{-}align}$，分别度量GRM SIDs与指令、与生成视频的语义相似度。
- 用户反馈 $R_{feedback} = R_{real} + R_{pred}$，融合真实交互与排序模型预估。

**约束优化 (GDPO)**:
- 主目标: 用户反馈；约束: $R_{align} \ge \tau_a$, $R_{quality} \ge \tau_q$。
- 复合奖励: $R(y_i) = R_{feedback}(y_i) - \sum_{c\in\{a,q\}} \lambda_c(t) \cdot \text{ReLU}(\tau_c - R_c(y_i))$。
- 阈值校准: $\tau_c = \mu_{base} + k_c \sigma_{base}$，$k$值：VGAs严格($k_a=k_q=1.1$)，IM适中($k_a=0.8$)，GRM宽松($k_a=0.3$)。
- 组解耦归一化: 候选集 $Y$ 内，$A_i = \frac{R(y_i) - \mu(Y)}{\sigma(Y) + \epsilon}$。
- 优化目标: $\mathcal{L}_{GDPO} = -\mathbb{E}_{(x,y_i)} \left[ A_i \cdot \log\frac{\pi_{\theta}(y_i|x)}{\pi_{ref}(y_i|x)} \right]$，加上裁剪和KL正则。
- $\lambda_c(t)$ 用PID控制器更新。

## 实验设置与结果

### 在线A/B测试 (表1)
- 平台：快手广告系统，>4亿DAU；基线：生产DLRM、GRM。
- 指标：广告收入提升百分比。

| 方法 | 相对DLRM提升 | 相对GRM提升 |
|------|---------------|-------------|
| GRM | +3.526% | - |
| GRM + D-SIDs | +4.460% | +0.902% |
| 全系统RaG (GRM+D-SIDs+IM+VGAs+SCRL) | +5.462% | +1.870% |

### 离线消融

#### D-SIDs质量 (表2)
- 语义检索R@1/5/10：0.896/0.985/0.994，超越Qwen2.5-VL-7B +16.5% R@1。
- 离散化：压缩失真1.02，碰撞2.62%，优于QARM (1.14/18.24%)。

#### 指令模型配置
- 8B 1M样本：解码保真度0.8096；32B 1M：0.8212；折中采用8B 1M。

#### VGAs vs 工作流基线 (表3)
| 指标 | 工作流基线 | VGAs | 提升 |
|------|------------|------|------|
| 自动化评分均值/中位数 | 62.4/62.0 | 71.3/76.0 | +14.3%/+22.6% |
| 自动化胜率 | 28.7% | 70.1% | +41.4pp |
| 用户研究胜率 | 34.4% | 52.9% | +18.5pp |

#### 奖励消融 (表4)
- 质量收益：单独视觉+21.4pp、音频+24.0pp、特效+18.6pp；联合+18.7pp (至56.0%自动化胜率)。
- 增加对齐奖励：对齐分数从0.707→0.828 (+17.1%)。

## 思考与可参考价值

### 局限性
- VGAs单次生成约180秒，仅适合近线，无法实时服务。未来需蒸馏加速。
- 奖励模型依赖LLM判定，可能与评估标准重叠，存在过拟合风险。
- 依赖内部工具链和专属码本，迁移需重建。
- 仅验证广告场景，泛化性待探索。

### 可借鉴点
- 推荐与生成共享解耦语义ID，可应用于电商商品图/文案生成。
- Agent分层规划、反思循环与KV-Cache复用降低推理成本，适合自动化广告素材生成。
- SCRL的PID控制多目标约束优化，适合工业界多目标排名与质量权衡。
- 分离部署（在线兴趣推断+近线批量生成+缓存策略）为推荐系统引入生成能力提供现实架构。
