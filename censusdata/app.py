import streamlit as st
import pandas as pd

# ---------- Background Styling ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

h1 {
    color: #ffffff;
    text-align: center;
}

h2, h3 {
    color: #e6f2ff;
}

[data-testid="stMetricValue"] {
    color: #00ffcc;
    font-size: 28px;
}

[data-testid="stMetricLabel"] {
    font-size: 18px;
}

div[data-testid="stExpander"] {
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 5px;
}

</style>
""", unsafe_allow_html=True)


# ---------- Title ----------
st.title("Financial Department Tax Report")


# ---------- Load Dataset (Cloud Version) ----------
df = pd.read_excel("censusdata/census.csv.xlsx")


# ---------- Section 1 ----------
st.subheader("Income and Tax Filing Data")

with st.expander("Click to View Full Dataset"):
    st.dataframe(df)


# ---------- Section 2 ----------
st.subheader("High Income Nonfilers")

result = df[
    (df['Income'] > 1312.50) &
    (df['Tax_Filing_Status'].str.strip().str.lower() == "nonfiler")
]

result2 = df[
    (df['Income'] < 1312.50) &
    (df['Tax_Filing_Status'].str.strip().str.lower() == "nonfiler")
]

with st.expander("Click to View High Income Nonfilers Table"):
    st.dataframe(result)


st.subheader("Category-wise count")
st.write(df['Tax_Filing_Status'].value_counts())


st.write("Number of High Income Nonfilers:")
st.success(result.shape[0])


# ---------- Section 3 ----------
st.subheader("Tax Compliance Report")

filers = df[
    df['Tax_Filing_Status'].str.strip().str.lower() != "nonfiler"
].shape[0]

st.metric("Total Filers", filers)
st.metric("Total Records", len(df))


# ---------- Section 4 ----------
st.subheader("Lost Revenue Estimate")

lost_income = result['Income'].sum()
lost_tax = lost_income * 0.10

st.metric("Potential Lost Tax", round(lost_tax, 2))


# ---------- Policy Report ----------
st.subheader("Policy Report: Tax Compliance Analysis")

st.markdown("""
### Overview

This report analyzes the relationship between **annual income** and **tax filing status** to identify potential gaps in tax compliance. The objective is to help the financial department identify individuals who are eligible to pay taxes but are not filing tax returns.

### Key Findings

- A total of **2000 individuals** were analyzed.
- **705 individuals** were identified as Nonfilers.
- **1295 individuals** were identified as Filers.
- Several individuals with income above the taxable threshold were found to be Nonfilers.

### Recommended Government Actions

**1. Targeted Tax Notices**

Individuals earning above the taxable income threshold but classified as Nonfilers can be identified and sent official tax notices encouraging compliance.

**2. Awareness Programs**

The government can organize tax awareness campaigns to educate citizens about tax filing requirements and benefits.

**3. Improved Monitoring**

Financial departments can monitor high-income Nonfilers more closely to detect possible tax evasion.

**4. Policy Planning**

The data can help policymakers evaluate whether the current taxable income threshold is appropriate and make adjustments if necessary.

### Conclusion

This analysis helps identify gaps in tax compliance and provides useful insights that can assist the government in improving tax collection and strengthening financial planning.
""")

