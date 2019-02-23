
import os

from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
from matplotlib_venn import venn3



file='venn.xlsx'


# get the list of genes that are DE in two or more methods when only two replicates were analyzed

def sheet1(file1):
    xls = pd.ExcelFile(file1)
    df1 = pd.read_excel(xls, 'Sheet1')# pd.read_excel(xls, 'Sheet1', skiprows=1) if want to skip the rows
    df11 = df1[df1.padj <0.05] # get the df with padj < 0.05
    nm = list(df1['test_id']) # get the 1st col
    nm_list =  [i.encode('ascii', 'ignore') for i in nm] # ignore ascii
    return nm_list

# get the DE genes from deseq2 method when only two replicates were analyzed
def sheet2(file1):
    xls = pd.ExcelFile(file1)
    df1 = pd.read_excel(xls, 'Sheet2')
    df11 = df1[df1.padj <0.05]
    nm = list(df11['test_id'])
    nm_list =  [i.encode('ascii', 'ignore') for i in nm]
    return nm_list

def sheet3(file1):
    xls = pd.ExcelFile(file1)
    df1 = pd.read_excel(xls, 'Sheet3')
    df11 = df1[df1.padj <0.05]
    nm = list(df11['test_id'])
    nm_list =  [i.encode('ascii', 'ignore') for i in nm]
    return nm_list  

def plot(one, two, three):
    figure = plt.figure()
    a = set(one)
    b = set(two)
    c = set(three)
    v1 = venn3([a,b,c], ('One','Two', 'Three'))
    plt.title('Venn')
    plt.savefig('fig.png')
    #plt.show()


first = sheet1(file)
second = sheet2(file)
third = sheet3(file)

print first
print second
print third
plot(first, second, third)
