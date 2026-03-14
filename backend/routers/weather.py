import httpx
from fastapi import APIRouter,HTTPException
from backend.schemas.weather import WeatherResponse,WeatherForecast

# ルーターを作成し、タグとURLパスのプレフィックスを設定
router = APIRouter(tags=["Weather"],prefix="/api")

#============================
#天気取得のエンドポイント
#============================
#
@router.get("/Weather",response_model=WeatherResponse)
async def get_Weather(getcityID:str): #←Swaggerのparametersに表示される
    url = f"https://weather.tsukumijima.net/api/forecast/city/{getcityID}"
    async with httpx.AsyncClient()as client:
        response = await client.get(url)
       #エラーハンドリング
        if response.status_code != 200:
            raise HTTPException(status_code=502,detail="外部APIから取得できませんでした")
       #レスポンスをjsonに変換してマッピング
        data = response.json()
        return WeatherResponse(
            city_id = getcityID,
            published_at = data["publicTime"],
            description = data["description"]["bodyText"],
            forecasts = [
            WeatherForecast(
            forecast_date = f["dateLabel"],
            condition     = f["telop"],
            high_temp     = f["temperature"]["max"]["celsius"],
            low_temp      = f["temperature"]["min"]["celsius"],
            icon_url      = f["image"]["url"],
            )
            for f in data["forecasts"]
                ]
        )
    
    #data["forecasts"]: data という変数に格納されたデータの中から、forecasts というキーに対応する値（通常は予測データのリスト）を参照します。
    #for f in ...: そのリストに含まれる各予測項目を一つずつ取り出し、一時的に変数 f に代入します。「f」はアキュムレーター
    #ループ内処理: ループの中で f を使うことで、各時間帯や各日の「気温」「天候」「降水確率」などの詳細情報にアクセスできます。 
