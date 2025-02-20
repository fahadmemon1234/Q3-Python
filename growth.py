import pandas as pd
import streamlit as st
import os
from io import BytesIO

# Page configuration with growth mindset theme
st.set_page_config(
    page_title="Growth Mindset Data Sweeper",
    layout="wide",
    page_icon="🌱"  # Growth symbol
)

# Enhanced custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #1a1a1a, #2d2d2d);
        color: white;
    }
    .success-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #4CAF50;
        color: white;
    }
    .growth-tip {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #2196F3;
        color: white;
        margin: 1rem 0;
    }
    /* Button styling */
    .stButton button {
        color: #2d2d2d !important;
        font-weight: bold !important;
        background-color: #4CAF50 !important;
        transition: all 0.3s ease !important;
    }
    .stButton button:hover {
        background-color: #45a049 !important;
        transform: translateY(-2px) !important;
    }
    /* Download button specific styling */
    .stDownloadButton button {
        color: #2d2d2d !important;
        font-weight: bold !important;
        background-color: #2196F3 !important;
    }
    .stDownloadButton button:hover {
        background-color: #1976D2 !important;
        transform: translateY(-2px) !important;
    }
    /* Checkbox label color */
    .stCheckbox label {
        color: white !important;
    }
    .stCheckbox div[data-testid="stMarkdownContainer"] {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced title and description with growth mindset message
st.title("🌱 Growth Mindset Data Sweeper")
st.markdown("""
    <div style='background-color: #262730; padding: 20px; border-radius: 10px; margin-bottom: 20px'>
        <h4 style='color: #4CAF50'>👨‍💻 Created with a Growth Mindset Made by Fahad Memon</h4>
        <p>Embrace the journey of data transformation! Each dataset is an opportunity to learn and grow. 
        Remember: challenges in data cleaning are stepping stones to better insights! 🚀</p>
        <p style='color: #2196F3'><i>"Every data challenge is an opportunity to learn and improve." - Growth Mindset Data Science</i></p>
    </div>
""", unsafe_allow_html=True)

# File upload with growth mindset encouragement
st.markdown("### 📁 Start Your Data Journey")
st.markdown("""
    <div class='growth-tip'>
        💡 <b>Growth Tip:</b> Don't fear messy data - each cleanup task makes you stronger!
    </div>
""", unsafe_allow_html=True)

st.markdown(
    '<p style="color: white;">Upload your files (CSV or Excel) - Every file is a new learning opportunity!</p>', 
    unsafe_allow_html=True
)
uploaded_files = st.file_uploader(
    label="",
    type=["csv", "xls", "xlsx"], 
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext in [".xls", ".xlsx"]:
                df = pd.read_excel(file)
            
            # Custom CSS for white metrics and buttons
            st.markdown("""
                <style>
                    [data-testid="stMetricValue"] {
                        color: white !important;
                    }
                    [data-testid="stMetricLabel"] {
                        color: white !important;
                    }
                    .dataframe {
                        color: white !important;
                    }
                </style>
            """, unsafe_allow_html=True)
            
            # Data summary
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", len(df))
            with col2:
                st.metric("Total Columns", len(df.columns))
            with col3:
                st.metric("Missing Values", df.isna().sum().sum())

            # Display dataframe with white text
            st.dataframe(df.head(), use_container_width=True)
            
            # Enhanced Data Cleaning Options
            st.markdown("### 🧹 Data Enhancement Journey", unsafe_allow_html=True)
            st.markdown("""
                <style>
                    h3 {
                        color: white !important;
                    }
                </style>
            """, unsafe_allow_html=True)
            st.markdown("""
<style>
    /* Checkbox label color */
    .stCheckbox label {
        color: white !important;
    }
    .stCheckbox div[data-testid="stMarkdownContainer"] {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
            if st.checkbox(f"✨ Begin data transformation for {file.name}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("🔄 Remove Duplicates", key=f"dup_{file.name}"):
                        original_len = len(df)
                        df.drop_duplicates(inplace=True)
                        removed = original_len - len(df)
                        st.success(f"🌟 Growth Achievement: Removed {removed} duplicate rows!")

                with col2:
                    if st.button("📝 Fill Missing Values", key=f"fill_{file.name}"):
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.success("🌟 Growth Achievement: Successfully handled missing values!")

                # Enhanced Download Options
                if st.button("💾 Save Your Progress", key=f"download_{file.name}"):
                    output = BytesIO()
                    if file_ext == ".csv":
                        df.to_csv(output, index=False)
                        file_name = f"enhanced_{file.name}"
                    else:
                        df.to_excel(output, index=False)
                        file_name = f"enhanced_{os.path.splitext(file.name)[0]}.xlsx"
                    
                    st.download_button(
                        label="📥 Download Your Enhanced Data",
                        data=output.getvalue(),
                        file_name=file_name,
                        mime="application/octet-stream"
                    )
                    
        except Exception as e:
            st.error(f"Learning Opportunity: Error in {file.name}: {str(e)}")
            st.markdown("""
                <div class='growth-tip'>
                    💪 Remember: Errors are stepping stones to success. Let's learn from this and try again!
                </div>
            """, unsafe_allow_html=True)