import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid_data_us.csv',skiprows=2)

# scale down data by dividing by 1000
df['New Cases'] = df['New Cases']//1000
df['7-Day Moving Avg'] = df['7-Day Moving Avg']//1000
df['Historic Cases'] = df['Historic Cases']//1000

df.plot(kind='bar')
plt.show()