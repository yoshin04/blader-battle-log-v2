# ブレーダーバトルログ

ベイブレードの対戦データを分析し、次の対戦相手の使用ベイを予測するシステム

## 技術スタック

### バックエンド
- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- scikit-learn

### フロントエンド 
- Next.js 14
- TypeScript
- TailwindCSS
- React Query

## 開発環境構築

### 必須環境
- Docker
- Docker Compose

### セットアップ手順
1. リポジトリをクローン
```bash
git clone https://github.com/your-repo/beyblade-predictor.git
cd beyblade-predictor
```

2.環境変数の設定
```
cp .env.example .env
```

3. アプリケーションの起動
```
docker-compose up --build
```

4. アクセス
* フロントエンド: http://localhost:3000
* バックエンドAPI: http://localhost:8000
* API Docs: http://localhost:8000/docs
