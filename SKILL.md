---
name: vision-analyzer
description: 本地识图工具 —— 调用本地 llama-server 进行视觉识别，零费用，零隐私泄露
runAs: inline
---

## 用途
发送图片到本地 llama-server 进行视觉识别，返回文字描述。不依赖任何云端 API。

## 适用场景
- 设计软件时分析 UI 截图
- 识别照片中的物体、文字、场景
- 配合 DeepSeek V4 Pro 使用 —— 识图走本地模型，对话走云端模型

## 使用方式
拖入图片后说"识别一下这张图"即可，skill 自动调用 vision.py 完成识图。

## 工作流程
1. Reasonix 检测到图片附件
2. 调用 vision.py，传入图片路径
3. vision.py 将图片 base64 编码后发送到本地 llama-server（127.0.0.1:8080）
4. 本地模型识别图片内容
5. 返回文字描述给用户

## 部署要求
- 本地运行 llama-server，需加载 mmproj 视觉投影文件
- Python 3.8+
- 无需任何 API Key
