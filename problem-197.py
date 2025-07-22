import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather = weather.sort_values('recordDate')
    weather['prevDate'] = weather['recordDate'].shift(1)
    weather['prevTemp'] = weather['temperature'].shift(1)
    mask = (weather['recordDate'] - weather['prevDate']).dt.days == 1
    result = weather[mask & (weather['temperature'] > weather['prevTemp'])]
    return result[['id']]
