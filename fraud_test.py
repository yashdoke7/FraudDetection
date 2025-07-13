import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

ms_model = XGBClassifier()
ms_model.load_model(r"C:\Users\Yash\Desktop\CS\College\Projects\FraudDetection\xgboost_model_2.json")  # Path to your JSON file


fraud_train_df = pd.read_csv(r"C:\Users\Yash\Desktop\CS\College\Projects\FraudDetection\CSV\FraudTrain.csv")
fraud_test_df = pd.read_csv(r"C:\Users\Yash\Desktop\CS\College\Projects\FraudDetection\CSV\FraudTest.csv")
mostly_synthetic = pd.read_csv(r"C:\Users\Yash\Desktop\CS\College\Projects\FraudDetection\CSV\synthetic_data.csv")


fraud_train_df.drop(["trans_date_trans_time","first","last","dob","cc_num","gender","street","city","state","zip","lat","long","city_pop","trans_num","merch_lat","merch_long","unix_time"], axis=1, inplace = True)
fraud_train_df["category"] = fraud_train_df["category"].astype("category")
fraud_train_df["job"] = fraud_train_df["job"].astype("category")
fraud_train_df["merchant"] = fraud_train_df["merchant"].astype("category")

fraud_test_df.drop(["trans_date_trans_time","first","last","dob","cc_num","gender","street","city","state","zip","lat","long","city_pop","trans_num","merch_lat","merch_long","unix_time"], axis=1, inplace = True)
fraud_test_df["category"] = fraud_test_df["category"].astype("category")
fraud_test_df["job"] = fraud_test_df["job"].astype("category")
fraud_test_df["merchant"] = fraud_test_df["merchant"].astype("category")

mostly_synthetic.drop(["trans_date_trans_time"], axis=1, inplace = True)
mostly_synthetic["category"] = mostly_synthetic["category"].astype("category")
mostly_synthetic["job"] = mostly_synthetic["job"].astype("category")
mostly_synthetic["merchant"] = mostly_synthetic["merchant"].astype("category")


X3 = fraud_test_df.drop(["is_fraud"], axis = 1)
y3 = fraud_test_df["is_fraud"]
X_ms = mostly_synthetic.drop(["is_fraud"], axis = 1)
y_ms = mostly_synthetic["is_fraud"]

X3 = X3.drop(columns=["Unnamed: 0"], errors="ignore")

X_ms_train, X_ms_test, y_ms_train, y_ms_test = train_test_split(X_ms, y_ms, test_size = 0.2, random_state = 42)


df_combined = pd.concat([fraud_train_df, mostly_synthetic], axis=0)

df_combined = df_combined.sample(frac=1, random_state=42).reset_index(drop=True)

X_ms_train = df_combined.drop('is_fraud', axis=1)
y_ms_train = df_combined['is_fraud']

X_ms_train = X_ms_train.drop(columns=["Unnamed: 0"], errors="ignore")
X3_ms = X3.drop(columns=["Unnamed: 0"], errors="ignore")
X_ms_train = X_ms_train.drop(columns=["year","month"], errors="ignore")
X3_ms = X3_ms.drop(columns=["year","month"], errors="ignore")


def predict_transaction(merchant, category, job, amt):
    input_df = pd.DataFrame([{
        "merchant": merchant,
        "category": category,
        "amt": amt,
        "job": job
    }])

    merchant_cats = X_ms_train["merchant"].cat.categories
    job_cats = X_ms_train["job"].cat.categories
    category_cats = X_ms_train["category"].cat.categories

    input_df["merchant"] = input_df["merchant"].astype(pd.CategoricalDtype(categories=merchant_cats))
    input_df["job"] = input_df["job"].astype(pd.CategoricalDtype(categories=job_cats))
    input_df["category"] = input_df["category"].astype(pd.CategoricalDtype(categories=category_cats))

    y_pred = ms_model.predict(input_df)
    return int(y_pred[0])