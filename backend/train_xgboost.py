import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
import joblib

df = pd.read_csv("../data/sales.csv")

label = LabelEncoder()

df['category'] = label.fit_transform(df['category'])
df['season'] = label.fit_transform(df['season'])
df['customer_segment'] = label.fit_transform(df['customer_segment'])

X = df[
    [
        'category',
        'units_sold',
        'season',
        'customer_segment',
        'inventory',
        'competitor_price'
    ]
]

y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Improved XGBoost MAE:", mae)

joblib.dump(
    model,
    "../models/xgboost_pricing_model.pkl"
)