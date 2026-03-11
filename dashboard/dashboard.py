import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Employee Analytics Dashboard", layout="wide")

st.title("Employee Workload Analytics & Productivity Dashboard")

# -------- File Upload --------
uploaded_file = st.file_uploader("Upload Employee Dataset", type=["csv","xlsx","json"])

if uploaded_file:

    # -------- Read File --------
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    elif uploaded_file.name.endswith(".json"):
        df = pd.read_json(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # -------- Detect Columns --------
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # -------- Sidebar Filters --------
    st.sidebar.header("Filter Data")

    if "department" in df.columns:
        dept_filter = st.sidebar.multiselect(
            "Select Department",
            options=df["department"].unique(),
            default=df["department"].unique()
        )

        df = df[df["department"].isin(dept_filter)]

    # -------- KPI Metrics --------
    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Employees", len(df))

    if "performance_score" in df.columns:
        col2.metric("Average Performance", round(df["performance_score"].mean(),2))

    if "department" in df.columns:
        col3.metric("Departments", df["department"].nunique())

    # -------- Statistics --------
    st.subheader("Statistical Summary")
    st.write(df.describe())

    # -------- Numeric Distribution --------
    st.subheader("Numeric Data Distribution")

    selected_num = st.selectbox("Select Numeric Column", numeric_cols)

    fig, ax = plt.subplots()

    df[selected_num].hist(bins=20, ax=ax)

    ax.set_title(f"{selected_num} Distribution")

    st.pyplot(fig)

    # -------- Categorical Distribution --------
    st.subheader("Categorical Distribution")

    selected_cat = st.selectbox("Select Category Column", categorical_cols)

    fig, ax = plt.subplots()

    df[selected_cat].value_counts().plot(kind="bar", ax=ax)

    st.pyplot(fig)

    # -------- Experience vs Performance --------
    if "years_experience" in df.columns and "performance_score" in df.columns:

        st.subheader("Experience vs Performance")

        fig, ax = plt.subplots()

        sns.scatterplot(
            x=df["years_experience"],
            y=df["performance_score"],
            ax=ax
        )

        st.pyplot(fig)

    # -------- Department Performance --------
    if "department" in df.columns and "performance_score" in df.columns:

        st.subheader("Department Average Performance")

        dept_perf = df.groupby("department")["performance_score"].mean()

        fig, ax = plt.subplots()

        dept_perf.plot(kind="bar", ax=ax)

        st.pyplot(fig)

    # -------- Correlation Heatmap --------
    if len(numeric_cols) > 1:

        st.subheader("Correlation Heatmap")

        fig, ax = plt.subplots()

        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)

        st.pyplot(fig)