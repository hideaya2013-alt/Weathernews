# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 開発環境セットアップ

仮想環境は `.venv/` に uv で管理されている。

```bash
# 依存関係のインストール
uv pip install -r requirements.in

# ロックファイルの再生成
uv pip compile requirements.in -o requirements.lock
```

## サーバー起動

```bash
# 開発サーバー（ホットリロードあり）
.venv/Scripts/uvicorn backend.main:app --reload
uv run uvicorn backend.main:app --reload

# または
cd backend && ../.venv/Scripts/uvicorn main:app --reload
```

## アーキテクチャ

- `backend/main.py` : FastAPI アプリケーションのエントリーポイント
- `requirements.in` : 直接依存関係の定義（uv pip compile でロックファイルを生成）
- `requirements.lock` : uv が生成したロックファイル

### 主要スタック

| ライブラリ | 用途 |
|---|---|
| FastAPI + Starlette | Web フレームワーク |
| uvicorn | ASGI サーバー |
| httpx | 外部 HTTP リクエスト |
| feedparser | RSS/Atom フィード解析（Weathernews フィード取得） |
| pydantic-settings | 設定管理（`.env` 読み込み） |
| python-dotenv | 環境変数管理 |

### 想定アーキテクチャ

Weathernews の RSS フィードを feedparser で取得・解析し、FastAPI エンドポイントで提供するアプリケーション。環境変数は `.env` ファイルで管理し、pydantic-settings で型安全に扱う。
