from pandas import Series, DataFrame
import pandas as pd
from openpyxl import load_workbook



def readData(name):
    rawData = pd.read_csv('%s.csv'% name)
    
    return rawData
