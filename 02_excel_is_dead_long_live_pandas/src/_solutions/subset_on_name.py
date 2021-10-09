for name in data.Name.unique():
    print(f'Computing {name} ...')
    subset = data.loc[data.Name == name]
    fname = f'subset_{name.replace(" ", "_")}.csv'
    filepath = os.path.join('..', 'data', 'interim', fname)
    subset.to_csv(filepath, index=False)
