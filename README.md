# Financial Department Tax Compliance Report

## Overview

This project is a **Streamlit-based web application** developed to analyze the relationship between **Income** and **Tax Filing Status** in a census dataset. The system shows individuals who are eligible to pay taxes but are not filing tax returns and generates a financial report that can assist government departments in improving tax compliance.

---

## Objectives

The main objectives of this project are:

* Analyze income and tax filing behavior
* Identify high-income individuals who are not filing taxes
* Estimate potential tax revenue loss
* Generate a simple policy report
* Present the results using an interactive web interface

---

## Dataset Description

The dataset contains information about individuals and their tax filing status.

### Columns Used

* **Income** – Annual income of individuals
* **Tax_Filing_Status** – Tax filing category

### Total Records

* **2000 Individuals**

---

## Data Cleaning and Preprocessing

Before analysis, the dataset was cleaned and prepared.

### Data Cleaning Steps

1. **Column Selection**

   * Only relevant columns were used:

     * Income
     * Tax_Filing_Status

2. **Handling Missing Values**

   * Rows with missing Income or Tax_Filing_Status values were removed.

3. **Data Type Conversion**

   * Income values were converted into numeric format.

4. **Text Cleaning**

   * Extra spaces were removed using:

   ```
   str.strip()
   ```

5. **Standardization**

   * Tax filing status values were standardized using:

   ```
   str.lower()
   ```

   This ensured values like:

   * "Nonfiler"
   * " nonfiler "
   * "NONFILER"

   were treated as the same category.

---

## Data Analysis

### 1. High Income Nonfilers

Individuals earning above the taxable threshold and not filing taxes were identified.

### Taxable Threshold

Income greater than:

```
1312.50 per month
```

Selection formula:

```
Income > 1312.50 AND Tax_Filing_Status = Nonfiler
```

These individuals represent potential tax non-compliance cases.

---

### 2. Tax Compliance Report

The application calculates:

* Total Records
* Total Filers
* Total Nonfilers

Filers are calculated as:

```
Filers = Total Records − Nonfilers
```

Where:

```
Nonfilers = Tax_Filing_Status = Nonfiler
```

---

### 3. Category-wise Distribution

The system displays the count of individuals in each tax filing category.

Example categories include:

* Nonfiler
* Single
* Jointbothunder65
* Headofhousehold
* Jointboth65+
* Jointoneunder65&one65+

This helps understand the distribution of taxpayers.

---

### 4. Lost Revenue Estimation

Potential lost tax revenue is estimated from individuals who:

* Earn above the taxable threshold
* Are Nonfilers

#### Step 1 – Lost Income

```
Lost Income = Sum of income of High Income Nonfilers
```

#### Step 2 – Lost Tax

```
Lost Tax = Lost Income × 10%
```

A flat tax rate of **10%** is assumed for estimation.

This represents the **estimated tax revenue the government could collect if all eligible taxpayers filed taxes.**

---

## Web Application (Streamlit)

The system provides an interactive dashboard using Streamlit.

### Features

* Dataset viewer with dropdown menu
* High Income Nonfiler table
* Category-wise count display
* Tax compliance statistics
* Lost revenue estimation
* Policy recommendation report
* Styled background interface

### UI Improvements

The interface includes:

* Gradient background
* Expandable tables
* Metric cards
* Organized sections

---

## Database Implementation

### Local Version

The local version of the project uses **MySQL Database**.

#### Table Structure

```
census
```

Columns:

* Income
* Tax_Filing_Status

The dataset was inserted into MySQL using Python.

---

### Deployed Version

The deployed version uses an **Excel dataset** instead of MySQL.

This change was required because:

```
Streamlit Cloud cannot connect to local databases.
```

The dataset is loaded using:

```
pd.read_excel("census.csv.xlsx")
```

---

## Technologies Used

* Python
* Streamlit
* Pandas
* MySQL
* Excel
* GitHub
* Streamlit Community Cloud

---

## How to Run Locally

Install dependencies:

```
pip install streamlit pandas openpyxl mysql-connector-python
```

Run the application:

```
streamlit run app.py
```

---

## Deployment

The project is deployed using **Streamlit Community Cloud**.

The deployed version reads data from an Excel file.

---

## Policy Recommendations

Based on the analysis, the government can take the following actions:

### 1. Targeted Tax Notices

High-income Nonfilers can be identified and sent tax notices to improve compliance.

### 2. Tax Awareness Programs

Educational campaigns can be organized to improve tax filing awareness.

### 3. Monitoring High Income Nonfilers

Authorities can monitor individuals with high income but no tax filings.

### 4. Policy Evaluation

The taxable income threshold can be evaluated and adjusted if required.

---

## Conclusion

This project demonstrates how data analysis can be used to identify tax compliance issues and estimate potential tax revenue loss.

The system provides a simple and effective tool that can help financial departments improve tax collection and policy planning.

---

## ->

Tax Compliance Analysis using Pandas and Streamlit
