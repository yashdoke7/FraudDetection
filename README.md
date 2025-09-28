# 🛡️ Fraud Detection System

Fraud Detection System is a machine learning project built to identify fraudulent financial transactions. Leveraging real-world datasets and the powerful XGBoost algorithm, it detects suspicious activity in transactional data, even in the face of extreme class imbalance.

## 🚀 Features

* 🧠 **Robust ML Model:** Trains on real-world fraud datasets using advanced algorithms like XGBoost.
* 📊 **Class Imbalance Handling:** Special techniques address the rarity of fraud cases (fraud <0.5% of all transactions).
* 🧪 **Real-Time Prediction:** Simulates live fraud detection, suitable for integration in real-world systems.
* 🌍 **Geolocation Mapping:** Visualizes fraudulent transactions on an interactive map, enabling investigators and analysts to identify hotspots, fraud-prone regions, and potential organized fraud networks.
* 📉 **Performance Visualization:** Includes clear model evaluation visualizations (confusion matrix, F1 vs threshold, precision–recall tradeoff, etc.).
* 🖥️ **Planned UI:** Upcoming web interface for transaction simulation, fraud alerting, and investigative dashboards.
* 🔒 **Investigation-Oriented Alerts (Planned):** Each flagged transaction can be linked with metadata (location, time, type of fraud) for security teams to act on faster.

## 📊 Model Evaluation Insights

### Class Distribution

Most transactions are genuine, with fraud cases extremely rare:

<img width="500" alt="Class Distribution" src="https://github.com/user-attachments/assets/156e3e83-bddf-4617-a46c-d2c378908132" />

### Confusion Matrix

<img width="500" alt="Confusion Matric" src="https://github.com/user-attachments/assets/4598707c-2d12-4b82-9d18-86cf96b506ac" />

### F1 Score vs. Threshold

<img width="500" alt="F1 Score vs Threshold" src="https://github.com/user-attachments/assets/dc3886df-4658-46ed-919a-40be24b43d29" />

### Log Loss Over Epochs

<img width="500" alt="Log Over Epochs" src="https://github.com/user-attachments/assets/21f7321e-acd1-4b94-ae90-19d446e9c184" />

### ⚖️ Precision-Recall Tradeoff

> **Why Prioritize Recall Over Precision?**
> In fraud detection, catching as many actual frauds (high recall) is usually more valuable than perfectly avoiding false alarms (high precision). Missing a fraudulent transaction could have severe consequences, so the system is intentionally tuned to flag more suspicious cases.

* **Low precision, high recall:** Safer approach—flagging more transactions as suspicious is preferable to missing a fraud.
* **Metrics visualization:**

<img width="500" alt="image" src="https://github.com/user-attachments/assets/3c292010-36d4-4511-8e47-fc2ec10054fa" />

---

### Map for tracking fraud transactions 

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b73dc508-89b2-4163-ac63-6cbb99944160" />

<img width="500" alt="image" src="https://github.com/user-attachments/assets/cf21678d-0678-472f-9058-9b2bdb33a547" />


---

## 🛠️ Tech Stack

* **Python 3.9+**
* Pandas, Scikit-learn, XGBoost
* Flask / Streamlit (planned for UI)
* Matplotlib, Seaborn (visualizations)
* Folium / Plotly (for fraud location mapping)

## 🧾 Requirements

* Python 3.9+
* Install dependencies:

  ```bash
  pip install xgboost pandas scikit-learn matplotlib flask streamlit folium plotly
  ```

## 📦 Dataset

Due to file size, datasets are **not included**. Download directly from [Kaggle](https://www.kaggle.com/datasets/kartik2112/fraud-detection) and place them in `Data/`:

```
/FraudDetection
├── Data/
│   ├── FraudTrain.csv
│   └── FraudTest.csv
├── Model/
├── services/
├── static/
├── templates/
├── fraud_test.py
├── main.py
└── README.md
```

## 🏁 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yashdoke7/FraudDetection.git
   cd FraudDetection
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Download the dataset:** See above.
4. **Run the application:**

   ```bash
   python main.py
   ```

---

## 🌍 Future Enhancements

* **User Dashboard:** Web UI to simulate transactions, visualize fraud alerts, and review flagged cases.
* **Fraud Heatmaps:** Aggregate geospatial patterns to track emerging fraud regions.
* **Explainable AI (XAI):** Feature importance visualization for why a transaction was flagged.
* **Real-Time APIs:** Deployable service to integrate with banking or payment systems.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) for details.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your proposal.

## 📞 Contact

Questions? Suggestions? Please open an issue or reach out via my [GitHub profile](https://github.com/yashdoke7).

---

Do you want me to also create a **screenshot mockup** (map with fraud markers/heatmap) that you can add to the README visuals, so it looks more complete?
