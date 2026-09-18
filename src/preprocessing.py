import pandas as pd

def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Hər sütunda neçə missing dəyərin olduğunu yoxlayır.
    """
    return df.isnull().sum().to_frame(name='missing_values').sort_values(by='missing_values', ascending=False)

def remove_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    DataFrame-dəki missing dəyərləri silir.
    """
    df = df.copy()
    before = len(df)
    df = df.dropna()
    print(f"Removed {before - len(df)} rows with missing values.")
    return df

def check_duplicates(df: pd.DataFrame) -> int:
    """
    DataFrame-də neçə təkrarlanan sətrin olduğunu yoxlayır.
    """
    return df.duplicated().sum()



def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    DataFrame-dəki təkrarlanan sətrləri silir.
    """
    df = df.copy()
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows.")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bütün təmizləmə addımlarını birləşdirir.
    """
    df = df.copy()
    df = remove_missing_values(df)
    df = remove_duplicates(df)
    return df