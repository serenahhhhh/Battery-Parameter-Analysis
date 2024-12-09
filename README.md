# **Battery Parameter Analysis**

## **Overview**
This project analyzes the NASA Battery Dataset to study how battery parameters such as **Electrolyte Resistance (`Re`)** and **Charge Transfer Resistance (`Rct`)** change as the battery ages through charge/discharge cycles. The analysis is visualized using Plotly to better understand battery degradation patterns.

---

## **Dataset Description**
The dataset contains data from Li-ion batteries subjected to various tests, including charge, discharge, and electrochemical impedance spectroscopy (EIS). Key features include:
- **`Re`**: Estimated electrolyte resistance (Ohms).
- **`Rct`**: Estimated charge transfer resistance (Ohms).
- **`test_id`**: Test cycle or measurement identifier.
- **`ambient_temperature`**: Temperature during the tests.

### **Source**
The dataset is part of NASA's publicly available battery data collection.  
[Kaggle: NASA Battery Dataset](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset)

---

## **Project Structure**
The repository contains the following:
- **`metadata.csv`**: The dataset used for analysis.
- **`assi.py`**: Python script containing the code for data processing, visualization, and analysis.
- **Plots**: Scatter plots showing trends in `Re` and `Rct` over battery cycles.

---

## **Features**
- **Visualization**: 
  - Scatter plots for `Re` and `Rct` vs. `test_id`.
  - Trendlines using LOWESS smoothing to observe patterns over time.
  - Data points colored by `ambient_temperature`.

---

## **Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/battery-parameter-analysis.git
