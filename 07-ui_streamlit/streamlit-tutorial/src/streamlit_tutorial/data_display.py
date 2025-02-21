import streamlit as st
import numpy as np
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "Berlin"]
}


st.table(data)

st.dataframe(data)



st.write("---")


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Line 1', 'Line 2', 'Line 3']
)

st.line_chart(chart_data)


st.dataframe(chart_data)
