def transform_data(df):
    """Function to transform the Beiersdorf fake dataset"""
    df = df.copy()
    df.Date = pd.to_datetime(df.Date) 
    df = df.set_index('Date')
    name = df.Name.unique()
    df[name] = df['Success']
    return df[name].groupby(pd.Grouper(freq='1D')).sum().astype(float)
