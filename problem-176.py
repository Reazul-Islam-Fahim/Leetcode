import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if len(distinct_salaries) < 2:
        second_highest = None
    else:
        second_highest = distinct_salaries.iloc[1]
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})
