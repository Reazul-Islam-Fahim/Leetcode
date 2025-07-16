def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    counts = person['email'].value_counts()
    duplicates = counts[counts > 1].index
    return pd.DataFrame(duplicates, columns=['email'])
