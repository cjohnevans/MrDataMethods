import pandas as pd
import datetime as dt
bbbcov = pd.read_csv('bbbcov_xnat.csv',sep=',')
xnatdate = bbbcov['Date']
xnatdate = xnatdate.apply(dt.datetime.fromisoformat)
bbbcov = bbbcov.drop('Date', axis='columns')
bbbcov = bbbcov.drop('Age', axis='columns')
bbbcov = bbbcov.drop('Scanner', axis='columns')
bbbcov['Date'] = xnatdate
# drop duplicates
bbbcov = bbbcov.drop([29,37], axis='index')

# bool Series of participants, filtering typos and pilots 
isppt=bbbcov['Subject'].str.contains('CAU002N0')
ismrs=bbbcov['Scans'].str.contains('Brainstem')
isafteraug=bbbcov['Date'] > dt.datetime(2022,8,31)

ispptafteraug = isppt&isafteraug
ispptafteraugwithmrs = isppt&isafteraug&ismrs

bbbcov['Study ppt']=isppt
bbbcov['Has data']=ismrs
bbbcov['After Aug']=isafteraug

newcolumns = ['Date', 'Subject', 'Study ppt', 'Has data', 'After Aug', 'MR ID', 'Scans']
bbbcov = bbbcov.reindex(columns=newcolumns)

bbbcov_out = bbbcov[['Date', 'Subject','Study ppt','Has data','After Aug']]

display(bbbcov_out)                    
display(bbbcov_out[['Study ppt', 'Has data', 'After Aug']].value_counts())
