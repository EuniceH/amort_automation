#import Libraries
import pandas as pd
import datetime as dt
from datetime import date, timedelta,datetime
from pandas.tseries.offsets import MonthEnd
from dateutil.relativedelta import relativedelta
import numpy as np


#EH:  set import sales function for amortization
def import_data(file_path):
    #import data from path
    import_sales=pd.read_csv(file_path)

 
    #update column data to datetime
    import_sales.loc[:,['schedule_month','sales_month','amrt_start_month']]=import_sales.loc[:,['schedule_month','sales_month','amrt_start_month']].astype('datetime64')



    # import_sales['schedule_month']= import_sales['schedule_month'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    #get last date of month
    import_sales['schedule_month']=import_sales['schedule_month']+MonthEnd(0)
    
    #update datatype
    import_sales['amrt_period']=import_sales['amrt_period'].astype('float64')
    #set beginning bal
    import_sales['beg_bal']=import_sales['sales_amt']
    
    #set amort end date series
    end_date_s=import_sales.apply(lambda x: x['amrt_start_month']+pd.DateOffset(months=x['amrt_period']),axis=1)
    
    #get the max amort end date
    max_enddate=end_date_s.max()
    
    return import_sales,max_enddate


#EH:  function to render remainder, end bal and monthly amort

def amort_cal(df):
    #calculate remainder numbers of month
    df['remainder']=df['amrt_period']-(df['schedule_month'].dt.year-df['amrt_start_month'].dt.year)*12-(df['schedule_month'].dt.month-df['amrt_start_month'].dt.month)-df['amrt_factor']
    #update remainder for negative value
    df.loc[df['remainder']<0,'remainder']=0
    #add end bal column
    df['end_bal']=round(df['remainder']*df['sales_amt']/df['amrt_period'],2)
    #add monthly amort column
    df['monthly_amort']=round(df['beg_bal']-df['end_bal'],2)
    
    return df


#EH:  function to carry end bal/lines to beg bal of next month schedule

def carryover(df):
    
    #copy from existing schedule
    carryover_df=pd.concat([df.iloc[:,0:8],df['end_bal']],axis=1)
    #update schedule month
    carryover_df['schedule_month']=carryover_df['schedule_month']+MonthEnd(1)
    #rename columns
    carryover_df.rename(columns={'end_bal':'beg_bal'},inplace=True)
    
    #drop row with zero beginning balance
    carryover_df.drop(carryover_df[carryover_df['beg_bal']==0].index,axis=0,inplace=True)
    return carryover_df



#EH: create amort rollforward schedule of sales record

def rollforward_df(df,end_date):
    rollforward=pd.DataFrame(columns=['schedule_month','sales_month','source','material#','sales_amt','amrt_start_month','amrt_period','amrt_factor','beg_bal','remainder','end_bal','monthly_amort'])

    schedule_holder=df.copy()
    while schedule_holder['schedule_month'].max()<=end_date:
        amort_cal_df=amort_cal(schedule_holder)
        rollforward=pd.concat([rollforward,amort_cal_df],axis=0,ignore_index=True)
        schedule_holder=carryover(amort_cal_df)

    return rollforward


#EH:  consolidate multiple rollforward schedules

def master_schedule(df1,df2):

    master_schedule=pd.concat([df1,df2],axis=0,ignore_index=True)
    return master_schedule


