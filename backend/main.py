from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.routers.weather import router as Weather_router

#=============
#起動ファイル
#=============
app = FastAPI()

#=============
#静的ファイルの配信　8000から配信される場合、_common /frontendを静的ファイルとしてmountする
#=============
app.mount("/frontend",StaticFiles(directory="frontend"),name="frontend")
app.mount("/_common", StaticFiles(directory="_common"), name="common")


@app.get("/")
async def root():
    return FileResponse("index.html")

#CORS設定
#app.add_middleware(
#	CORSMiddleware,
#	allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
#	allow_credentials=True,
#	allow_methods=["GET"],
#	allow_headers=["*"],
#)

#ルーターのマウント
app.include_router(Weather_router)