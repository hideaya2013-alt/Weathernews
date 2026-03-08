from pydantic import BaseModel,HttpUrl;

#-----------------------------
#スキーマ定義
#-----------------------------
class WeatherForecast(BaseModel):
    forecast_date : str | None = None  #"今日"/"明日"/"明後日"
    condition : str | None = None #"晴れ"/"曇り"/"雨"
    high_temp : str | None = None #最高気温
    low_temp :  str | None = None #最低気温
    icon_url :  HttpUrl | None = None #アイコンsvg

class WeatherResponse(BaseModel):
    city_id : str | None = None
    published_at : str | None = None #発表時刻
    description : str | None = None #概況文
    forecasts : list[WeatherForecast]