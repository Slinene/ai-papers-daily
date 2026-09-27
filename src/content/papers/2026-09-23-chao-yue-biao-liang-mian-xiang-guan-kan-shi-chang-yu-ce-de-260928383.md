---
title: 'Beyond a Scalar: Distributional Serving Interfaces for Watch-Time Prediction'
title_zh: 超越标量：面向观看时长预测的分布式服务接口
authors:
- Xuan Liu
- Jingbin Qian
- Zhanyu Liu
- Hefeng Zhou
affiliations:
- Shanghai Jiao Tong University
- Rice University
arxiv_id: '2609.28383'
url: https://arxiv.org/abs/2609.28383
pdf_url: https://arxiv.org/pdf/2609.28383
published: '2026-09-23'
collected: '2026-09-27'
category: RecSys
direction: 短视频推荐 · 分布服务接口
tags:
- watch-time prediction
- distributional serving
- short-video recommendation
- duration bias
- event-time distribution
one_liner: 将观看时长从单一标量改为冻结分布提供器与紧凑摘要，下游只训轻量 readout 即可复用多目标
practical_value: '- 把单点预测服务改成分布摘要接口：冻结上游模型，对外暴露紧凑分布统计（事件概率、分位数/时间尺度、熵、主导 gap），下游不同业务目标（点击、转化、GMV、时长、互动）只训练轻量
  linear/DCN head，避免反复全量重训，支持快速迭代和多目标复用。

  - 用 deterministic 业务规则从原始 label 构造多事件类型（如 ratio 分段 early/mid/completion/overplay），不需要额外标注，同时用
  duration-aware support mask 屏蔽不合法组合，能更好刻画短视频/信息流的完播与超播。

  - 在分布摘要中保留显式 duration-relative 统计（如 completion ratio、overplay ratio gap）可以提升 duration-relative
  ranking，适合业务中完播率、超额消费等指标。

  - 新目标上线时只需冻结 provider，对新 label 训一个线性头即可，低标签预算（1%）就能达到或超过全量 baseline；随机初始化 provider
  无效，说明收益来自学到的 watch-time 结构而非额外特征通道，这种接口化思路可复用到用户/物品表示服务。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

现有观看时长预测在 serving 时普遍只输出一个期望值或去偏标量，即使下游能拿到视频时长，也只能得到时长归一化的点估计。相同的预测秒数在 12 秒和 60 秒视频中含义完全不同，而单一标量无法表达完成、超播等区域的概率分布。当新决策需要不同的时长相关目标时，要么复用该点估计，要么重训整个预估器。

**方法关键点**

- 三阶段 Distributional Serving Interface（DSI）：
  1) 从日志观看时长和视频时长构造四类 operational event types——early / mid / completion / overplay，按 watch ratio 阈值 0.3、0.9、1.1 划分，同时得到 event-time bin，不引入额外标签；
  2) 训练 provider 估计 event type 与 event time 的联合分布，按视频时长屏蔽不兼容的 type-time 组合，损失为 support-masked NLL + log-space restoration SmoothL1，对齐秒级均值；
  3) 冻结 provider，将分布压缩为 27 维摘要，包括事件边际概率、long mass、均值、时长相对时间尺度、熵、主导 gap 等，下游用共享 DCNv2 readout：value branch 恢复秒级预测，ranking branch 训练 overplay 排序，可迁移到 long engagement 和新目标。

**关键结果数字**

在 KuaiRec、KuaiRand-1K、WeChat21 三个公开短视频数据集上，完整 DSI 系统 MAE 相对最强 baseline 降低 1.9%–8.5%，XAUC 在两个数据集上最优；Long-N@5 和 OP-N@5 在所有数据集上均第一。控制实验显示紧凑摘要优于 mean+duration 点接口；冻结接口迁移到新 watch-time targets（ratio>0.5、Q75）和独立 engagement label 时，仅用线性 head 即可取得最优，且随机初始化 provider 无增益。

**最值得记住的一句话**

把“预测一个秒数”变成“冻结一个分布，对外暴露一个紧凑摘要，每个下游目标只训一个轻量 readout”。
