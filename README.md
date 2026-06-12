# vision-analyzer 🔍

本地识图工具 —— 图片发给本地 llama-server 进行视觉识别，零费用，零隐私泄露。

---

## 🚀 一键式傻瓜安装

### 一句话搞定

支持：Reasonix · Claude Code · Cursor · Gemini CLI · GitHub Copilot · Windsurf · Cline · Aider …

直接复制下面这行话，丢给你的 AI Agent，就装好了：

```
强制重装这个项目，删除旧版本后重新安装最新版：https://github.com/Kepsilent/vision-analyzer
```

> ⚠️ 重要：AI 不得跳过安装流程，必须删除旧版本后重新下载覆盖。详见 `INSTALL.md`。

Agent 会自动读取 `AGENTS.md` → 按 `INSTALL.md` 步骤执行。当前会话立刻生效。

---

## 🛠️ 傻瓜式使用

装好后，在聊天框里直接输入：

```
/vision-analyzer
```

或者用自然语言说：

```
- "识别一下这张图"
- "分析这个图片里有什么"
```

> 如果你已经装过但想升到最新版，重新复制顶部的那句话丢给 AI Agent 即可强制覆盖。

---

## 📖 项目介绍

本地识图工具 —— 图片发给本地 llama-server 进行视觉识别，零费用，零隐私泄露。

### 为什么需要它

- ❌ 云端识图（GPT-4V）需要上传图片 → 隐私泄露风险
- ❌ API 调用按 token 计费 → 成本不可控
- ✅ 本地 llama-server 跑识图 → **零费用、零隐私泄露**

### 安装

```bash
pip install -r requirements.txt
```

### 使用

```bash
python vision.py photo.jpg
python vision.py screenshot.png --prompt "分析这个 UI 界面的布局"
python vision.py receipt.jpg --prompt "提取图片中的所有文字"
```

### 安全设计

- 仅与 127.0.0.1 通信（本地）
- 不读取系统敏感目录
- 不写入任何文件（纯读取+分析）
- 不传输数据到任何第三方

---

## 项目结构

```
vision-analyzer/
├── README.md              # 本文档（安装入口）
├── AGENTS.md              # AI Agent 发现入口
├── INSTALL.md             # AI 自动安装指令
├── CLAUDE.md              # Claude Code 路由指引
├── LICENSE                # MIT 协议
├── vision.py              # ⭐ 核心：识图脚本
├── SKILL.md               # Reasonix 技能定义
├── REASONIX_CHAT_HISTORY.md # 开发记录
└── requirements.txt       # 无外部依赖
```

---

## 许可

MIT
