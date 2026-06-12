# vision-analyzer Skill — 开发对话记录

> 与 Reasonix AI 协作完成，2026-06-11 ~ 2026-06-12

---

## 项目背景

用户已部署本地 llama.cpp 服务（Qwen3.6-35B-A3B，Q5_K_P 量化，27GB），运行在 RTX 3060 12GB + i5-12400F 32GB RAM 上。Reasonix 桌面版支持自定义模型配置，但不支持原生的多模态图片请求。

目标：让 Reasonix 能调用本地模型进行识图，无需任何云端 API。

## 技术方案

- **核心脚本** `vision.py`：读取图片 → base64 编码 → 发送到本地 llama-server 视觉 API → 返回结果
- **Skill 封装** `SKILL.md`：Reasonix 检测图片附件时自动触发识图流程
- **安全设计**：仅 127.0.0.1 通信，只读不写，不传输任何数据给第三方

## 文件清单

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Reasonix 技能定义，YAML 头部 + 使用说明 |
| `vision.py` | 识图核心脚本，纯 Python 标准库，无外部依赖 |
| `README.md` | 开源文档，含安装、使用、树莓派部署指南 |
| `LICENSE` | MIT 协议 |
| `requirements.txt` | 无外部依赖 |

## 工作流程

```
用户发图 → Reasonix 检测图片
  → 触发 vision-analyzer skill
    → vision.py base64 编码图片
      → POST http://127.0.0.1:8080/v1/chat/completions（vision 格式）
        → 本地模型识别 → 返回文字描述
          → Reasonix 展示结果
```

## 技术细节

- **API 格式**：OpenAI vision-compatible `image_url` with `data:image/*;base64,...`
- **支持格式**：jpg, jpeg, png, webp, gif, bmp
- **大小限制**：单张最大 20MB
- **超时**：120 秒
- **依赖**：Python 3.8+，无 pip 外部依赖

## 适用场景

- 设计软件时分析 UI 截图
- 识别照片中的物体、文字、场景
- 配合 DeepSeek V4 Pro 使用（识图走本地模型，对话走云端）

## 安全措施

- 仅与本机 127.0.0.1:8080 通信
- 不读取系统敏感目录
- 不写入任何文件（纯读取+分析）
- 文件类型白名单校验
- 文件大小上限检查（20MB）
- 权限异常捕获

## 部署路径

| 路径 | 用途 |
|------|------|
| `D:\wanjie\Documents\Github\vision-analyzer\` | 源码仓库 |
| `D:\wanjie\Documents\Reasonix\.reasonix\skills\vision-analyzer\` | Reasonix Skill 安装 |

## GitHub

- 账号：Kepsilent
- 仓库：vision-analyzer（待推送）
- 协议：MIT

---

*此项目由用户与 Reasonix AI Agent 协作完成。*
