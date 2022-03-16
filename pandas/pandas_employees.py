import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')

# plot number of employees by company
df.groupby('Company Name').count()['Employee Markme'].plot(kind='bar')
plt.show()