import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("toilet_usage.csv")

data['hour'] = pd.to_datetime(data['time']).dt.hour

hourly = data.groupby('hour')['users'].sum()
print(hourly)
plt.plot(hourly.index, hourly.values)
plt.xlabel("Hour")
plt.ylabel("Users")
plt.title("Public Toilet Usage")
plt.show()
