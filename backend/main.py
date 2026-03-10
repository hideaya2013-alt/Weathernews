from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.weather import router as Weather_router

#=============
#起動ファイル
#=============
app = FastAPI()

#CORS設定
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5500"],
	#allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

#ルーターのマウント
app.include_router(Weather_router)