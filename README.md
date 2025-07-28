# 🛡️ Fraud Detection System

Fraud Detection System is a machine learning project built to identify fraudulent financial transactions. Leveraging real-world datasets and the powerful XGBoost algorithm, it detects suspicious activity in transactional data, even in the face of extreme class imbalance.

## 🚀 Features

- 🧠 **Robust ML Model:** Trains on real-world fraud datasets using advanced algorithms like XGBoost.
- 📊 **Class Imbalance Handling:** Special techniques address the rarity of fraud cases (as shown below, fraud is less than 0.5% of all transactions).
- 🧪 **Real-Time Prediction:** Simulates live fraud detection, suitable for integration in real-world systems.
- 📉 **Performance Visualization:** Includes clear model evaluation visualizations (see below).
- 🖥️ **Planned UI:** Upcoming web interface for transaction simulation and fraud alerting.

## 📊 Model Evaluation Insights

### Class Distribution

Most transactions are genuine, with fraud cases extremely rare:


![WhatsApp Image 2025-07-28 at 11 11 53_a0410126](https://github.com/user-attachments/assets/31564a32-0172-41be-9be6-364aab951e19)


### Confusion Matrix

Displays model performance by comparing actual vs. predicted results:


![WhatsApp Image 2025-07-28 at 11 14 51_3d79aad4](https://github.com/user-attachments/assets/0c29a31b-1610-4247-95c3-63cc9f0173fb)


### F1 Score vs. Threshold

Shows how the F1 Score changes with different classification thresholds:


![WhatsApp Image 2025-07-28 at 11 15 00_dd3f1c07](https://github.com/user-attachments/assets/2b7b1bcb-2f2b-44db-a2ab-fa848a1f7777)


### Log Loss Over Epochs

Demonstrates model training and evaluation progress, highlighting convergence:


![WhatsApp Image 2025-07-28 at 11 15 10_9808a27f](https://github.com/user-attachments/assets/8fdc6beb-2105-4bdf-abac-eae5a637f928)


### ⚖️ Precision-Recall Tradeoff

> **Why Prioritize Recall Over Precision?**
>
> In fraud detection, catching as many actual frauds (high recall) is usually more valuable than perfectly avoiding false alarms (high precision). Missing a fraudulent transaction could have severe consequences, so the system is intentionally tuned to flag more suspicious cases. This means some legitimate transactions may be flagged as suspicious, functioning like an alert for review—helpful in real-world fraud prevention.

- **Low precision, high recall:** A safer approach—flagging more transactions as possibly suspicious is generally preferable to missing a fraud.
- **Metrics visualization:** 

![WhatsApp Image 2025-07-28 at 11 15 29_5df208fd](https://github.com/user-attachments/assets/4b0598fb-01fa-45e9-8bbd-8a7a92d8f722)


## 🛠️ Tech Stack

- **Python 3.9+**
- Pandas, Scikit-learn, XGBoost
- Jupyter Notebooks (EDA, prototyping)
- Flask / Streamlit (planned for UI)
- Matplotlib (visualizations)

## 🧾 Requirements

- Python 3.9+
- Install dependencies:
  ```bash
  pip install xgboost pandas scikit-learn matplotlib flask streamlit
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

## 🖼️ How to Add/Edit Visualizations

- All key plots (like those above) are in the `/images` folder and referenced in this README.
- To add your own visualization (e.g., F1/Recall/Precision bar graph), save your figure using matplotlib:
  ```python
  plt.savefig('images/your_plot.png')
  ```
  And include it like:
  ```markdown
  ![Description](images/your_plot.png)
  ```
- For image edits, use Python (matplotlib/plt.annotate), or tools like Canva, PowerPoint, or Photopea for highlights.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) for details.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your proposal.

## 📞 Contact

Questions? Suggestions? Please open an issue or reach out via my [GitHub profile](https://github.com/yashdoke7).
