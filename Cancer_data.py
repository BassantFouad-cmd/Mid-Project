import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    layout='wide',
    page_title="Global Cancer Patients 2015–2024",
    page_icon=":cancer:"
)


st.markdown(
    """<h1 style='color: white; text-align: center;'> Global Cancer Patients 2015–2024 Analysis </h1>""",
    unsafe_allow_html=True
)

tab_1 , tab_2 , tab_3 , tab_4 , tab_5 = st.tabs(["Purpose and Introduction","Used Data Frame",
        "Univariate Analysis",
        "Bivariate analysis",
        "Multivariate Analysis"])

with tab_1 : 
    col1, col2 = st.columns([1, 2]) 
    with col2:
        st.image("images.jpeg", width=550)
        
  

    st.markdown("""<h1 style='color: white; text-align: center;'> Purpose </h1>""",unsafe_allow_html=True)
    st.markdown("""
<div style='text-align: center'>
    <p style="font-size:18px;">
    The central purpose of analyzing the Global Cancer Patient Dataset is to extract meaningful insights about the patterns and determinants of cancer over a ten-year period (2015–2024). By simulating global cancer-related data, this analysis empowers a wide range of stakeholders—including medical researchers, clinicians, policymakers, and AI developers—to understand how various factors interact in the onset, treatment, and survival outcomes of cancer.
    </p>
    <p style="font-size:18px;">
    Through this simulated dataset, the project aims to:
    <ul style="text-align: left; display: inline-block;">
        <li>Identify trends in cancer incidence and mortality across different regions.</li>
        <li>Evaluate the effectiveness and reach of various treatment protocols.</li>
        <li>Investigate the impact of socio-demographic, genetic, and environmental variables on patient outcomes.</li>
        <li>Provide a foundation for predictive modeling and decision support tools powered by AI.</li>
    </ul>
    </p>
    <p style="font-size:18px;">
    Ultimately, the insights derived from this analysis can help inform global health strategies, improve clinical practices, and guide future research in oncology.
    </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""<h1 style='color: white; text-align: center;'> Introduction </h1>""",unsafe_allow_html=True)
    st.markdown("""
<div style='text-align: center'>
    <p style="font-size:18px;">
    Welcome to this analytical overview of cancer—a disease that continues to challenge healthcare systems, researchers, and policymakers worldwide.
    </p>
    <p style="font-size:18px;">
    In this report, we begin with a foundational understanding of what cancer is at a biological level—how abnormal cell growth disrupts normal body functions and leads to life-threatening conditions if not detected and managed in time.
    </p>
    <p style="font-size:18px;">
    We then categorize cancer into its major types—including carcinomas, sarcomas, leukemias, lymphomas, and more—highlighting how each originates in different tissues and organs, with unique clinical and epidemiological profiles.
    </p>
    <p style="font-size:18px;">
    This analysis also covers the staging system, a critical framework used globally to classify cancer progression from Stage 0 to Stage IV. We’ll discuss how staging impacts prognosis, treatment planning, and survival outcomes.
    </p>
    <p style="font-size:18px;">
    Drawing on global datasets and simulated trends from 2015 to 2024, this video will help you contextualize how cancer types and stages have evolved across populations, and what patterns are emerging that could inform future medical research, resource allocation, and AI-driven prediction models.
    </p>
    <p style="font-size:18px;">
    Let’s dive into the data and insights shaping our understanding of cancer today.
    </p>
</div>
""", unsafe_allow_html=True)


    st.markdown("""<h3 style='color: white; text-align: center;'> What is Cancer? </h3>""",unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=LEpTTolebqo")

    st.markdown("""<h3 style='color: white; text-align: center;'> Explainer Video on Cancer Staging </h3>""",unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=yvHe3AiY3jg")
    st.markdown("""<h3 style='color: white; text-align: center;'> Explainer Video on Cancer Types </h3>""",unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dEBi-yvSWmQ")


with tab_2:
    df = pd.read_csv("global_cancer_patients_2015_2024.csv")
    st.dataframe(df, height=800, width=1200)


with tab_3:
    st.markdown(
        """<h2 style='color: white; text-align: center;'> Univariate Analaysis </h2>""",
        unsafe_allow_html=True
    )

    df = pd.read_csv("global_cancer_patients_2015_2024.csv")
    df = df.drop("Patient_ID", axis=1)

    df["Year"] = pd.to_datetime(df["Year"], format='%Y')

    Start_Date = st.sidebar.date_input(
        "Start Date", value=df.Year.min(), min_value=df.Year.min(), max_value=df.Year.max()
    )
    End_Date = st.sidebar.date_input(
        "End Date", value=df.Year.min(), min_value=df.Year.min(), max_value=df.Year.max()
    )

    Aspect_Percentage = st.sidebar.radio(
        "Select the Aspect for getting the percentage of each Category",
        ['Gender', 'Country_Region', 'Year', 'Cancer_Type', 'Cancer_Stage'])
    st.markdown(
        """<h3 style='color: white; text-align: center;'> Selected Aspect Percentage from the Entire Database </h3>""",
        unsafe_allow_html=True)
    st.plotly_chart(px.pie(data_frame=df, names=Aspect_Percentage))
    st.markdown(
        """<h3 style='color: white; text-align: center;'> Which countries or regions have the highest number of reported cancer cases?</h3>""",
        unsafe_allow_html=True)
    st.plotly_chart(px.box(data_frame= df , x="Country_Region"))
    bins = [0, 30, 50, 70, float('inf')]
    labels = ['<30', '30-50', '50-70', '70+']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    st.markdown("""<h3 style='color: white; text-align: center;'>What is the least repeated Age group from 2015 to 2024?</h3>""",unsafe_allow_html=True)
    st.plotly_chart(px.bar(data_frame= df , x="Age_Group"))



with tab_4:
    st.markdown(
        """<h2 style='color: white; text-align: center;'> Bivariate Analysis </h2>""",
        unsafe_allow_html=True
    )

    df_filtered = df[
        (df["Year"] >= pd.to_datetime(Start_Date)) &
        (df["Year"] <= pd.to_datetime(End_Date))
    ]

    st.markdown(
        """<h3 style='color: white; text-align: center;'> What is the distribution of Air pullation between the chosen Date Range </h3>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<h6 style='color: white; text-align: center;'> Make sure to Choose start and End Date to Analyze Air Pollution Through the Years </h6>""",
        unsafe_allow_html=True
    )

    st.plotly_chart(px.histogram(data_frame=df_filtered,x="Air_Pollution",labels={"Air_Pollution": "Air Pollution Distribution"}))

    st.markdown(
        """<h3 style='color: white; text-align: center;'> Is there a correlation between the all aspects? </h3>""",
        unsafe_allow_html=True
    )

    correlation = df.select_dtypes(include='number').corr()

    st.plotly_chart(px.imshow(correlation,height=800,width=1200,text_auto=True))


    st.markdown(
        """<h3 style='color: white; text-align: center;'> Among patients of the selected age, how does the average treatment cost vary across different cancer types? </h3>""",
        unsafe_allow_html=True
    )
    st.markdown(
        """<h5 style='color: white; text-align: center;'> Select an Age from the Age Slider </h5>""",
        unsafe_allow_html=True
    )
    Age_Value = st.sidebar.slider("Age Slider", min_value=int(df["Age"].min()), max_value=int(df["Age"].max()))

    filtered_df = df[df["Age"] == Age_Value]
    avg_cost_by_cancer_type = filtered_df.groupby("Cancer_Type")["Treatment_Cost_USD"].mean().reset_index()
    st.plotly_chart(px.bar(data_frame=avg_cost_by_cancer_type,x="Cancer_Type",y="Treatment_Cost_USD"))







with tab_5:
    st.markdown(
        """<h2 style='color: white; text-align: center;'> Multi Analysis </h2>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<h3 style='color: white; text-align: center;'> How does cancer severity vary with smoking and genetic risk? </h3>""",
        unsafe_allow_html=True
    )

    df['Genetic_Risk_Bin'] = pd.cut(
        df['Genetic_Risk'],
        bins=[0, 0.3, 0.7, 1.0],
        labels=['Low', 'Medium', 'High']
    )
    df = df.dropna(subset=['Genetic_Risk_Bin'])

    grouped = df.groupby(["Smoking", "Genetic_Risk_Bin"]).agg(
        Avg_Severity=("Target_Severity_Score", "mean"),
        Count=("Target_Severity_Score", "count")
    ).reset_index()

    fig = px.scatter(
        grouped,
        x="Smoking",
        y="Avg_Severity",
        color="Genetic_Risk_Bin",
        labels={"Avg_Severity": "Avg. Cancer Severity Score"},
    )

    st.plotly_chart(fig)

    st.markdown(
        """<h3 style='color: white; text-align: center;'> How does the treatment cost vary across different cancer types and stages? </h3>""",
        unsafe_allow_html=True
    )

    df_cost = df.groupby(['Cancer_Type', 'Cancer_Stage'])['Treatment_Cost_USD'].sum().reset_index()

    fig= px.bar(
        df_cost,
        x="Cancer_Type",
        y="Treatment_Cost_USD",
        color="Cancer_Stage",
        barmode="group",
        labels={"Cancer_Type": "Cancer Type"}
    )

    st.plotly_chart(fig)

    st.markdown(
        """<h3 style='color: white; text-align: center;'> How Cancer Stage, Cost, and Region Relate to Survival Years</h3>""",
        unsafe_allow_html=True
    )
    fig2 = px.histogram(df,x="Cancer_Stage",y="Survival_Years",color="Country_Region",barmode="group",title="Survival Years vs Treatment Cost (Colored by Cancer Stage)")
    st.plotly_chart(fig2)
