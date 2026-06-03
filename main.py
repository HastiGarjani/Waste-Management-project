import streamlit as st
import numpy as np
import pandas as pd
import math
from streamlit_vertical_slider import vertical_slider

waste = pd.read_csv("data/waste.csv")
# Scenario 1

st.set_page_config(layout="wide")

TOTAL_WASTE_no_Int = int(waste['mean_biohazard_waste_no_intervention'][0]
+ waste['mean_yellow_waste_no_intervention'][0]
+ waste['mean_annesthesia_waste_no_intervention'][0])

TOTAL_WASTE_with_Int = int(waste['mean_biohazard_waste_with_intervention'][0]
+ waste['mean_yellow_waste_with_intervention'][0]
+ waste['mean_annesthesia_waste_with_intervention'][0])
def cost(n_black_op, n_yellow, n_black):
        cost_per_black_op_bag = 1.9
        cost_per_yellow_bag = 0.1
        cost_per_black_bag = 0.3
        return n_black_op*cost_per_black_op_bag + n_yellow*cost_per_yellow_bag + n_black*cost_per_black_bag

def Scenario(Total_waste, key, defaults):

    st.write("\n\nTotal Waste:" + str(Total_waste) + "(g)")

    bottom_cols = st.columns([1,1,1,4,4], gap = "small", width = 1200)
    with bottom_cols[0]:
        n_black_op_before = vertical_slider(
            label="Black-OP",
            height=150,
            key=key[0],
            default_value=defaults[0],
            step=1,
            min_value=0,
            max_value=8500,
            value_always_visible=True,
            slider_color = "black",
        )

    with bottom_cols[1]:
        n_yellow_before = vertical_slider(
            label="Yellow bags",
            height=150,
            key=key[1],
            default_value=defaults[1],
            step=1,
            min_value=0,
            max_value=3000,
            value_always_visible=True,
            slider_color = "yellow",
        )
    default_3 = Total_waste - (n_black_op_before+n_yellow_before)
    with bottom_cols[2]:
        n_black_before = vertical_slider(
            label="Black bags",
            height=150,
            key=f"{key[2]}_{n_black_op_before}_{n_yellow_before}",
            default_value=default_3,
            step=1,
            min_value=0,
            max_value=Total_waste,
            value_always_visible=True,
            slider_color = "grey"
        )

   
    cost_before = int(cost(n_black_op_before, n_yellow_before, n_black_before))

    with bottom_cols[3]:
        st.write("Total cost for one operation = ", f"{cost_before:,.2f}", " Euros")

    with bottom_cols[4]:
        n_per_year = st.number_input("Total number of operations per year", placeholder = "Type a number...", min_value = 50, step = 1, key=key[3])
        st.write("Total cost per year = ", f"{int(n_per_year*cost_before):,.2f}", " Euros")

    return n_black_op_before, n_yellow_before, n_black_before, Total_waste,cost_before, n_per_year
st.subheader("Waste management before intervention")
Scenario(TOTAL_WASTE_no_Int, ["S1_0", "S1_1", "S1_2", "S1_3"],
         [int(waste['mean_biohazard_waste_no_intervention'][0]), int(waste['mean_yellow_waste_no_intervention'][0]), int(waste['mean_annesthesia_waste_no_intervention'][0])])

st.subheader("Waste management after intervention (training and proper labeling)")
Scenario(TOTAL_WASTE_with_Int, ["S2_0", "S2_1", "S2_2", "S2_3"],
         [int(waste['mean_biohazard_waste_with_intervention'][0]), int(waste['mean_yellow_waste_with_intervention'][0]), int(waste['mean_annesthesia_waste_with_intervention'][0])])
st.subheader("Produced waste at a random inspection")
eval = Scenario(TOTAL_WASTE_with_Int, ["S3_0", "S3_1", "S3_2", "S3_3"],
         [int(waste['mean_biohazard_waste_with_intervention'][0])+500, int(waste['mean_yellow_waste_with_intervention'][0]), int(waste['mean_annesthesia_waste_with_intervention'][0])])
if (eval[0]/eval[3]) > 0.05+int(waste['mean_biohazard_waste_with_intervention'][0])/TOTAL_WASTE_with_Int:
    
    st.markdown("<span style='color:#b30000;font-weight:500'>The hospital is not compliant with the regulations.</span>", unsafe_allow_html=True)
    st.warning("Deviation from standards", icon="⚠️")

