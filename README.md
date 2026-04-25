# 🎓 Student Performance Prediction App

> An end-to-end Machine Learning web application that predicts students' math scores based on demographic and academic features — built with Python, scikit-learn, and Flask.

## 📌 Overview

This project demonstrates a complete ML pipeline — from raw data ingestion to a live web app — that predicts a student's math exam score using inputs like gender, parental education level, lunch type, and test preparation course completion.

The goal is to help educators and institutions proactively identify students who may need academic support.

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.x |
| ML Library | scikit-learn, XGBoost, CatBoost |
| Web Framework | Flask |
| Data Processing | Pandas, NumPy |
| Model Persistence | Pickle |
| Frontend | HTML, CSS (Jinja2 Templates) |
| Version Control | Git & GitHub |

## 📁 Project Structure

```
Student_Performance_Prediction_App/
│
├── app.py                    # Flask app entry point
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
│
├── artifacts/                # Generated during training
│   ├── model.pkl             # Trained best model
│   ├── preprocessor.pkl      # Feature preprocessor
│   ├── train.csv
│   └── test.csv
│
├── src/
│   ├── exception.py          # Custom exception handling
│   ├── logger.py             # Logging module
│   ├── utils.py              # Helper functions
│   │
│   ├── components/
│   │   ├── data_ingestion.py         # Data loading & splitting
│   │   ├── data_transformation.py   # Preprocessing pipeline
│   │   └── model_trainer.py         # Model training & selection
│   │
│   └── pipeline/
│       ├── predict_pipeline.py       # Inference pipeline
│       └── train_pipeline.py         # Training pipeline
│
├── notebooks/                # EDA & model experimentation
│   └── EDA.ipynb
│
└── templates/
    ├── index.html            # Landing page
    └── home.html             # Prediction form
```

## ⚙️ Features

- **Automated Model Selection** — Trains and evaluates multiple models (Random Forest, XGBoost, CatBoost, Gradient Boosting, AdaBoost) and selects the best by R² score
- **Modular Codebase** — Clean separation of data ingestion, transformation, and model training
- **Custom Logging & Exception Handling** — Production-grade error tracking
- **End-to-End Pipeline** — From raw CSV to live predictions via Flask
- **Interactive Web Interface** — Users enter student details and receive instant score predictions

## 📊 Input Features

| Feature | Description |
|---|---|
| Gender | Male / Female |
| Race/Ethnicity | Group A–E |
| Parental Education | High school to Master's degree |
| Lunch | Standard / Free-Reduced |
| Test Preparation Course | Completed / None |
| Reading Score | Numeric score |
| Writing Score | Numeric score |

**Target:** Math Score (continuous)

## 📈 Model Performance

| Model | R² Score |
|---|---|
| CatBoost | ~0.88 |
| XGBoost | ~0.87 |
| Gradient Boosting | ~0.87 |
| Random Forest | ~0.85 |
| AdaBoost | ~0.82 |

> Best model is automatically selected and saved as `model.pkl`.

## 🔧 Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/jahanvigarg238/Student_Performance_Prediction_App.git
cd Student_Performance_Prediction_App

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
```

Then open your browser and navigate to: `http://127.0.0.1:5000`

## 🧪 How It Works

```
User Input (Web Form)
        ↓
CustomData Class → Converts to DataFrame
        ↓
Load preprocessor.pkl → Feature Encoding & Scaling
        ↓
Load model.pkl → Predict Math Score
        ↓
Display Result on Web Page
```

## 📦 Dataset

- **Source:** [Kaggle – Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Size:** ~1,000 records
- **Features:** 8 (7 input + 1 target)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests with improvements

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👩‍💻 Author

**Jahanvi Garg**  
[GitHub](https://github.com/jahanvigarg238) • [LinkedIn](#)

---

> ⭐ If you found this project helpful, please consider giving it a star!
