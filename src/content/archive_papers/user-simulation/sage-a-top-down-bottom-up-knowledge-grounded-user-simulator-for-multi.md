---
title: 'SAGE: A Top-Down Bottom-Up Knowledge-Grounded User Simulator for Multi-turn
  AGent Evaluation'
authors: Ryan Shea, Yunan Lu, Liang Qiu, Zhou Yu
affiliation: Columbia University
date: 2025-10
venue: EACL 2026 Findings
topic: user-simulation
topic_name: User Simulator
topic_icon: 👥
idea: Simulator 不能脱离业务知识：Top-down 用 ideal customer profile / persona 灌入业务逻辑，Bottom-up
  把 agent infra 的商品目录、FAQ、知识库灌进 simulator，让用户 "知道自己要什么、要怎么问"。比基线多发现 33% 的 agent error。
paperUrl: https://arxiv.org/abs/2510.11997
tags:
- User Simulator
- Knowledge Grounded
- Evaluation
- Persona
unverified: false
---

## 核心思路

**问题**：多轮交互式 agent（客服、销售、导购）难评测——靠真人成本高、不可规模化；现有 user simulator 要么依赖稀缺的真人对话数据，要么用 prompt 造一个"通用闲聊用户"，提的问题脱离具体业务，导致评测时**触发不到真实 bug**。

**关键 idea**：真实客户的行为由两件事决定——**他是谁**（角色、画像、购买力）和**他想要什么信息**（公司特定的产品知识）。SAGE 据此把两路业务知识灌进 simulator：

- **Top-down 知识**：来自业务逻辑的用户画像。核心是 **ICP（Ideal Customer Profile，理想客户画像）**——firmographics（行业/公司规模）、决策权限、预算、deal stage 等营销维度，再叠加 Big-Five 人格 + 人口学的"个体差异"。让 simulator 演的是"对这家公司有价值的那类客户"，而不是泛泛路人。
- **Bottom-up 知识**：来自 agent 自己的基础设施（商品目录 SQL 库、FAQ、知识库向量库、库存表）。把 agent 看得到的同一份知识也喂给 simulator，让它"知道该问什么、期望得到什么答案"。这份知识在评测阶段还充当 **LLM-judge 的 ground truth 参照**，用来判 agent 回答是否 faithful。

两路知识融合 → 构造 task scenario → 驱动多轮交互 → LLM-as-Judge 抓错并聚合成 unique bug 列表。结果：交互更真实、更多样，且比无知识 baseline 多发现 **25–33%** 的 agent bug。

## 整体实现思路

SAGE 是一条无需真人数据的端到端 pipeline，分四步（见下图）：

![SAGE 整体框架：configure knowledge / build task scenarios / generate interactions / evaluate agent 四个流程，左侧定义 top-down 用户属性与 bottom-up agent 基础设施知识，中间构造 task scenario 驱动 simulator 与待测 agent 多轮交互，右侧用 LLM-as-Judge 五维打分并聚合成 bug report](/ai-papers-daily/figures/sage-a-top-down-bottom-up-knowledge-grounded-user-simulator-for-multi/fig1.png)

1. **Configure Knowledge（配置知识，§3.1）**：定义三类输入——① user attributes（个体差异 + ICP，可配置）；② agent capabilities（公司给出要测的功能清单）；③ agent infrastructure knowledge（结构化 catalog + 非结构化 FAQ/网页）。
2. **Build Task Scenarios（构造场景，§3.2）**：把 agent capability 用 LLM 翻成 user goal；按 goal 分层选一条相关 infra 知识；据知识 + 属性生成连贯 user profile；三者拼成自然语言 task scenario，作为 simulator 的 system prompt。
3. **Generate Interactions（生成交互，§3.3）**：simulator 与待测 agent 在共享环境里多轮对话。simulator 经 system prompt 显式接地于 infra 知识；agent 黑盒访问自己的知识。对话历史持续 append 双方上下文，直到 simulator 吐 `###STOP###` 或达 turn budget。
4. **Evaluate Agent（评测抓 bug，§3.4）**：LLM-as-Judge 对每个 agent turn 五维打分；低分 turn → 两阶段聚合成 unique bug 列表 + 报告。

整条链路全部用 LLM 算子（goal 翻译、属性生成、profile 转写、对话、打分、聚错），**零真人对话训练数据**，对应"冷启动新 agent 没历史 log"的现实开发场景。

## 子模块实现（可复现细节）

### 1. User Attributes（top-down 用户属性）

两类，全部可配置：

**个体差异（Individual Differences）**
- Big-Five 人格：conscientious / extroverted / antagonistic / neurotic / closed-to-experience 五维各取值。
- 人口学：年龄、性别、教育、国籍/地点、婚姻、家庭规模、政治倾向等（沿用 Toubia et al. 2025 的 Twin-2K-500 体系）。

**ICP（理想客户画像）**，按 B2B / B2C 分两套（Appendix B）：
- **B2B 属性**（值集在括号内）：customer type（new prospect / returning），discovery channel（search engine / third-party / friend rec / social media），budget，decision-making authority（primary / secondary），deal stage（new leads → demo schedule → after demo → decision make → contract sent → signed → paid），industry，company name，job information，company size。其中 authority、customer type、deal stage 是**小而稳定的枚举值集**；company name、industry、job information 这类**动态生成**（值太多无法穷举）。
- **B2C 属性**：复用 B2B 可迁移字段（customer type / discovery channel / budget）+ decision-making style（rational / intuitive），purchasing preference（discount / value / quality-oriented），spending behavior（5 档 tightwad–spendthrift 量表，Rick et al. 2008），loyalty level（loyal / neutral / disloyal）。

### 2. Agent Capabilities → User Goals

公司给出能力清单，LLM 把每条 capability 翻成一个 user goal（如"购买清洁机器人"/"询问某型号清洁效率"）。电商场景下按消费者决策模型分 5 阶段组织能力（Appendix C，Table 6），用 **Verb–Object–Prepositional-Phrase（EARS 需求语法）** 写成可测指令：

| 决策阶段 | 示例 agent capability |
|---|---|
| Need Recognition | 基于场景协助购买规划 |
| Information Search | 在给定品类/约束内推荐商品；回答 feature 级产品问题 |
| Evaluation of Alternatives | 提供商品对比 |
| Purchase Decision | 回答配送查询；回答折扣/促销查询 |
| Post-Purchase | 处理订单追踪；处理产品缺陷上报；处理退款/退货 |

遍历全部 goal → 保证对 agent 全能力面的覆盖。

### 3. Agent Infrastructure Knowledge Selection（分层选知识）

输入：一个 user goal。目标：选出**既相关又多样**的一条 infra 知识。

- 知识按 category 组织（FAQ / product catalog / …），每 category 含多条 knowledge piece（SQL 结构化 / 向量库非结构化）。
- **第一层**：LLM 给定 goal 选相关 category（如 goal 是"问折扣"→ 选 FAQ）。
- **第二层**：在选中 category 内用**聚类算法**找最相关的知识簇（如"reward program / promo code"簇）。
- **多样性采样**：从簇里采一条**之前没用过**的 piece；若全用过则簇内随机选一条。

### 4. Profile Construction（画像生成）

输入：选中的 infra 知识 + 用户属性 schema。输出：一段第二人称自然语言 profile。

- 每个属性是 `key → (预定义值元组)`；无预定义值的 key（firmographics / budget / company name / job info）由 **LLM 据选中的 infra 知识动态生成**（prompt 见 Appendix G.1：给定 knowledge，一次生成 `num_personas` 套 business_type / company_name / job_information / company_size，要求 diverse 且与公司 overview 对齐，返回 JSON）。
- **联合选值保证一致性**：所有 key 的值**一次性联合生成**，避免互相矛盾（job info 依赖 industry 与 company name）。另有一个 **validate-attributes** LLM 步骤：对每对属性判 Yes/No 一致性（例："commercial cleaning 公司不会叫 Caesars Entertainment"→ No；"returning customer 不会处于 new leads stage"→ No）。
- **转写 prompt**：第二人称，固定以 `"You are <name> who is <TRAIT 1..5>."` 开头嵌入 Big-Five。Appendix D 的样例 profile 把 11 项 ICP/人口学属性串成一段连贯人设（如 32 岁 Event Coordinator、$90k–130k 预算、primary 决策权、new prospect / new leads stage）。

### 5. Task Scenario & Simulator System Prompt

最终 scenario = user goal + infra 知识 + user profile，用结构化模板拼成，外加行为规则。simulator system prompt（Appendix G.2）关键约束：
- 每次只生成**一行**用户消息，简短；不一次性倒出全部 instruction；
- **禁止幻觉**：instruction 没给的信息（如 order id）就说"不记得/没有"，不编造；
- 不照抄 instruction，要用自己的话；按 background（job / household / 活动）个性化提问；按人格调语气；
- 模仿真人客户**短句 + 偶尔 typo + 不完整句**的 chitchat 风格，以提问开场；
- goal 满足后输出独立的 `###STOP###` 结束。

### 6. Evaluate Agent（LLM-as-Judge + 两阶段聚错）

**打分**（Appendix G.3）：对每个 agent 回复沿五维各打 **0–4 分 + 理由**：helpfulness、coherence、verbosity、relevance、faithfulness。faithfulness 的 prompt 额外注入 bottom-up `{knowledge}` 作为事实参照——这是 SAGE 相对纯 prompt simulator 的关键增益（不靠模型内部知识判对错）。评测模型 `gpt-4.1-2025-04-14`，temperature=0.1。

**阈值**：只保留**得分 < 2** 的 turn 视为问题 turn。阈值经人审标定（不同模型评分偏置不同，如 gpt-5 的 helpfulness 系统性偏低，需各自标阈值）。人审 50 条低分 turn → 94% 确含 bug；50 条高分 turn 仅 4 条有错。

**两阶段聚错**（Appendix G.4）：
- 阶段一：LLM 据问题 turn + 理由生成**高层失败类目**（Unspecific / Inaccurate / Incomplete / Irrelevant / Repetition 等），返回 JSON。
- 阶段二：给定类目 + 理由，**去重**成 fine-grained unique bug statement（明确指令"不要再用 helpfulness/coherence 这些维度，要落到 agent 具体行为，每条缺失信息算一个独立 bug"，附 item_id），如"did not provide weight capacity for Product_A when explicitly requested"。
- 最终输出 bug 列表 + 各 bug 关联 turn 的报告。

**LLM 抓 bug 质量验证**：对同 50 条低分 turn，LLM bug 列表 vs. 三位人类专家 → precision 0.73 / recall 0.74 / F1 0.73 / accuracy 0.74；专家间一致性 Fleiss' Kappa = 0.85。

## 实验设置与结果

**两个待测 agent**：① 机器人公司**生产环境部署的 RAG 销售 agent**（用技术 catalog + FAQ + 企业信息答产品咨询，目标是最大化 lead conversion）；② Shopify 上的 **Tool-augmented 导购 agent**（集成 13 个 API：get_recommendation / get_user_info / get_product / return_item / cancel_order 等 + FAQ/店铺政策）。

**两条消融基线**（对应两个假设 H1/H2）：
- **w/o ICP**：去掉 top-down ICP，只留个体差异 + bottom-up 知识——对标 τ-bench / CRMArena 的 prompt simulator。
- **w/o Agent-Infra**：去掉 bottom-up infra 知识，只留企业 overview + top-down——对标 DuetSim 这类纯 persona simulator。

**模型**：gpt-4.1（正文）；gpt-5 / gemini-2.5-flash / Qwen2.5-7B-Instruct / Llama-3.3-70B-Instruct（附录）。每条件每 use case 生成 150 段交互；真人交互从生产 log（2024.07–2025.07，英文，按 lead conversion 分析保留 **3–15 turn** 区间，该区间转化率 >20%）采 150 段。

**指标**：① 词汇多样性（reference-free：MTLD / HD-D / logTTR / rootTTR / vocab size / distinct@1-2-3，越接近真人越好）；② simulator fidelity（人评 3 点 Likert × 4 维：human-likeness / coherence / specificity / consistency）；③ 发现的 unique bug 数（越多越好）。

### 词汇多样性（gpt-4.1，Table 1，加粗=最接近真人）

| Method | MTLD↑ | HD-D↑ | logTTR↑ | rootTTR↑ | Vocab↑ | Distinct@1/2/3↑ |
|---|---|---|---|---|---|---|
| **RAG 销售 agent** | | | | | | |
| w/o ICP | 81.43 | 0.86 | 0.77 | 11.58 | 1011 | 0.21/0.60/0.81 |
| w/o Agent-Infra | 80.76 | 0.85 | 0.76 | 10.65 | 973 | 0.18/0.55/0.76 |
| **SAGE** | **86.05** | 0.86 | **0.78** | **11.80** | **1034** | **0.21/0.61/0.82** |
| **Tool 导购 agent** | | | | | | |
| w/o ICP | 76.52 | 0.86 | 0.75 | 9.88 | 907 | 0.18/0.57/0.78 |
| w/o Agent-Infra | **81.59** | 0.86 | 0.75 | 9.82 | 953 | 0.17/0.56/0.78 |
| **SAGE** | 79.97 | 0.86 | **0.76** | **10.37** | **961** | **0.19/0.59/0.80** |
| Human（参照） | 86.84 | 0.87 | 0.84 | 20.62 | 1360 | 0.30/0.72/0.91 |

SAGE 几乎所有指标最接近真人（仅 Tool 场景 MTLD 例外）。注意真人 rootTTR(20.62)/vocab(1360) 仍显著高于所有 simulator——多样性仍有差距。

### Simulator Fidelity 人评（RAG agent，gpt-4.1，Table 2；∗=对两 baseline 均显著 p<0.05，†=对一个）

| Method | Human-likeness↑ | Coherence↑ | Specificity↑ | Consistency↑ |
|---|---|---|---|---|
| w/o ICP | 2.38 | 2.75 | **2.80**† | 2.88 |
| w/o Agent-Infra | 2.20 | 2.50 | 2.53 | 2.88 |
| **SAGE** | **2.58**∗ | **2.85**∗ | 2.75† | 2.88 |
| Human | 2.90 | 2.85 | 2.85 | 2.90 |

SAGE 在 human-likeness、coherence 上显著最优且最接近真人；specificity 上 w/o ICP 略高（说明 specificity 主要靠 bottom-up 知识）；consistency 四者持平（该维度对知识注入不敏感）。整体 w/o ICP > w/o Agent-Infra，暗示**对 RAG agent，bottom-up infra 知识比 ICP 更重要**。

### Unique Bug 数（5 次平均，Table 3 / Table 9 / Table 12）

| Simulator model | Method | RAG-based | Tool-Augmented |
|---|---|---|---|
| gpt-4.1 | w/o ICP | 29.0 | 14.4 |
| gpt-4.1 | w/o Agent-Infra | 13.6 | 13.0 |
| gpt-4.1 | **SAGE** | **38.6** | **18.0** |
| gpt-4.1 | Human（参照） | 14.0 | – |
| gpt-5 | w/o ICP | 27.4 | 19.2 |
| gpt-5 | w/o Agent-Infra | 14.6 | 17.8 |
| gpt-5 | **SAGE** | **28.8** | **24.0** |
| gemini-2.5-flash | **SAGE** | **27.8** | **24.2** |
| Qwen2.5-7B | **SAGE** | **20.6** | **21.2** |
| Llama-3.3-70B | **SAGE** | **23.2** | **21.2** |

**结论**：SAGE 在所有模型/场景下都抓到最多 unique bug，次优是 w/o ICP；**去 bottom-up 知识掉得最狠**（gpt-4.1 RAG：38.6 → 13.6）。SAGE vs. 次优 baseline 的提升约 **25–33%**（gpt-4.1 RAG：38.6 vs 29.0 = +33%）。值得注意：**真人交互只暴露 14 个 bug，远少于 SAGE**——说明 simulator 在 bug-finding 上可能比真人 log 更有效。

### 失败类目分布（Figure 2）

![Figure 2：RAG 销售 agent 五类高层错误（Unspecific / Inaccurate / Incomplete / Irrelevant / Repetition）的 unique error 数，w/o Agent-Infra（蓝）/ w/o ICP（橙）/ SAGE（绿）三条件对比柱状图；SAGE 在 Unspecific 与 Inaccurate 两类上大幅领先](/ai-papers-daily/figures/sage-a-top-down-bottom-up-knowledge-grounded-user-simulator-for-multi/fig2.png)

SAGE 抓到的错误集中在 **Unspecific Response** 与 **Inaccurate Answer**——正好对应 RAG 系统的核心失效模式（检索不准/不全）。w/o Agent-Infra 在这两类几乎抓不到错，印证 **bottom-up 知识是触发"信息检索类"bug 的关键**。另：绝大多数 error 出现在**第一轮之后**（Incomplete / Irrelevant / Repetition 尤甚），说明多轮评测不可替代（与 "LLMs get lost in multi-turn" 一致）。

### 案例（Table 4/13）

同一 goal"对比产品"下：SAGE 是**唯一**触发 agent error 的条件——抓到两个 faithfulness 错（agent 谎称 Product_A "适合户外/3 小时充满"，实际是室内用、需 5.5 小时）。第一个错由 top-down ICP 知识驱动的"农业户外适用性"提问触发，第二个由 bottom-up 知识驱动的"充电时间"提问触发——**两路知识各自能逼出不同类型的错**。w/o ICP 用泛化 persona → 重复/通用提问、轨迹不多样；w/o Agent-Infra → 提了与场景无关的问题（拿一台做餐饮的 Product_B 去问农活）。

## 思考与可参考价值

**局限**（含作者自述）：
1. 预定义属性源自**面向客户的 business logic**，内部 agent（教育/开票/后台）需自行重定义属性。
2. 一个 task scenario 只含**单 goal + 单条 infra 知识**，无法覆盖真人在同一 session 内切话题的复杂轨迹。
3. **强依赖业务侧已有结构化知识**（catalog/FAQ）；ICP 设计仍需人工。
4. 评测是**冷启动设定，无真人参照对比**；多样性只用了 reference-free 词汇指标，fidelity 靠人评——指标偏弱。
5. 33% 的增益是 **evaluation 视角**（发现更多 bug），不直接等于 agent 训练增益；且 LLM 生成属性可能放大主流群体、弱化少数群体（作者在 Ethics 中承认）。

**对电商/搜推/Agent 方向的可借鉴点**：
- **"双路知识接地"是可直接复用的工程范式**：评测电商导购/客服 agent 时，把商品 SQL 库 + FAQ + 用户画像（ICP）同时灌进 simulator，能让模拟用户提"业务真问题"，精准压测检索/工具调用链路——比通用 user-bot 找 bug 多 25–33%。
- **faithfulness judge 注入 ground-truth 知识**：把 bottom-up 知识同时作为 judge 的事实参照，是治 LLM-judge 幻觉的实用做法，可迁到任何 RAG agent 离线回归。
- **属性联合生成 + 一致性校验**两步，是生成"逻辑自洽 persona"的轻量方法，可用在推荐/营销的合成用户群体构造。
- **ICP × deal-stage × spending-behavior** 这套营销维度对电商尤其契合——按 deal stage / 购买偏好分层造模拟用户，能做漏斗各阶段的 agent 压测与覆盖率统计。
- **"simulator 比真人 log 更会找 bug"**的发现值得警惕也值得利用：simulator 可主动构造对抗/边界 query 提升 evaluation coverage，但要注意它不复刻真实流量分布，上线前仍需真人 log 校准。
