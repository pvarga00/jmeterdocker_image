## IMPORTS
import csv, sys, fnmatch, os, webbrowser
import texttable
import xml.etree.ElementTree as ET

t = texttable.Texttable()

# GET TEST DURATION
resultsxml = open('results.xml')
tree = ET.parse(resultsxml)
root = tree.getroot()
testduration = int(float(root.find('TestDuration').text))
resultsxml.close()

t.add_rows([['Transaction name', 'Response time (s)', 'Passed', 'Failed', 'Transaction / second']])
resultscsv = ('results.csv')
with open(resultscsv, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if(len(row['label'])):
            t.add_row([row['label'], row['avg_rt'], row['succ'], row['fail'], float(row['succ'])/testduration])

print(t.draw())
