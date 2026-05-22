---
title: 'DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback'
title_zh: DeltaBox：面向有状态AI智能体的毫秒级沙箱检查点/回滚系统
authors:
- Yunpeng Dong
- Jingkai He
- Yuze Hou
- Dong Du
- Zhonghu Xu
- Si Yu
- Yubin Xia
- Haibo Chen
affiliations:
- Shanghai Jiao Tong University
- Huawei Technologies Co., Ltd.
arxiv_id: '2605.22781'
url: https://arxiv.org/abs/2605.22781
pdf_url: https://arxiv.org/pdf/2605.22781
published: '2026-05-21'
collected: '2026-05-22'
category: Agent
direction: AI智能体沙箱环境·增量状态检查点
tags:
- Sandbox
- Checkpoint-Restore
- AI Agent
- OverlayFS
- Process Memory
- CoW
one_liner: 通过仅复制连续检查点间的增量变化，实现耦合文件系统与进程内存的毫秒级检查点/回滚，解决AI智能体搜索的状态管理瓶颈。
practical_value: '- **快速沙箱重置与克隆**：DeltaFS 基于 OverlayFS 的热层切换，可在 1-2 ms 内完成文件系统快照与回滚，适合电商测试环境、推荐模型
  A/B 实验沙箱的毫秒级快速重建，避免全量复制。

  - **轻量级进程模板池**：DeltaCR 通过 fork 冻结模板进程，恢复时仅复制页表（~3 ms），可借鉴为每个用户会话或推理请求预 fork 模板，实现极低延迟的隔离执行环境，例如为每个电商搜索请求快速创建上下文隔离的
  Python 解释器。

  - **异步预热页表降低延迟抖动**：后台线程遍历子进程的匿名可写 VMA 触发 CoW 预拷贝，将页故障开销移出关键路径，适用于需要快速恢复的高频在线学习或特征生成任务。

  - **一致性的联合状态管理**：文件系统与进程内存的耦合检查点保证智能体回溯时上下文不分裂，可直接用于多智体仿真、代码执行驱动的奖励模型评估等需要回滚到精确历史点的场景。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM 驱动的 AI 智能体在解决复杂任务（如代码修复）时，需通过树搜索（MCTS）、Best-of-N 等策略探索状态空间，频繁对沙箱环境进行检查点和回滚。现有方案（Docker commit、VM 快照、文件复制）依赖全量复制整个文件系统和进程内存，延迟达数百毫秒至秒级，严重制约深度搜索和强化学习训练吞吐。关键观察是：相邻检查点之间仅存在少量增量变化（几个文件或内存页）。因此仅复制变化即可实现高效 C/R。

## 方法
DeltaBox 提出 **DeltaState** 抽象，将文件系统和进程内存视为事务性的变化对，并设计两个协同的 OS 机制：
- **DeltaFS**：扩展 OverlayFS，支持运行时动态层切换。检查点时冻结当前可写层为只读层，插入新可写层；文件更新变为写时复制，回滚仅需层切换。通过 per-inode 生成计数器实现跨检查点的惰性文件描述符重定向，避免强制关闭文件。
- **DeltaCR**：进程状态增量转储 + 模板 fork 快速恢复。每个检查点同时执行异步 CRIU 增量 dump（持久化）和模板创建 fork（父进程冻结为模板），恢复时优先从模板 fork 出子进程（~3.75 ms），若模板被淘汰则回退到 CRIU 惰性页恢复（~7.25 ms）。后台异步预热线程在子进程恢复后立即遍历其匿名可写 VMA 触发 CoW，吸收后续写入的缺页开销。状态管理器确保文件系统和内存状态在检查点时刻一致，并为值函数测试提供无副作用隔离。

## 实验
在 SWE-bench Verified 四个典型仓库（Django、SymPy、Astropy、Xarray）上评估：
- 耦合检查点平均延迟 **14.57 ms**，回滚（快速路径）**5.14 ms**，比 Docker commit+重放快两个数量级。
- 在 100 轮 MCTS 轨迹中，DeltaBox 将沙箱操作开销从基线的 47–77% 降低至 **3–6%**，使智能体在固定时间预算内探索更多节点。
- 文件系统写放大与修改量成比例，得益于 XFS reflink 和 overlayfs 层级 CoW 保存，大文件多次检查点仅占用单个物理块。
- 与 Firecracker 差分快照相比，回滚延迟降低 139–325 倍。
