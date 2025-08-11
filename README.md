# 🧾 Vendor Performance Analysis – Retail Inventory & Sales

Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using **SQL** and **Python**.

---

## 📌 Table of Contents
- [Overview](#overview)  
- [Business Problem](#business-problem)  
- [Dataset](#dataset)  
- [Tools & Technologies](#tools--technologies)  
- [Project Structure](#project-structure)  
- [Data Cleaning & Preparation](#data-cleaning--preparation)  
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
- [Research Questions & Key Findings](#research-questions--key-findings)  
- [How to Run This Project](#how-to-run-this-project)  
- [Final Recommendations](#final-recommendations)  
- [Author & Contact](#author--contact)  

---

## Overview
This project evaluates **vendor performance** and **retail inventory dynamics** to drive insights for purchasing, pricing, and inventory optimization.  
A complete analysis pipeline was built using:
- **SQL** for data extraction, cleaning, and transformation (ETL)  
- **Python** for exploratory data analysis, visualization, and statistical testing  

---

## Business Problem
Effective inventory and sales management are critical in retail.  
This analysis aims to:
- Identify underperforming brands needing pricing or promotional adjustments  
- Determine vendor contributions to sales and profits  
- Analyze cost-benefit of bulk purchasing  
- Investigate inventory turnover inefficiencies  
- Statistically validate differences in vendor profitability  

---

## Dataset
- Multiple CSV files located in `/data/` folder: **sales**, **vendors**, and **inventory** data  
- Summary tables generated during the cleaning & processing stage for analysis  

---

## Tools & Technologies
- **SQL** – CTEs, joins, aggregations, and filtering  
- **Python** – Pandas, Matplotlib, Seaborn, SciPy  
- **GitHub** – Version control and documentation  

---

## Project Structure
vendor-performance-analysis/
│
├── README.md
├── Vendor Analysis Project.pptx
├── exploratory_data_analysis.ipynb
├── vendor_performance_analysis.ipynb
├── ingestion_db.py
│   └── get_vendor_summary.py
├── sales.csv
├── vendors.csv
└── inventory.csv


---

## Data Cleaning & Preparation
- Removed transactions with:
  - Gross Profit ≤ 0  
  - Profit Margin ≤ 0  
  - Sales Quantity = 0  
- Created vendor-level summary metrics  
- Converted data types, handled outliers, merged lookup tables  

---

## Exploratory Data Analysis (EDA)
**Negative or Zero Values Detected:**
- Gross Profit: min `-52,002.78` (loss-making sales)  
- Profit Margin: min `-∞` (sales at/below cost)  
- Unsold inventory: slow-moving stock  

**Outliers Identified:**
- Freight costs up to `257K`  
- Large purchase/actual prices  

**Correlation Analysis:**
- Weak: Purchase Price ↔ Profit  
- Strong: Purchase Qty ↔ Sales Qty (`0.999`)  
- Negative: Profit Margin ↔ Sales Price (`-0.179`)  

---

## Research Questions & Key Findings
- **Brands for Promotions:** 198 brands with low sales but high profit margins  
- **Top Vendors:** Top 10 vendors = 65.69% of purchases → over-reliance risk  
- **Bulk Purchasing Impact:** 72% cost savings per unit in large orders  
- **Inventory Turnover:** $2.71M worth of unsold inventory  
- **Vendor Profitability:**  
  - High Vendors: Mean Margin = 31.17%  
  - Low Vendors: Mean Margin = 41.55%  
- **Hypothesis Testing:** Statistically significant difference in profit margins → distinct vendor strategies  

---

## How to Run This Project
1. Load CSVs into the database by running [`ingestion_db-checkpoint.py`](./ingestion_db-checkpoint.py)

2. Generate vendor summary using [`get_vendor_summary-checkpoint.py`](./get_vendor_summary-checkpoint.py)

3. Run the notebooks:
   [Exploratory Data Analysis-checkpoint.ipynb](./Exploratory%20Data%20Analysis-checkpoint.ipynb)  
   [Vendor Performance Analysis-checkpoint.ipynb](./Vendor%20Performance%20Analysis-checkpoint.ipynb)



## Final Recommendations

- Diversify vendor base to reduce risk  
- Optimize bulk order strategies  
- Reprice slow-moving, high-margin brands  
- Clear unsold inventory strategically  
- Boost marketing for underperforming vendors




