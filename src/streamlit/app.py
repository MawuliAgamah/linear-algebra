import streamlit as st
import numpy as np
import pandas as pd


# Create input fields for matrix dimensions
rows = st.number_input("Number of rows", min_value=1, max_value=10, value=3)
cols = st.number_input("Number of columns", min_value=1, max_value=10, value=3)


# _Create input fields for matrix elements
matrix = []
for i in range(int(rows)):
    col_values = []
    cols_input = st.columns(int(cols))
    for j in range(int(cols)):
        with cols_input[j]:
            value = st.number_input(f"[{i},{j}]", value=0.0, format="%.2f")
            col_values.append(value)
    matrix.append(col_values)


def draw_grid():


    # Display the matrix
if matrix:
    st.write("Current Matrix:")
    df = pd.DataFrame(matrix)
    st.dataframe(df)
