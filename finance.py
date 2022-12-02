import pandas as pd
import numpy as np
import datetime
import os

bank = {
    'sbi':30000.70,
    'fed':15549.57,
    'uco':5000.08,
    'hdfc':12501.00,
    'ubi':10000.71,
    'ippb':500.00,
    'posb':11582.46,
    'cash':100,
    'lent':16000.0
}
credit = {
    'onecard':0,
    'icici':25000.0-21904.35,
    'lazypay':0,
    'paytmpl':0,
    'amazonpl':0,
    'personal':0
}
goldrate = 53120.0  #https://ibjarates.com
silverrate = 63683.0
assets = {
    'elss':31751.00,
    'index':5000.00,
    'gold':2 * goldrate / 10,
    'silver':20 * silverrate / 1000,
    'fd':15000
}

rent = 15977.70
budget = 63000

bank_mab = 16000
in_hand = 70981.00



path = os.getcwd()
cols = ['timestamp', 'datetime', 'amount', 'category', 'catcode', 'description']
essentials = 0
expense_report = ""
file = open('financials.txt', 'w')
df = pd.read_csv(path + "/log/ledger.csv", header=None)

# GET DATA

df.columns = cols
for i in np.unique(df.category.values):
    expense_report = expense_report + f"{i} : {np.sum(df.loc[df.category==i].amount.values)}\n"
    if i in ['Food', 'Groceries', 'Transport']:
        essentials = essentials + np.sum(df.loc[df.category==i].amount.values)
left = budget - np.sum(df.amount.values)
mon = pd.Period(datetime.datetime.now().date().strftime("%Y-%m-%d")).days_in_month
daysleft = mon - datetime.datetime.now().date().day
# daysleft = 31

# CALCULATE FINANCES

investments = sum(assets.values())
liabilities = sum(credit.values())
eom = sum(bank.values()) - liabilities - left - bank_mab
report = f"""EXPENSE REPORT

{expense_report}

BUDGET : {budget}
ESSENTIALS : {essentials} + {rent} = {essentials + rent}
REST : {np.sum(df.amount.values) - essentials - rent}
TOTAL : {np.sum(df.amount.values)}
LEFT: {left}
DAYS LEFT: {str(daysleft)}
BUDGET: {str(left/daysleft)}/day

NETWORTH : {sum(bank.values()) - liabilities + investments}
LIQUID : {sum(bank.values()) - liabilities - bank_mab}

NETWORTH AT END OF MONTH : {eom + investments + bank_mab}
LIQUID AT END OF MONTH : {eom}
LIQUID CONTRIBUTION : {in_hand - budget}

Assets in bank:\t\t\tInvestments:
SBI : {bank['sbi']}\t\t\tELSS : {assets['elss']}
FED : {bank['fed']}\t\t\tINDX : {assets['index']}
POS : {bank['posb']}\t\t\tGOLD : {assets['gold']}
UCO : {bank['uco']}\t\t\tSILV : {assets['silver']}
HDF : {bank['hdfc']}\t\t\tFD   : {assets['fd']}
UBI : {bank['ubi']}
CSH : {bank['cash']}
LNT : {bank['lent']}
TOTAL : {sum(bank.values())}\t\tTOTAL : {investments}

Liabilities:
SBM 1 CC : {credit['onecard']}
ICICI CC : {credit['icici']}
AMAZN PL : {credit['amazonpl']}
LZYPY PL : {credit['lazypay']}
PAYTM PL : {credit['paytmpl']}
PRSNL LN : {credit['personal']}
TOTAL : {liabilities}
"""

file.write(report)
file.close()
# print(report)