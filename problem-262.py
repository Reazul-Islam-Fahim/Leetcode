import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips['request_at'] = pd.to_datetime(trips['request_at'])
    
    start_date = '2013-10-01'
    end_date = '2013-10-03'
    filtered_trips = trips[
        (trips['request_at'] >= start_date) & 
        (trips['request_at'] <= end_date)
    ].copy()
    
    unbanned_clients = set(users.loc[(users['banned'] == 'No') & (users['role'] == 'client'), 'users_id'])
    unbanned_drivers = set(users.loc[(users['banned'] == 'No') & (users['role'] == 'driver'), 'users_id'])
    
    filtered_trips = filtered_trips[
        (filtered_trips['client_id'].isin(unbanned_clients)) &
        (filtered_trips['driver_id'].isin(unbanned_drivers))
    ].copy()
    
    filtered_trips['Day'] = filtered_trips['request_at'].dt.strftime('%Y-%m-%d')
    
    cancelled_mask = filtered_trips['status'].isin(['cancelled_by_client', 'cancelled_by_driver'])
    
    result = filtered_trips.groupby('Day').agg(
        total_requests=('id', 'count'),
        cancelled_requests=('status', lambda x: x.isin(['cancelled_by_client', 'cancelled_by_driver']).sum())
    ).reset_index()
    
    result['Cancellation Rate'] = (result['cancelled_requests'] / result['total_requests']).round(2)
    
    return result[['Day', 'Cancellation Rate']]
