from pandas_profiling import ProfileReport
profile = ProfileReport(data, title="The Beiersdorf spreadsheet challenge", minimal=True)
profile.to_notebook_iframe()
