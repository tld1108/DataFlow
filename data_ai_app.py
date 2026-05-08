import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Insight Dashboard",
    layout="wide"
)

#CSS

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Montserrat', sans-serif;
    background-color: #F5F5FA;
}

section[data-testid="stSidebar"] {
    background-color: white !important;
    border-right: 1px solid #ECECF3;
}

.sidebar-title {
    font-size: 26px;
    font-weight: 700;
    color: #6D4AFF;
    padding: 20px 0;
    text-align: center;
}

/* Styling Card Utama */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: white !important;
    border-radius: 22px !important;
    border: 1px solid #F1F1F5 !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
    padding: 25px !important;
}

.metric-box {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #F1F1F5;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}
.metric-box h2 { color: #6D4AFF; margin: 0; }
.metric-box p { color: #6B7280; margin: 0; font-size: 14px; }

</style>
""", unsafe_allow_html=True)

#sidebar 

with st.sidebar:
    st.markdown("<div class='sidebar-title'>DataFlow</div>", unsafe_allow_html=True)
    st.info(" Dashboard")

#main

st.title("Data Insight Dashboard")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file:
    df = pd.read_csv(file)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"<div class='metric-box'><h2>{df.shape[0]}</h2><p>Total Rows</p></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-box'><h2>{df.shape[1]}</h2><p>Total Columns</p></div>", unsafe_allow_html=True)
    with m3:
        missing = df.isnull().sum().sum()
        st.markdown(f"<div class='metric-box'><h2>{missing}</h2><p>Missing Values</p></div>", unsafe_allow_html=True)

    st.write("---")

    # data preview 
    with st.container(border=True):
        st.subheader("Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)

    # insight
    with st.container(border=True):
        st.subheader("Insights")
        num_cols = df.select_dtypes(include='number').columns
        for col in num_cols:
            mean_val = df[col].mean()
            st.write(f" Average value of **{col}** is **{mean_val:.2f}**")

    # visualization
    if len(num_cols) > 0:
        with st.container(border=True):
            st.subheader("Visualization")
            selected_col = st.selectbox("Choose Column", num_cols)
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.hist(df[selected_col].dropna(), bins=20, color='#7B61FF', edgecolor='white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            st.pyplot(fig)

else:
    st.info("Upload CSV untuk mulai mendaptkan insight dari data Anda!")