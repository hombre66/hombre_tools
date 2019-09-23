import pandas as pd
import pandas_profiling as pp
df = pd.read_csv(r'C:\Users\stanislav_vohnik\Documents\Data\GSR1.csv',delimiter=';', parse_dates=['GL DateGL DateGL Date'])
df = df.replace(to_replace=r',', value='.', regex=True)
df = df.replace(to_replace=r'/', value='', regex=True)
for col in df.filter(regex='^Measure').columns:
    df[col] = df[col].astype('float64')
    
pp.ProfileReport(df)