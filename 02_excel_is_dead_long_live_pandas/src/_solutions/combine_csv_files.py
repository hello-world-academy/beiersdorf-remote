dfs = []
for f in filelist:
    # read the data
    df = pd.read_csv(f)
    # append dataframes to a list
    dfs.append(df)
# concatenate the dataframes
fulldata = pd.concat(dfs)
print(fulldata.shape)
fulldata.sample(10)
