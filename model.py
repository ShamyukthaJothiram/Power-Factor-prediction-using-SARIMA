#imports
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

#1. Load datasets
df = pd.read_excel("datasets.xlsx")

#2. data preprocessing
df['datetime'] = pd.to_datetime(                                               # standardize date and time into datetime
    df['DATE'].astype(str) + " " + df['TIME'].astype(str),
    errors="coerce", dayfirst=True
)

df = df.dropna(subset=['datetime'])                                            # Drop rows where datetime failed
df.fillna(method='ffill', inplace=True)                                        # auto-fill empty cells to avoid NaN errors

# 3. Set index
df.set_index('datetime', inplace=True)

#4. Select series 
series = df['PF'].dropna()
y = df['PF']                                                                   # to be predicted    

#Scale series (optional)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['VOLTAGE', 'CURRENT', 'POWER (KW)', 'Temp (F)', 'Humidity (%)']])
X = pd.DataFrame(X_scaled, index=df.index, columns=['VOLTAGE', 'CURRENT', 'POWER (KW)', 'Temp (F)', 'Humidity (%)'])  # features on which PF depends on

#5. Split training and testing data
y_train, y_test, X_train, X_test = train_test_split(y, X, test_size=0.2, shuffle=False)

#6. auto tune parameters
model = SARIMAX(
    y_train,
    exog=X_train,
    order=(1,1,1),                 # ARIMA part
    seasonal_order=(2,2,1,24),     # Example seasonal (24 for hourly daily seasonality)
    enforce_stationarity=False,
    enforce_invertibility=False
)

#7. fit model
model_fit = model.fit(disp=False)
print(model_fit.summary())

# 8. Forecast test data
train_pred = model_fit.predict(start=y_train.index[0], end=y_train.index[-1], exog=X_train)      # Predict result for training data
test_pred=model_fit.forecast(steps=len(y_test), exog=X_test)                                     # Predict result for test data

#9. Evaluate
mse = mean_squared_error(y_test, test_pred)
print(f"Test MSE: {mse}")

#10. plot results
plt.figure(figsize=(20,10))

plt.plot(y_train.index, y_train, label="Training Data")
plt.plot(y_train.index, train_pred, label="Predicted PF (Train)", color="green", linestyle="--")

plt.plot(y_test.index, y_test, label="Testing Data", color="blue")
plt.plot(y_test.index, test_pred ,label="Predicted PF (Test)", color="red", linestyle="--")

plt.title("Power Factor: Train vs Test Forecasting")
plt.xlabel("Time")
plt.ylabel("Power Factor")
plt.legend()
plt.show()

