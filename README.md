# Weathernews
### 起動方法
仮想環境起動
.venv\Scripts\activate

起動コマンド
uvicorn backend.main:app --reload
## 「Smart App Controlが無効な環境でのみ動く」
uv run uvicorn backend.main:app --reload
# uvicorn本体ではなくPythonモジュールとして起動
.venv\Scripts\python -m uvicorn backend.main:app --reload
