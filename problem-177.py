import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    output_column_name = f'getNthHighestSalary({N})'
    
    if N <= 0:
        return pd.DataFrame({output_column_name: [None]})

    distinct_salaries = employee['salary'].drop_duplicates()
    if len(distinct_salaries) < N:
        return pd.DataFrame({output_column_name: [None]})

    nth_salary_series = distinct_salaries.nlargest(N)
    result_salary = nth_salary_series.iloc[-1]

    return pd.DataFrame({output_column_name: [result_salary]})
