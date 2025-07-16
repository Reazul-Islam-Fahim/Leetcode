import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager_salaries = employee.set_index('id')['salary'].to_dict()
    mask = employee['managerId'].map(manager_salaries) < employee['salary']
    result = employee.loc[mask, ['name']].rename(columns={'name': 'Employee'})
    return result
