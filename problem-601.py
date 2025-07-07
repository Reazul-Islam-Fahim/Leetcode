import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium[stadium['people'] >= 100]
    stadium = stadium.sort_values('id')
    stadium['grp'] = stadium['id'].values - pd.RangeIndex(len(stadium))
    group_sizes = stadium.groupby('grp')['id'].transform('size')
    result = stadium[group_sizes >= 3]
    return result.sort_values('visit_date')[['id', 'visit_date', 'people']]
