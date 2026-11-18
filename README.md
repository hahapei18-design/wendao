# 问道

**遇到创业、工作、学习上的困惑,向厉害的人问路。** 目前收录马斯克和黄仁勋,每条建议都附他们的逐字原话和出处。

"问道"把马斯克(Elon Musk)和黄仁勋(Jensen Huang)在公开访谈、演讲、财报会和 X 上说过的话,按"普通人会问的问题"整理成中文卡片,做成一个通用格式的 [Agent Skill](https://agentskills.io)。

装上以后,你问 AI "马斯克招人看重什么""黄仁勋怎么面对失败""这句话真是他说的吗",它会去查这套资料,用**逐字核对过的英文原话 + 中文翻译 + 出处链接**回答。视频链接点开会直接跳到他说那句话的那一秒。

## 里面有什么

- **43 张中文卡片**:创业选方向、招人带团队、管理、决策与思考方法、学习、时间精力、面对失败、产品、成本、人生和家庭;第一性原理、五步工作法、找限制因素、光速、扁平组织、零亿美元市场等方法;AI、芯片、火箭、电动车、自动驾驶、机器人等行业看法;观点变化和预言兑现情况。卡片里 399 条原话全部用脚本逐字核对过原文。
- **原文**:马斯克 657 篇、黄仁勋 222 篇视频和文字稿(年份逐个核查过;另有 210 篇是同一场活动的重复上传,已标记,搜索时默认跳过),马斯克 2013 年到 2025 年 5 月的全部 X 推文和回复,以及从中挑出的 697 条讲做事方法的推文。
- **两个脚本**(只需要 Python 3):`scripts/search.py` 按关键词搜原话,`scripts/verify_quote.py` 核对一句原话是不是逐字存在、时间点对不对。

资料截止:视频到 2026 年 10 月,马斯克推文到 2025 年 5 月。

## 怎么装

把整个 `wendao` 文件夹放到你的 AI 工具读取 skill 的目录里:

- **Claude Code**:`~/.claude/skills/wendao/`(只给某个项目用就放 `<项目>/.claude/skills/`)
- **Codex**:`~/.codex/skills/wendao/`
- **其他支持 Agent Skills 的工具**:按该工具说明放到它的 skills 目录

```bash
git clone https://github.com/hahapei18-design/wendao.git ~/.claude/skills/wendao
git clone https://github.com/hahapei18-design/wendao.git ~/.codex/skills/wendao
```

不想装也可以直接读:从 [`references/index.md`](references/index.md) 进入,卡片都是普通的 Markdown 文件。

## 怎么用

装好后正常提问就行,不用特意提 skill 的名字。例如:

- 马斯克是怎么招人的?我开了个小公司想招第一个员工
- 黄仁勋说的"光速"是什么意思,普通人能用吗?
- "If things are not failing, you are not innovating enough" 是马斯克哪年说的?
- 马斯克对自动驾驶的时间预测准吗?

## 资料来源和局限

- 视频文字稿来自 YouTube 字幕和 [silicon-valley.tech](https://silicon-valley.tech) 整理的转写;财报会和部分访谈文字稿、推文、预言清单来自 silicon-valley.tech 的公开数据。
- 视频字幕是自动生成的,不分说话人,个别词可能听错。卡片里的原话已经回原文核对过,但引用前仍建议点链接听一下。
- 卡片里"你可以怎么用"和标着"我的判断"的部分是整理者的建议,不是他们的原话。
- 本项目不隶属于马斯克、黄仁勋或他们的公司。

## 许可证

MIT,见 [LICENSE](LICENSE)。
