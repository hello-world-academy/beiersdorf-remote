import matplotlib.pyplot as plt
plt, ax = plt.subplots(figsize=(13,5))
fulldata_transformed.cumsum().plot(ax=ax)
ax.grid()
ax.set_ylabel("Success", size=11)
ax.set_title("The Beiersdorf spreadsheet challenge", size=22);
