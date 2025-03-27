# SME AI KMGPT

## 專為中小製造企業設計的智能知識管理與檢索系統

SME AI KMGPT 是一個基於 RAG (Retrieval-Augmented Generation) 技術的智能知識管理系統，專為中小型製造企業設計。本系統能幫助企業快速整理、檢索和利用內部知識資源，提升工作效率並降低培訓成本。

### 主要功能

- **文件智能檢索**：快速從企業內部文件中找到所需資訊
- **知識庫管理**：集中管理企業各類知識文件，包括技術規範、操作手冊、培訓資料等
- **多模態支援**：處理多種類型的文件，包含圖表、表格等內容
- **精準引用**：自動提供信息來源和引用，確保回答的準確性與可追溯性
- **多用戶協作**：支援團隊同時使用與共享知識

## 啟動方式

您可以使用以下方式來啟動系統：

### 方式一：使用 Docker Compose（推薦）

只需要執行一個指令：
```bash
docker-compose up -d
```

要停止服務：
```bash
docker-compose down
```

### 方式二：手動執行 Docker 指令

如果您需要更細緻的控制，可以手動執行以下指令：

1. 建立自定義 Docker 映像檔：
```bash
docker build -t kotaemon-custom -f Dockerfile.custom .
```

2. 運行 Docker 容器：
```bash
docker run -e GRADIO_SERVER_NAME=0.0.0.0 -e GRADIO_SERVER_PORT=7860 -v ./ktem_app_data:/app/ktem_app_data -p 7860:7860 -it --rm kotaemon-custom
```

啟動後，您可以通過瀏覽器訪問 `http://localhost:7860` 開始使用系統。

## 系統需求

- 硬體建議：至少 8GB RAM，推薦 16GB 以上
- 網路連接：啟動時需要網路連接
- 支援的瀏覽器：Chrome, Firefox, Edge 最新版本
