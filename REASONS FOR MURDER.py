# -- coding: utf-8 --
"""
Created on Fri Mar  3 17:20:40 2023

@author:OLAJIDE STEPHEN WALE-ONI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 # Read the dataset into a Pandas dataframe
df_murder = pd.read_csv(r"C:\Users\User\OneDrive - University of Hertfordshire\Desktop\REASONS FOE MURDER IN INDIA\Murder Motives.csv")
print(df_murder)

df_murder = df_murder[['YEAR', 'Property Dispute', 'Lunacy', 'Terrorists/ Extremists']]
print(df_murder) 

df_murder=df_murder.groupby('YEAR').sum()
print(df_murder)

def line_plot(x, y, xlabel, ylabel, title, label='', **others):
    """
    Plot a line graph using matplotlib
    """
    plt.plot(x, y, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.savefig("Reasons for murder in India.PNG")
 

  

    
line_plot(df_murder.index, df_murder['Lunacy'], 'Year', 'Murder Cases', 'Reasons for Murder in India', 'LUNACY')
line_plot(df_murder.index, df_murder['Property Dispute'], 'Year', 'Murder Cases', 'Reasons for Murder in India','PROPERTY DISPUTE' )
line_plot(df_murder.index, df_murder['Terrorists/ Extremists'], 'Year', 'Murder Cases', 'Reasons for Murder in India','TERRORISTS AND EXTREMISTS' )

plt.show()

def bar_chart(i, j, xlabel, ylabel, title):
    
    plt.figure()
    plt.bar(i,j)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig("murder reason distribution bar chat.png")
    plt.show()
    
YEAR = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
Murder_reasons = [ 14496,1376, 13218,12558,11628,10866,10740,10341,10335,11001,11355,10530,9234]
    
bar_chart(YEAR,Murder_reasons, 'year', 'murder cases', 'REASONS FOR MURDER IN INDIA' )

def pie_chart(labels, values, title):
    """
    Plot a pie chart using matplotlib
    """
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.legend(loc="best")
    plt.axis('equal')
    plt.savefig("murder reason distribution")
    plt.show()
    
murder_reasons = ['Property Dispute', 'Lunacy', 'Terrorists/ Extremists']
no_of = np.array([117018, 2019, 31041])
total_murders_by_year = np.sum(df_murder, axis=0)
print(total_murders_by_year)

pie_chart(murder_reasons, no_of, "Distribution of Deaths by Murder Reason In India")
