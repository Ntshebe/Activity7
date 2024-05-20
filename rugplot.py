import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Admin/Documents/My Modules/Technical Programing 2/dataset - 2020-09-24.csv")

selected = df.iloc[0:5]

sns.rugplot(selected.Age, alpha=0.5)
plt.show()