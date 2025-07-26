import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    result = activity.groupby('player_id', as_index=False)['event_date'].min()
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    return result
