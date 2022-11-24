import pandas as pd
import numpy as np
import datetime
import os

elss = 31079.00
gold = 2
silver = 20
bank = {
    'sbi':20000.70,
    'fed':3640.65,
    'uco':5000.08,
    'hdfc':12000.00,
    'ubi':6000.71,
    'ippb':1000.00,
    'posb':1040.46,
    'cash':590,
    'lent':21500.0
}
credit = {
    'onecard':467.95-1985-159,
    'icici':25000.0-10567.29-8147.86-445,
    'lazypay':1407.0,
    'amazonpl':655.0-655,
    'personal':653.5-0-446.66
}
rent = 15977.70
budget = 63000
fd = 15000.00
goldrate = 52713.0  #https://ibjarates.com
silverrate = 62266.0
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

# CALCULATE FINANCES

goldworth = gold * goldrate / 10
silverworth =  silver * silverrate / 1000
investments = goldworth + silverworth + elss + fd
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
SBI : {bank['sbi']}\t\t\tELSS : {elss}
FED : {bank['fed']}\t\t\tGOLD : {goldworth}
POS : {bank['posb']}\t\t\tSILV : {silverworth}
UCO : {bank['uco']}\t\t\tFD   : {fd}
HDF : {bank['hdfc']}
UBI : {bank['ubi']}
CSH : {bank['cash']}
LNT : {bank['lent']}
TOTAL : {sum(bank.values())}\t\tTOTAL : {investments}

Liabilities:
SBM 1 CC : {credit['onecard']}
ICICI CC : {credit['icici']}
AMAZN PL : {credit['amazonpl']}
LZYPY PL : {credit['lazypay']}
PRSNL LN : {credit['personal']}
TOTAL : {liabilities}
"""

file.write(report)
file.close()
# print(report)