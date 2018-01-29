import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('task31_data.csv')

#Prepare data
us_spending = data.iloc[0][1:]
us_spending_year = np.array(us_spending.index).astype(np.int)
us_spending_amt = us_spending.values
suicide = data.iloc[1][1:]
suicide_year = np.array(suicide.index).astype(np.int)
suicide_amt = suicide.values

#Create figure
fig = plt.figure(figsize=(20,10))
ax1 = plt.gca()
line1, = ax1.plot(us_spending_year, us_spending_amt, c='g')
ax2 = ax1.twinx()
line2, = ax2.plot(suicide_year, suicide_amt, c='r')
plt.legend((line1,line2),("US spending on science, space, and technology",
                          "Suicides by hanging, strangulation and suffocation"), loc = 2)
ax1.set(title = "US spending on science, space, and technology \n correlates with \n suicides by hanging, strangulation and suffocation",
        ylabel = "US Spending (million USD)")
ax2.set(ylabel = "Deadths (US)")
ax1.set_ylim(18000,30000)
ax1.set_xlim(1999,2009)
ax2.set_ylim(5000,9000)

plt.savefig('task31.png')
plt.show()