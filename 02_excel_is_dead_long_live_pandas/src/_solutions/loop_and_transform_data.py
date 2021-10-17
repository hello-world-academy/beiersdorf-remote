dfs = []
# loop over all individual csv files
for f in filelist:
    # read the data
    df = pd.read_csv(f)
    # apply transformation
    data_transformed = transform_data(df)
    # append the dataframe to a list
    dfs.append(data_transformed)
# concatenate the dataframes
fulldata_transformed = pd.concat(dfs, axis=1)
print(fulldata_transformed.shape)
fulldata_transformed.sample(10)
