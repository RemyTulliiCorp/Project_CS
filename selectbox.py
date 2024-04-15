import streamlit as st
import pandas as pd
cuisine_type = st.selectbox('Choose a cuisine type', ('', 'American', 'Asian', 'British', 'Caribbean', 'Central Europe', 'Chinese', 'Eastern Europe', 'French', 'Indian', 'Italian', 'Japanese', 'Kosher', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic', 'South American', 'South East Asian'), index=0, key='type')
max_time = st.selectbox('Maximum total time in minutes', ('', '15', '30', '45'), index=0, key='time')
