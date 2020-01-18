import numpy
import pandas
#%matplotlib notebook
import matplotlib.pyplot as plt
import scipy.stats
from pandas.plotting import autocorrelation_plot
import matplotlib.offsetbox as offsetbox
from matplotlib.ticker import StrMethodFormatter as StrMethodFormatter
idx=pandas.IndexSlice
from pandas import DataFrame

DATA = pandas.read_csv('Clean Database.csv')

items = ['a','b','c','d','e','f','g','h','i','j']

pre_all = DATA.loc[DATA['Exposure'] =='Pre']
post_all = DATA.loc[DATA['Exposure'] =='Post']

pvals = pandas.DataFrame(columns = ['Item', 'Time', 'Fixations', 'Duration'])

for item in items:
    pre_item = pre_all.loc[pre_all['Item'] == item]
    post_item = post_all.loc[post_all['Item'] == item]
    
    utime_item = str(scipy.stats.mannwhitneyu(pre_item['Time'],post_item['Time'],use_continuity = True,alternative = 'greater')) 
    ufixations_item = str(scipy.stats.mannwhitneyu(pre_item['Fixations'],post_item['Fixations'],use_continuity = True,alternative = 'greater'))
    uduration_item = str(scipy.stats.mannwhitneyu(pre_item['Duration'],post_item['Duration'],use_continuity = True,alternative = 'less'))
    
    pvtime_item = float(((utime_item.partition("pvalue="))[2]).partition(")")[0])
    pvfixations_item = float(((ufixations_item.partition("pvalue="))[2]).partition(")")[0])
    pvduration_item = float(((uduration_item.partition("pvalue="))[2]).partition(")")[0])
    
    #keeping letters good idea?
    pvals_item = pandas.DataFrame([[item, pvtime_item, pvfixations_item, pvduration_item]],columns = ['Item', 'Time', 'Fixations', 'Duration'])
    pvals = pandas.concat([pvals, pvals_item], axis=0)
    
  pvals
  
UTime = str(scipy.stats.mannwhitneyu(pre_all['Time'],post_all['Time'],use_continuity = True,alternative = 'greater'))
UFixations = str(scipy.stats.mannwhitneyu(pre_all['Fixations'],post_all['Fixations'],use_continuity = True,alternative = 'greater'))
UDuration = str(scipy.stats.mannwhitneyu(pre_all['Duration'],post_all['Duration'],use_continuity = True,alternative = 'less'))
print(UTime)
print(UFixations)
print(UDuration)
