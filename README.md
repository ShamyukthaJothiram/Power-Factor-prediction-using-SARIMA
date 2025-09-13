# Power-Factor-prediction-using-SARIMA
## **Project Overview**

This project implements a Seasonal AutoRegressive Integrated Moving Average with Exogenous Variables (SARIMAX) model to predict power factor (PF) variations in the Southern Indian Power Grid.
The model captures seasonality, temporal dependencies, and noise patterns in grid performance data, enabling accurate PF forecasting for improved grid reliability, load balancing, and energy efficiency.
<br>

## **Why Predict Power Factor?**

Power factor is vital for substations and medium-to-large industries as it affects energy efficiency, equipment lifespan, and operational costs. A low power factor causes higher losses, reduced capacity, and utility penalties, while accurate prediction and control help ensure stable voltage, lower costs, and reliable grid operation.

<br>

**Predicting PF helps in**

1.  Grid stability assessment

2.  Demand-side management

3.  Reducing operational costs

4.  Enhancing energy efficiency

<br>

## **Background of Dataset**

This project is based on the Electric Power Load Dataset, which provides real-world substation measurements from Godishala, Huzurabad, Telangana, India. Key details:

Source: 33/11 kV substation, data collected for the entire year 2021

Frequency: Hourly measurements → 8,760 data points

Features included:

1.  Voltage (kV)

2.  Current (Amps)

3.  Power Factor (PF)

4.  Power (kW)

5.  Temperature (°F)

6.  Humidity (%)

7.  Day status (Weekday/Weekend)

8.  Season (Winter, Summer, Rainy)

Missing data: ~66 values (imputed using averages from nearby hours/days)

Load statistics: Mean ≈ 2130 kW, Peak ≈ 6306 kW, Std Dev ≈ 1302 kW

Citation: Veeramsetty, Venkataramana; Sushma Vaishnavi, Gudelli; Sai Pavan Kumar, Modem; Sumanth, Nagula; Prasanna, Potharaboina (2022), “Electric power load dataset”, Mendeley Data, V1, doi: 10.17632

[Dataset link](https://data.mendeley.com/datasets/tj54nv46hj/1)

<br>

## **Why SARIMAX?**

The SARIMA framework is well-suited for this application as it explicitly accounts for seasonality, temporal dependencies, and stochastic noise components inherent in grid performance metrics

SARIMAX extends SARIMA by handling exogenous variables, making it well-suited for grid data influenced by seasonal cycles (daily/weekly demand) and external conditions.

Captures both:

Short-term dependencies (p, q terms)

Long-term seasonality (P, Q, s terms)

Provides a robust statistical baseline before moving to complex deep learning models.

<br>

## **Methodology**

1. Load Dataset

2. Preprocessing

3. Split training and testing data

4. Model Selection and parameter tuning

5. Fitted SARIMAX on training data.

6. Evaluation and predicted PF on test data

7. Compare Predicted vs Actual values with plots

8. Calculated error metrics (MAE, RMSE)

<br>

## **Results**
