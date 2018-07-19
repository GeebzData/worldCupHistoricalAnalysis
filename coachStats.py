import pandas as pd
import re
import numpy as np

wcm = pd.read_csv("/Users/geebz/Documents/fifa-world-cup/WorldCupMatches.csv", index_col=0)
wcp = pd.read_csv("/Users/geebz/Documents/fifa-world-cup/WorldCupPlayers.csv", index_col=0)
wc = pd.read_csv("/Users/geebz/Documents/fifa-world-cup/WorldCups.csv", index_col=0)

list = []

for x in wcp['Coach Name']:
    country = re.split('\W+', x)[-2]
    list.append(country)

wcp['Coach_Country'] = list

homeCoaches = wcp.loc[(wcp['Team Initials']==wcp['Coach_Country'])]
nonHomeCoaches = wcp.loc[(wcp['Team Initials']!=wcp['Coach_Country'])]

hc = len(homeCoaches['Coach Name'])
nhc = len(nonHomeCoaches['Coach Name'])
total = len(wcp['Coach Name'])

print("Percent of coaches from national country " +str(round(((hc/total)*100),2)) + "%")
print("Percent of coaches not from national country " +str(round(((nhc/total)*100),2)) + "%")
