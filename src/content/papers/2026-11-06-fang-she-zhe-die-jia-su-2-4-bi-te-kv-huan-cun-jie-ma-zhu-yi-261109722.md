---
title: 'FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through
  Affine Folding'
title_zh: 仿射折叠加速 2/4 比特 KV 缓存解码注意力
authors:
- Donglin Zhuang
- Pragaash Ponnusamy
- Xiaoxia Wu
- Shuaiwen Leon Song
- Zhongzhu Zhou
affiliations:
- Together AI
- University of Sydney
arxiv_id: '2611.09722'
url: https://arxiv.org/abs/2611.09722
pdf_url: https://arxiv.org/pdf/2611.09722
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM 推理加速 · KV cache 量化
tags:
- KV cache
- quantization
- GPU kernels
- LLM inference
- affine folding
- attention
one_liner: 将 KV cache 的 scale 和 offset 从逐值反量化折叠到矩阵乘输入或输出，降低指令 issue 瓶颈，提升低比特解码速度
practical_value: '- 线上 LLM 推理服务（如电商商品描述生成、广告文案、Agent 多轮对话）引入 2-bit/4-bit KV cache
  时，不能只看 HBM 流量节省，必须评估逐元素反量化对指令 issue 的占用；优先选择将 scale/offset 折叠到矩阵乘输入或输出上的 kernel
  方案。

  - 在 Blackwell/B200 上，per-value reconstruction 的指令需求可能超过硬件 issue 峰值，导致 INT2/4 量化
  kernel 反而慢于原生 FP8/FP4；部署时可以优先测试 FOSCAR 这类 folding kernel，或参考其思路自研。

  - 直接利用 packed integer 位模式构造 Tensor Core 操作数（如 Blackwell 上 INT2→FP4 只需 0.19 ALU/element），能大幅降低
  ALU 指令数；在自研 CUDA kernel 或集成 SGLang/vLLM 时，可借鉴这种 bit-level 构造和预计算 s'', z'' 的补偿方式。

  - 长上下文场景（RAG、多轮 Agent、长商品列表/评论摘要）中 KV cache 内存压力大，FOSCAR 结合 OSCAR 等量化策略可将 2-bit
  配置的峰值聚合吞吐提升 170%（B200）且精度几乎无损，适合作为长上下文 LLM serving 的加速后端。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
低比特 KV cache 存储（2-bit/4-bit）能直接减少 decode 阶段从 HBM 读取的数据量，但现有 kernel 在送入 Tensor Core 前仍需逐元素反量化（应用 scale 和 offset），消耗大量指令 issue 槽位。测量显示，H100/B200 上现有 2-bit 融合 kernel 仅达到峰值 HBM 吞吐的 31%/15%；原因是 B200 上 INT2 逐元素重建所需的指令 issue 需求已超过硬件峰值。这说明单纯压缩内存带宽并不自动转化为 latency 收益，瓶颈转移到指令 issue。

## 方法关键点
- **affine folding**：将量化组的共享 scale 和 offset 从逐元素操作中移出，按量化轴选择折叠方向。token-wise K 使用 acc-fold（先做无缩放的部分 QK，再乘 scale，加 offset×query sum）；channel-wise K 使用 operand-fold（先缩放 Q 再加 offset 修正）；V 同理。两种方式都在精确算术下等价于逐值反量化。
- **bit-level 操作数构造**：直接利用 packed integer 位模式生成 Tensor Core 操作数，避免显式 int→float 转换。Hopper 上采用 mantissa injection 产生 BF16 y=q+128，Blackwell 上直接低位放置生成 FP4/FP8 y=q/2 或 q·2⁻⁹；通过预计算 s'=s/α, z'=z-βs' 补偿映射差异。
- **warp-specialized pipeline**：Hopper 上 1 个 producer + 2 个 consumer warpgroups 交替处理奇偶 KV tile；Blackwell 上分离 TMA copy、tcgen05 矩阵发射、operand 准备、softmax、输出修正到不同 warpgroups，共享内存和 TMEM 传递中间结果。

## 关键实验
- Kernel benchmarks：H100 上 FOSCAR INT2/INT4 对 FlashInfer BF16 几何平均加速 3.36×/2.83×，对 TensorRT-LLM FP8 为 2.03×/1.71×；B200 上对 BF16 2.67×/2.30×，对 FP8 1.48×/1.28×，对 NVFP4 1.16×/1.00×。INT2 有效 KV 访问吞吐达到 H100 峰值的 91.3%、B200 的 44.4%，远超 baseline。
- 精度：与 BF16 decode 比较，INT2 的 L2 误差主要来自量化本身（0.52–0.61），kernel 算术误差仅 1.68–1.76×10⁻³，与 BF16 匹配；服务 Qwen3-8B 的 GPQA-Diamond 和 GSM8K 准确率无显著差异。
- Serving：Qwen3-8B 100K 输入/1K 输出，99% prefix cache hit 时，FOSCAR INT2 峰值聚合吞吐 H100 达 506 tok/s（较 OSCAR INT2 +88%，较 BF16 +341%），B200 达 897 tok/s（较 OSCAR +170%）。

## 最值得记住的一句话
低比特 KV cache 加速的关键不是减少内存带宽，而是消除逐元素反量化产生的指令 issue 瓶颈，affine folding 将 scale/offset 折叠到矩阵乘另一侧或输出，同时保持精确算术等价。
