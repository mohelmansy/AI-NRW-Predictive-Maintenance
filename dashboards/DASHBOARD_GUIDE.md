# 📊 DASHBOARD_GUIDE.md

## 🎯 Purpose
This guide explains how to build and use the **AI-NRW Predictive Maintenance Dashboard** in Power BI Desktop using the provided dataset.

---

## 📁 Files
- `mock_powerbi_data.csv`: Dataset containing mock asset and KPI data.
- `AI_NRW_Dashboard.pbix`: Placeholder Power BI file to save your final report.
- Dashboard visuals include:
  - Failure by Zone (Bar Chart)
  - KPI Performance (Radar/Spider Chart)
  - Asset Summary Table

---

## 🧰 Tools Needed
- **Power BI Desktop** (Free from Microsoft Store)
- Import the `mock_powerbi_data.csv` as your data source.

---

## 🛠️ Step-by-Step Instructions

### 1. Open Power BI Desktop
- Launch the Power BI Desktop application.

### 2. Import the Dataset
- Go to **Home > Get Data > Text/CSV**.
- Select `mock_powerbi_data.csv`.
- Click **Load**.

### 3. Create Visuals

#### 🔹 Failure by Zone Chart
- Visualization: **Stacked Bar Chart**
- Axis: `Zone`
- Legend: `Failure`
- Values: `Asset_ID` (Count)

#### 🔹 KPI Radar Chart
- Go to **Visualizations > Get more visuals > AppSource**
- Search and install **Radar Chart**
- Add: 
  - Axis: `KPI_ResponseTime`, `KPI_RepairSLA`, `KPI_Reporting`, `KPI_Feedback`
  - Group by: `Contract_Name`

#### 🔹 Asset Summary Table
- Visualization: **Table**
- Columns: `Asset_ID`, `Zone`, `Asset_Type`, `Failure`, `Run_Hours`, `Temperature`, `Pressure`, etc.

### 4. Add Filters
- Use slicers for:
  - `Zone`
  - `Asset_Type`
  - `Contract_Name`
  - `Failure`

---

## ✅ Tips
- Save your final dashboard as `AI_NRW_Dashboard.pbix`.
- Publish it to Power BI Service for sharing and scheduling.
- Add a report tooltip with probability bands if integrating model output.

---

## 👨‍💼 Contact
For guidance or customization, contact:  
**Mohamed Elmansy**  
📧 mohammedelmansy@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/mohamedsaad-eldin)

