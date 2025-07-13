# 🛡️ Fraud Detection System
Fraud Detection System is a machine learning-based project designed to identify fraudulent financial transactions. It uses real-world datasets and applies algorithms like XGBoost to detect suspicious patterns in transactional behavior.

---

## 🚀 Features
- 🧠 ML model training using real-world fraud datasets
- 📊 High class imbalance handling using XGBoost
- 🧪 Real-time fraud prediction simulation
- 🌍 Kaggle-hosted datasets for large-scale training
- 🖥️ Planned UI for payment simulation and alerting

---

## 🛠️ Tech Stack
- Python
- Pandas, Scikit-learn, XGBoost
- Flask / Streamlit (planned for UI)
- Jupyter Notebooks (for EDA and prototyping)

---

## 🧾 Requirements
- Python 3.9+
- `xgboost`, `pandas`, `scikit-learn`, `matplotlib`, `flask` or `streamlit`

---

## 📦 Dataset
Due to file size limitations, the datasets are **not included in this repo**.

Download them directly from [this Kaggle dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection)

Place them in a `datasets/` folder like:
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

---

## 🏁 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashdoke7/FraudDetection.git
   cd FraudDetection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install xgboost pandas scikit-learn matplotlib flask streamlit
   ```

3. **Download the dataset**
   - Download from [Kaggle](https://www.kaggle.com/datasets/kartik2112/fraud-detection)
   - Extract and place in `Data/` folder

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📞 Contact
For questions or suggestions, please open an issue on this repository or contact me via my [GitHub profile](https://github.com/yashdoke7).
