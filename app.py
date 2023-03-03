import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
'''
# Get yout taxi fare done!
'''

date = st.date_input(
    "Choose a Date",
    datetime.datetime(year=2023,month= 3,day= 3))
time = st.time_input('Choose a time', datetime.time(8, 45,2))
n_pass = st.text_input('Number of passengers', '1')
pickup__longitude= (st.text_input('Pickup  longitude','-73.9798156'))
pickup__latitude= (st.text_input('Pickup latitude','40.7614327'))
dropoff__longitude=(st.text_input('Dropoff longitude','-73.8803331'))
dropoff__latitude=(st.text_input('Dropoff latitude','40.6513111'))
# date_time=datetime.time(f"{date} {time}")
pickup_time= str(datetime.datetime.combine(date, time))
map_data=pd.DataFrame(np.array([[float(pickup__latitude),float(pickup__longitude)],
        [float(dropoff__latitude),float(dropoff__longitude)]]), columns=['lat', 'lon'])
st.map(data=map_data, zoom=2, use_container_width=True)

'''

'''

url = 'https://taxifare.lewagon.ai/predict'




# pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
# 2. Lets build a dictionary containing the parameters for our API...


params={'pickup_datetime':pickup_time,'pickup_longitude':pickup__longitude,
        'pickup_latitude': pickup__latitude,'dropoff_longitude':dropoff__longitude,
        "dropoff_latitude":dropoff__latitude, 'passenger_count':n_pass}

# 3. Let's call our API using the `requests` package...

r = requests.get(url, params=params).json()
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
# st.write(r.status_code)
a=round(r['fare'],2)
st.write(f'Your taxi fare is {a}$')
## Finally, we can display the prediction to the user

# d=st.date_input("label", value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# date = st.date_input(
#     "Choose a Date",
#     datetime.date(2023, 3, 3))
# t = st.time_input('Choose a time', datetime.time(8, 45))
# n_pass = st.text_input('Number of passengers', '')
# pickup_longitude= st.number_input('pickup longitude')
# pickup_latitude= st.number_input('pickup_latitude')
# dropoff_longitude=st.number_input('dropoff_longitude')
# dropoff_latitude=st.number_input('dropoff_latitude')

# st.write('Your birthday is:', d)
