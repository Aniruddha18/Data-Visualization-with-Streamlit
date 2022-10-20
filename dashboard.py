import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

#Main Dataframe
dataframe = pd.read_csv('employee_data.csv')
if st.checkbox('Show Employee Dataframe'):
    st.subheader('Employee data')
    st.write(dataframe)

#Bar Chart Visualization
def dataVisualization():
    st.title("Bar Chart (Data Visualization)")
    emp_dis = px.histogram(dataframe,y='JobRole',orientation='h',histnorm='percent'  ,text_auto='.2f',title="% Distribution of employees across job Roles")
    emp_income_dist = px.histogram(dataframe,x='Department',y='MonthlyIncome',color='Attrition',barmode="group",text_auto=True,histfunc='avg',title="Avg Income by Dept and Attrition")

    st.plotly_chart(emp_dis, use_column_width=True)
    st.plotly_chart(emp_income_dist, use_column_width=True)


#Search Form
def searchForm():
    with st.form(key='searchform'):
        col1,col2 = st.columns(2)
        col3,col4 = st.columns(2)
        col5,col6 = st.columns(2)
        with col1:
            department_selection = dataframe['Department'].unique().tolist()
            department = st.selectbox("Select Department",department_selection)
        with col2:
            attrition_selection = dataframe['Attrition'].unique().tolist()
            attrition = st.radio("Select Attrition",attrition_selection)
        with col3:
            gender_selection = dataframe['Gender'].unique().tolist()
            gender = st.radio("Select Gender",gender_selection)
        with col4:
            years_selection = dataframe['YearsAtCompany'].unique().tolist()
            year_at_company = st.slider("Select Years at Company",min_value= min(years_selection),
                        max_value= max(years_selection),
                        value=(min(years_selection),max(years_selection)))
        with col5:
            on_submit = st.form_submit_button()
    if on_submit:
            result_df = dataframe[ (dataframe['Department'] == department) & (dataframe['Attrition'] == attrition) & (dataframe['Gender'] == gender) & ( min(year_at_company) <= dataframe['YearsAtCompany']) &  ( max(year_at_company) >= dataframe['YearsAtCompany'])].head()
            result_df = result_df.sort_values(by=['MonthlyIncome'],ascending=False)
            st.write(result_df)


if st.checkbox('Show Employee Search Form'):
    st.subheader('Select employee details to filter dataframe')
    searchForm()
dataVisualization()



