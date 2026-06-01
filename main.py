import streamlit as st
import numpy as np
import math
from streamlit_vertical_slider import vertical_slider

# Scenario 1

st.set_page_config(layout="wide")

TOTAL_WASTE = 12000


st.subheader("Waste management before intervention")
st.write("\n\nTotal Waste: 12000 (g)")

bottom_cols = st.columns([1,1,1,4,4], gap = "small", width = 1200)
with bottom_cols[0]:
    n_black_op_before = vertical_slider(
        label="Black-OP",
        height=150,
        key="S1_0",
        default_value=5000,
        step=1,
        min_value=0,
        max_value=8000,
        value_always_visible=True,
        slider_color = "black",
    )

with bottom_cols[1]:
    n_yellow_before = vertical_slider(
        label="Yellow bags",
        height=150,
        key="S1_1",
        default_value=1000,
        step=1,
        min_value=0,
        max_value=3000,
        value_always_visible=True,
        slider_color = "yellow",
    )
default_3 = TOTAL_WASTE - (n_black_op_before+n_yellow_before)
with bottom_cols[2]:
    n_black_before = vertical_slider(
        label="Black bags",
        height=150,
        key=f"S1_2_{n_black_op_before}_{n_yellow_before}",
        default_value=default_3,
        step=1,
        min_value=0,
        max_value=TOTAL_WASTE,
        value_always_visible=True,
        slider_color = "grey"
    )

def cost(n_black_op, n_yellow, n_black):
    cost_per_black_op_bag = 2
    cost_per_yellow_bag = 0.5
    cost_per_black_bag = 0.8
    return n_black_op*cost_per_black_op_bag + n_yellow*cost_per_yellow_bag + n_black*cost_per_black_bag

cost_before = int(cost(n_black_op_before, n_yellow_before, n_black_before))

with bottom_cols[3]:
    st.write("Total cost for one operation = ", f"{cost_before:,.2f}", " Euros")

with bottom_cols[4]:
    n_per_year = st.number_input("Total number of operations per year", placeholder = "Type a number...", min_value = 50, step = 1)
    st.write("Total cost per year = ", f"{int(n_per_year*cost_before):,.2f}", " Euros")


st.subheader("Waste management after intervention (training and proper labeling)")
st.write("\n\nTotal Waste: 12000 (g)")

bottom_cols_2 = st.columns([1,1,1,4,4], gap = "small", width = 1200)

with bottom_cols_2[0]:
    n_black_op_after = vertical_slider(
        label="Black-OP (Biohazard)",
        height=150,
        key="S2_0",
        default_value=3000,
        step=1,
        min_value=0,
        max_value=8000,
        value_always_visible=True,
        slider_color = "black",
    )

with bottom_cols_2[1]:
    n_yellow_after = vertical_slider(
        label="Yellow bags (Recyclable)",
        height=150,
        key="S2_1",
        default_value=2000,
        step=1,
        min_value=0,
        max_value=3000,
        value_always_visible=True,
        slider_color = "yellow",
    )


default_3_after = TOTAL_WASTE - (n_black_op_after+n_yellow_after)

with bottom_cols_2[2]:
    n_black_after = vertical_slider(
        label="Black bags",
        height=150,
        key=f"S2_2_{n_black_op_after}_{n_yellow_after}",
        default_value=default_3_after,
        step=1,
        min_value=0,
        max_value=TOTAL_WASTE,
        value_always_visible=True,
        slider_color = "grey"
    )


cost_after = int(cost(n_black_op_after, n_yellow_after, n_black_after))

with bottom_cols_2[3]:
    st.write("Total cost for one operation = ", f"{cost_after:,.2f}", " Euros")

with bottom_cols_2[4]:
    st.write("Total cost per year = ", f"{int(n_per_year*cost_after):,.2f}", " Euros")

    