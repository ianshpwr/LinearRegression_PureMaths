import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('score_updated.csv')

plt.scatter(data.Hours , data.Scores)
plt.show()