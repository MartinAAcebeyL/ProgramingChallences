import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    employees.head(3)
