#Health app for measuring client's feelings about their health(exercise, consumption, etc) over time
#App: Client enters details about how they feel their personal health is that current day
#the app records the data and sends it back to us, the data we get back is organised and aesthetically visualised back to the client
#showing relationships between clients actions (exercise, consumption) and their feeling ratings for each day.
# Ques 1 answer= input("1-100")
# Ques 2,3,4 answer= input("1-100")

# each Qs A's must be recorded as separate variables
import csv
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from datetime import datetime, timedelta
from threading import Timer





# Getting Clients age
def Client_age():
    while True:
        age = input("How old are you?: ")
        if age.isdigit():
            return int(age)
        print("invalid age given")

# Getting Clients name

def Client_name():
    while True:
        name = input("Enter your name: ")
        if name:
            return name

# Getting Clients input

def inputQ1():
    while True:
        Q1A = input("Rate your exercise today on scale 1-100: ")
        if Q1A.isdigit():
            return int(Q1A)
        print("invalid value")



Client_name()
Client_age()
ansQ1 = []

i = 1
# Attempting to implement date/time for questionnaire to run
dates = []

while True:
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in dates:
        ansQ1.append(inputQ1())
        dates.append(today)
        print(ansQ1)



wb = openpyxl.load_workbook('EdProjDBeg.xlsx')
print(wb.sheetnames)
currentsheet = wb['Sheet']


ws = currentsheet
#ws = wb.active <-- defaults to first sheet

i = 0
cell_val = ''
# Finds which row is blank first
while cell_val != None:
    i += 1
    cell_val = ws['A' + str(i)].value
    print(cell_val)

x = input('Prompt: ')

#sets A column of first blank row to be user input
ws['A' + str(i)] = x

#saves spreadsheet
wb.save("sample.xlsx")