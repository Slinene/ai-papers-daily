---
title: 'PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool
  Actions'
title_zh: PhoneHarness：混合GUI、CLI与工具动作的手机智能体基准与执行框架
authors:
- Chenxin Li
- Zhengyao Fang
- Zhengyang Tang
- Pengyuan Lyu
- Xingran Zhou
- Xin Lai
- Fei Tang
- Liang Wu
- Yiduo Guo
- Weinong Wang
affiliations:
- Tencent Hunyuan
- The Chinese University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
- Tsinghua University
arxiv_id: '2606.14832'
url: https://arxiv.org/abs/2606.14832
pdf_url: https://arxiv.org/pdf/2606.14832
published: '2026-06-11'
collected: '2026-06-17'
category: Agent
direction: 手机智能体 · 混合动作执行基准
tags:
- Phone Agent
- GUI Automation
- Mixed Actions
- Benchmark
- Verifiable Execution
one_liner: 提出混合动作手机智能体基准和执行框架，通过率75.0%，超越仅GUI方法12.9个百分点
practical_value: '- **移动端自动化任务设计**：在电商App的自动下单、客服回复等场景中，不应仅依赖GUI视觉操作，可借鉴混合GUI、CLI（设备侧命令）和工具调用的思路，提升动作可靠性与效率。

  - **可验证执行与审计**：引入“可观察副效应”验证机制（如检查文件是否修改、消息是否发送），确保智能体操作真实生效。电商场景中可类似验证订单是否提交、推送是否发出，避免“看起来很对但实际没做”的风险。

  - **动作路由与委托架构**：PhoneHarness采用确定性路由与有限GUI委托的代理循环，可作为构建多动作空间购物助手（如既能操作界面又能调用API查询商品）的参考架构。

  - **任务完成式评估**：其基准设计关注任务完成而非仅答案匹配，可直接迁移到推荐系统多步交互评测，例如衡量购物助手是否真正帮用户完成“挑选并下单”全流程，而非仅给出推荐列表。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有手机智能体评测多聚焦于单步GUI动作预测，忽略了真实任务需混合使用GUI、CLI和工具调用，且缺乏对操作是否真正生效的验证。
**方法**：推出PhoneHarness，一个包含基准与执行框架的套件。执行框架在设备端运行代理循环，支持GUI、CLI和主机端工具动作，通过确定性路由与有限GUI委托统一调度，并生成可审计的执行轨迹。基准PhoneHarness Bench以任务是否产生可观察副效应（如文件修改、消息发送）为通过标准，而非仅评估输出答案的合理性。
**结果**：在标注评估集上，PhoneHarness单智能体达到75.0%通过率，比不使用该混合动作框架的最强配置高出12.9个百分点。实验表明，可靠手机自动化更依赖动作表面路由与可验证执行，而不仅是视觉GUI控制。
