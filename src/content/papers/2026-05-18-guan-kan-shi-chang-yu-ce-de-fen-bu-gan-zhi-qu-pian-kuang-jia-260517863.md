---
title: 'DADF: A Distribution-Aware Debiasing Framework for Watch-Time Regression in
  Recommender Systems'
title_zh: 观看时长预测的分布感知去偏框架DADF
authors:
- Yiqing Yang
- Xinlong Zhao
- Zhao Liu
- Xiao Lv
- Ruiming Tang
- Han Li
- Kun Gai
affiliations:
- Kuaishou Technology
- Unaffiliated
arxiv_id: '2605.17863'
url: https://arxiv.org/abs/2605.17863
pdf_url: https://arxiv.org/pdf/2605.17863
published: '2026-05-18'
collected: '2026-05-19'
category: RecSys
direction: 观看时长预测 · 分布感知去偏
tags:
- Watch-Time Prediction
- Debiasing
- Long-Tailed Regression
- Multiplicative Correction
- Duration Bias
- Second-Stage Correction
one_liner: 通过动态分布变换、时长分组专家和多任务辅助信号，在不动第一阶模型的情况下对观看时长做第二阶乘性校正
practical_value: '- **轻量即插即用的第二阶校正**：不替换已部署的主模型，只在推理阶段增加一个乘性校正因子（bias factor）的轻量子网络。电商中的连续目标（如GMV、支付金额、转化深度）预测如果存在局部高估/低估，可借鉴该范式快速上线。

  - **分组自适应变换处理长尾**：利用Box–Cox变换将长尾的乘性校正因子映射到类高斯空间，且按视频时长（或类目、客单价）分组学习专用变换参数，缓解长尾回归的不稳定。可迁移到其他长尾连续值预测。

  - **已知分组特征的专家网络**：用视频时长作为debias factor划分组，每组用独立专家预测校正值，显著降低组间方差。电商中可用价格带、品类等已知特征构建组路由，提升校准的细粒度。

  - **多任务辅助信号增强校正**：从已存在的多任务头（如完播、有效观看、负反馈等）提取logits和tower表示，拼接后作为校正网络的输入，几乎无额外成本。已有MMoE/PLE等多任务结构的推荐系统可直接利用。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
工业短视频推荐中，观看时长预测普遍存在**伪平衡**现象：模型在全局校准良好，但会系统性地高估短播放、低估长播放，两类相反偏差在整体平均时抵消，隐藏了严重的局部校准问题。以往方法多聚焦于改进第一阶预测器，但线上更换成本高。本文提出不替换主模型，而是在后处理阶段用轻量网络建模乘性校正因子，消除残余偏差。  

**方法关键点**  
- **动态分布感知变换**：针对乘性校正因子（真实观看时长/第一阶预测）的长尾性，按视频时长划分组，每组学习一个Box–Cox变换，将校正目标映射到类高斯空间，稳定训练。  
- **时长感知路由专家**：用视频时长定义debias-factor分组，每组一个专家网络预测变换后的校正值，利用分组可降低残差的组间方差（oracle风险分析）。  
- **多任务辅助模块**：从冻结的第一阶多任务头（如完播、有效观看、长播等）提取logits和tower表示，经自注意力融合后作为侧信息输入校正网络，强化对用户消费强度的感知。  
- **联合训练目标**：变换空间MSE + 原始空间Huber loss + 分组矩正则化（约束变换后目标的均值为零、方差为1、偏度为零），平衡稳定性和精度。  

**关键结果**  
在两个公开数据集（KuaiRec、WeChat21）上，DADF作为插件在7种不同类型的第一阶模型（VR、WLR、TPM、D2Q、CREAD、D2CO、EGMN）上均取得一致的MAE下降（平均4.33%）和XAUC提升（平均4.01%），显著优于全局校正基线TranSUN。在快手国际版的在线A/B测试中，DADF带来平均设备时长+0.347%、App总时长+0.356%、长播率+0.351%，且7日留存+0.054%。消融实验证明分布变换、时长分组和多任务辅助信号三部分互相补充，尤其是变换模块对MAE的贡献和多任务对XAUC的贡献最突出。细粒度分析显示，DADF在长时长视频桶上MAE降幅超过23%，尾部切片增益放大，验证其对局部偏差的有效修正。
