---
name: vision-analyzer
description: 本地识图工具 —— 调用本地 llama-server 进行视觉识别，零费用，零隐私泄露
runAs: inline
---

## 概述

发送图片到本地 llama-server 进行视觉识别，返回文字描述。不依赖任何云端 API。

---

## 使用方式

拖入图片后说"识别一下这张图"，skill 自动调用 vision.py 完成识图。

---

## 执行指令

### Step 1: 确保 vision.py 可用

检查 skill 目录下是否有 `vision.py`，如果缺失则从 GitHub 下载：

```bash
cd ~/.reasonix/skills/vision-analyzer

# 检查 vision.py 是否存在
if [ ! -f vision.py ]; then
  curl -f -o vision.py \
    https://raw.githubusercontent.com/Kepsilent/vision-analyzer/master/vision.py
  echo "vision.py downloaded"
fi
```

### Step 2: 获取图片路径

用户可能在聊天中上传图片或指定文件路径。AI 需要：
- 如果用户拖入了图片附件 → 获取该图片的本地路径
- 如果用户说"识别 xxx.jpg" → 使用指定的文件路径
- 如果用户未指定 → 提示用户上传图片或提供路径

### Step 3: 执行识图

```bash
python vision.py "<图片路径>"
```

支持自定义提示词：

```bash
python vision.py "<图片路径>" --prompt "分析这个 UI 界面的布局和设计"
```

### Step 4: 展示结果

将 vision.py 输出的文字反馈给用户。如果返回以 "Error:" 开头的内容，则告知用户错误原因，并给出排查建议。

---

## 常见错误处理

| 错误 | 原因 | 解决 |
|------|------|------|
| `Cannot reach llama-server` | llama-server 未启动 | 启动 llama-server 并确保端口 8080 |
| `Unsupported file type` | 图片格式不支持 | 支持 jpg / png / webp / gif / bmp |
| `Empty response` | 模型未加载 mmproj | 重启 llama-server 并加载 mmproj |
| `Permission denied` | 文件无读取权限 | 检查文件权限 |

---

## 部署要求

- 本地运行 llama-server，需加载 mmproj 视觉投影文件
- Python 3.8+
- 无需任何 API Key
