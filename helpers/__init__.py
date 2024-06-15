def add_constant_column(df):
    """
    Adds a constant column 'const' with value 1 as the first column to the DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    
    Returns:
    pd.DataFrame: DataFrame with the added constant column as the first column.
    """
    # Create a new DataFrame to avoid modifying the original DataFrame
    df_with_const = df.copy()
    
    # Add a constant column with value 1
    df_with_const.insert(0, 'const', 1)
    
    return df_with_const