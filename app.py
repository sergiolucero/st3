import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

df = pd.read_csv('dopa1.csv')

AgGrid(df)
