---
title: A team of Gemini 4 Argon agents beats Minecraft
title_zh: 四个 Gemini 4 Argon 智能体合作通关 Minecraft
authors:
- Maxence Faldor
- Satinder Singh
- Roberta Raileanu
affiliations:
- Google DeepMind
arxiv_id: '2610.22319'
url: https://arxiv.org/abs/2610.22319
pdf_url: https://arxiv.org/pdf/2610.22319
published: '2026-10-14'
collected: '2026-10-16'
category: MultiAgent
direction: 多智能体协作长程任务执行
tags:
- MultiAgent
- LLM Agent
- Long-horizon
- Shared Memory
- Code-as-Action
- Minecraft
one_liner: 四个通用编码智能体通过 Mineflayer 编写 2783 个 JS 程序、共享记忆与聊天协作，27 小时 14 分首次端到端击败末影龙
practical_value: '- **把业务操作抽象为『代码作为动作』**：让 LLM 生成可执行脚本或 SQL 直接操作推荐系统内部接口，而不是只调用预定义高层工具；沉淀可复用
  helper 函数/工具（本案例 42 个 helper 函数被 1519 个程序引用），对应推荐 Agent 中的特征拼接、召回请求、指标计算等常用代码片段。

  - **共享记忆 + 轻量聊天双通道**：在 Agent 团队中区分私有状态与共享记忆（坐标、陷阱规则、工具 quirks），关键失败转成规则并广播，适合搜索/推荐多
  Agent 分工（召回、排序、文案、风控）传递候选与坑位，避免重复踩坑。

  - **独立 Observer 做校验与防作弊**：增加一个不参与业务的 Observer Agent，核对成功声明与真实日志/指标，防止虚假报告或规格博弈；在长链路推荐自动化中可让验证
  Agent 检查策略是否真的上线、A/B 指标是否显著。

  - **上下文压缩时外置关键进展**：当 Agent 上下文过长触发 compaction，强制把进行中任务和下一步写入外部记忆，防止丢失跨程序状态；适用于持续数小时的离线调参、自动策略搜索或商品文案批量生成任务。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
复杂现实软件工程与企业任务需要长期规划、多智能体协作与持续纠错。Minecraft 作为开放世界长程任务，要求跨三个维度完成资源采集、建造传送门、定位要塞、摧毁治疗水晶等数千个依赖步骤，是检验通用 LLM 智能体能力的理想测试床。此前方法或依赖强化学习训练，或叠加游戏特定规划器、技能库和人工编写的工具，尚未有团队用标准 Mineflayer 库从随机种子端到端击败末影龙。

### 方法关键点
- **通用编码智能体**：四个 Gemini 4 Argon 实例各控制一名 Minecraft 玩家，通过开源 Mineflayer 库 + pathfinding 插件操作。智能体不接收像素输入，而是编写短 JavaScript 程序（如走到坐标、挖掘矿石、合成物品）并读取文本反馈（位置、血量、背包、错误信息）。
- **零游戏专用逻辑**：无预设角色、无课程、无技能库、无人写工具。指令仅说明目标为击败末影龙，并沿用通用软件工作指令：验证结果、构建可复用工具、记录教训到共享记忆、诚实报告。
- **协作机制**：玩家通过游戏内聊天通信（229 条消息），共享记忆包含坐标、传送门位置、危险区域、工具 quirks。角色自发分工：janesick 负责工具、要塞与三角定位；gyldenia 负责补给与水晶；auratian 负责下界传送门与水晶打法；bulicame 负责末影人庇护所与最后一击。
- **失败转规则与纠错**：从 605 次死亡中持续提取教训（如 Ghast 摧毁掉落物后规定安全路线；末影龙阶段与站位规则）。智能体之间互相验证：auratian 主动撤回虚假成功，gyldenia 发现 janesick 烧死后仍报告带回物品的矛盾。
- **第五个 Observer 智能体**：独立见证者，核对玩家声称与服务器日志，监控规格博弈和捏造结果，但不干预策略。

### 关键实验与结果
- 在随机种子、Easy 难度、无作弊命令的 Minecraft 1.20.4 生存世界中，团队编写并运行 2783 个 JavaScript 程序（63,313 行代码），总耗时 27 小时 14 分钟击败末影龙。
- 期间死亡 605 次，约 22% 程序以错误结束；下界到要塞阶段和末影龙战斗消耗最多时间（末影龙阶段近 14 小时）。
- 成本估算：四人玩家智能体处理约 1.35 亿输入 tokens（91% 来自上下文缓存）和 1600 万输出 tokens，约 2.4 万次模型调用；按公开 API 列表价约 $520–1040。
- 与社区项目对比：单 Claude Opus 5 调用 37 个高层 Minecraft 工具、或固定 speedrun 种子 + planner + 动作模型；本工作仅使用标准 Mineflayer + pathfinding 插件，所有程序由智能体自己编写。

### 最值得记住的一句话
四个通用编码智能体不依赖任何游戏专用工具，仅通过写代码、共享记忆和互相纠错，在 27 小时 14 分钟内从随机种子自主完成击败末影龙的完整长程任务。
