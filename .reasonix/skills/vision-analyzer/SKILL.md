---
name: vision-analyzer
description: 本地识图工具 —— 图片发给本地 llama-server 进行视觉识别，零费用，零隐私泄露
runAs: inline
---

## 概述

本地识图工具 —— 图片发给本地 llama-server 进行视觉识别，零费用，零隐私泄露

---

## 使用方式

```
/vision-analyzer
```

---

## 执行指令

### 用户发图时

1. Reasonix 检测到图片附件
2. 调用 vision.py，传入图片路径
3. vision.py 将图片 base64 编码后发送到本地 llama-server（127.0.0.1:8080）
4. 本地模型识别图片内容
5. 返回文字描述给用户

### 部署要求

- 本地运行 llama-server，需加载 mmproj 视觉投影文件
- Python 3.8+
- 无需任何 API Key
