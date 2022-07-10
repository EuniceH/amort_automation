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

     st.write(f'max_amort_date is {max_date} for this schedule')





st.subheader('2. calculate amortization rollfoward')
if st.button('calculate rollforward'):
    #EH: calculate amort
    st.session_state.amort_rollforward=rollforward_df(import_df,max_date)
    #EH: display amortization schedule
    st.write(st.session_state.amort_rollforward)


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

st.download_button(
     label="Download master schedule as CSV",
     data=csv,
     file_name='master_schedule.csv',
     mime='text/csv',
 )

st.subheader('4. Amortization Summary')


if st.button('Generate Summary'):
    summary=st.session_state.master_df.groupby(by=['schedule_month','material#']).sum()
    summary=summary.iloc[:,[-1]]
    summary=summary.reset_index()

    st.write(summary)


csv2 = convert_df(st.session_state.summary)

st.download_button(
     label="Download amort summary schedule as CSV",
     data=csv,
     file_name='amort_summary.csv',
     mime='text/csv',
 )
