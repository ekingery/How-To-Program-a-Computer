import os
import forecastio


def get_weather(date_to_display):
    # Dark Sky API Key
    api_key = os.environ.get('DARKSKY_API_KEY')
    if api_key is None:
        return None
    lat = 41.9030703
    lon = -87.8006613
    try:
        forecast = forecastio.load_forecast(api_key, lat, lon)
    except Exception as e:
        msg = 'Exception: ' + str(e) + ' attempting to load forecast.'
        print(msg)
        return None
    return forecast
