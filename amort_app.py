#import Libraries
import pandas as pd
import datetime as dt
from datetime import date, timedelta,datetime
from pandas.tseries.offsets import MonthEnd
from dateutil.relativedelta import relativedelta
import streamlit as st
import numpy as np
from amort_func import *



st.set_page_config(page_title="Amort_App",layout="wide")
st.markdown(
"""
<style>
[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
width: 600px;
}
[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
width: 500px;
margin-left: -600px;
}
</style>
""",
unsafe_allow_html=True
)


# "st.session_state object:",st.session_state

if 'master_df' not in st.session_state:
    st.session_state['master_df']=pd.DataFrame(columns=['schedule_month','sales_month','source','material#','sales_amt','amrt_start_month','amrt_period','amrt_factor','beg_bal','remainder','end_bal','monthly_amort'])

if 'amort_rollforward' not in st.session_state:
    st.session_state['amort_rollforward']=pd.DataFrame(columns=['schedule_month','sales_month','source','material#','sales_amt','amrt_start_month','amrt_period','amrt_factor','beg_bal','remainder','end_bal','monthly_amort'])

if 'summary' not in st.session_state:
    st.session_state['summary']=pd.DataFrame(columns=['schedule_month','material#','monthly_amort'])


st.title('Amortization Schedule Application')

st.subheader('1. Upload sales file')

#EH:  upload sales file
uploaded_file = st.file_uploader("Select sales file")

#EH: check the file is not none
if uploaded_file is not None:
     # import sales file into df and find the max amortization date
     import_df,max_date=import_data(uploaded_file)

     #EH: display sales file as df
     st.write(import_df)

    #EH: specify the last month of amortization per schedule month
     st.write(f'max_amort_date is {max_date} for this schedule')




#EH:  calculate amortization rollforward of sales per schedule month
st.subheader('2. calculate amortization rollfoward')


if st.button('calculate rollforward'):
    #EH: calculate amort
    st.session_state.amort_rollforward=rollforward_df(import_df,max_date)
    #EH: display amortization schedule
    st.write(st.session_state.amort_rollforward)

#EH:  compile amortization rollforward to master amortization schedul
st.subheader('3. add rollfoward to master schedule')
if st.button('compile master schedule'):
    #EH: create master df
    st.session_state.master_df=master_schedule(st.session_state['master_df'],st.session_state.amort_rollforward)
    #EH: display master amortization schedule
    st.write(st.session_state.master_df)

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(st.session_state.master_df)

#EH: download amortization master schedult o csv
st.download_button(
     label="Download master schedule as CSV",
     data=csv,
     file_name='master_schedule.csv',
     mime='text/csv',
 )

#EH:  summarize amortization by schedule month and material number
st.subheader('4. Amortization Summary')


if st.button('Generate Summary'):
    st.session_state.summary=st.session_state.master_df.groupby(by=['schedule_month','material#']).sum()
    st.session_state.summary=st.session_state.summary.iloc[:,[-1]]
    st.session_state.summary=st.session_state.summary.reset_index()

    st.write(st.session_state.summary)


csv2 = convert_df(st.session_state.summary)

#EH: download amortization summary o csv
st.download_button(
     label="Download amort summary schedule as CSV",
     data=csv2,
     file_name='amort_summary.csv',
     mime='text/csv',
 )

#EH: pivot the master schedule to column rollforward
st.subheader('5. Pivot schedule')

if st.button('Generate schedule pivot'):


    pivot_df=st.session_state.master_df.copy()
    pivot_df=pd.pivot_table(pivot_df,columns=['schedule_month'],values=['beg_bal','remainder','end_bal','monthly_amort'],index=['sales_month','source','material#','sales_amt','amrt_start_month','amrt_period','amrt_factor'],fill_value=0).swaplevel(0,1, axis=1).sort_index(axis=1)
    pivot_df=pivot_df.reset_index()

    st.write(pivot_df)




