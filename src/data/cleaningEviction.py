# -*- coding: cp1252 -*-
import pandas as pd
import numpy as np

df=pd.read_csv("Eviction_Notices.csv")
print(df)
df=df.drop('Constraints Date',1)
df['Location'].dtypes
df['Location'] = df['Location'].astype(str)
df.dtypes
df['Location'] = df['Location'].str.extract(r"\((.*?)\)", expand=False)
df.head(10)
new = df["Location"].str.split(" ", n = 1, expand = True)
df["X"]= new[0]
df["Y"]=new[1]
df.head(10)
df.dtypes
nan_rows = df[df['X'].isnull()]
df = df[pd.notnull(df['X'])]
nan_rows = df[df['City'].isnull()]
df['City']= "San Francisco"
df['State']= "CA"
df.isna().any()
nan_rows = df[df['Eviction Notice Source Zipcode'].isnull()]
df.dropna(inplace=True)
df.isna().any()
df.rename(columns = {'Eviction ID': 'EvictionID','Address':'Address', 'City':'City',
                              'State':'State', 'Eviction Notice Source Zipcode': 'Zipcode', 'File Date': 'Date', 'Location': 'Location', 'Neighborhoods - Analysis Boundaries': 'Neighborhoods','Ellis Act WithDrawal': 'Withdrawl','Condo Conversion': 'Condoconversion','Roommate Same Unit':'Roomate','Other Cause':'Other','Late Payments':'LatePayments','Lead Remediation': 'LeadRemediation','Development': 'Development','Good Samaritan Ends':'GoodSamaritanEnds','Supervisor District':'SupervisorDistrict', 'Access Denial': 'AccessDenial','Unapproved Subtenan':'UnapprovedSubtenan','Owner Move In':'OwnerMoveIn','Demolition': 'Demolition','Capital Improvement':'CapitalImprovement','Substantial Rehab': 'Rehab', 'Non Payment': 'Nonpayment','Breach': 'Breach','Nuisance': 'Nuisance','Illegal Use': 'IllegalUse','Failure to Sign Renewal':'FailureToSign'}, inplace = True)
df.head(10)
df['Zipcode'] = df["Zipcode"].astype(int)
df['X'] = df["X"].astype(float)
df['Y'] = df["Y"].astype(float)
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = pd.DatetimeIndex(df['Date']).day
df['Month'] = pd.DatetimeIndex(df['Date']).month
df['Year'] = pd.DatetimeIndex(df['Date']).year
df.dtypes
df=df.sort_values(by='Year',ascending=False)
df=df.reset_index(drop=True)
df=df.apply(lambda x: x.astype(str).str.lower())
df.to_csv('../../data/processed/Eviction.csv', index = None, header=True)