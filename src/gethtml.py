import pandas as pd
import os
path = os.getcwd()
cols = ['timestamp', 'datetime', 'amount', 'category', 'catcode', 'description']
df = pd.read_csv(path + "/log/ledger.csv", header=None)
df.columns = cols
df.sort_values(by=['timestamp'], ascending=False, inplace=True)

df.to_html(path + "/reports/expense.html")