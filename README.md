# Medical Cost Prediction System

> An AI-powered web application that predicts individual medical insurance costs using Machine Learning.

---

## Overview

The **Medical Cost Prediction System** is designed to estimate healthcare insurance expenses based on personal and lifestyle factors such as age, BMI, smoking habits, and region.

It leverages **Machine Learning (Random Forest Regressor)** to provide accurate, real-time predictions, helping individuals and insurance providers make informed financial decisions.

---

## Features

* Real-time medical cost prediction
* User-friendly web interface (Flask-based)
* High accuracy model (~85%+)
* Data visualization for insights
* Scalable and accessible system
* Clean UI with smooth navigation

---

## Machine Learning Model

* **Algorithm:** Random Forest Regressor
* **Type:** Ensemble Learning (Regression)
* **Why Used:**

  * Handles both categorical & numerical data
  * Reduces overfitting
  * High prediction accuracy
  * Provides feature importance insights

---

## Input Parameters

The model predicts cost based on:

* Age
* Gender
* BMI (Body Mass Index)
* Number of Children
* Smoking Status
* Region

---

##  Tech Stack

### Programming

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

###  Web Development

* Flask
* Flask-CORS

###  Model Handling

* Joblib

###  Frontend

* HTML
* CSS
* Materialize CSS

---

## Project Architecture

```
User Input → Flask Backend → Data Processing → ML Model → Prediction → UI Output
```

### Components:

* Frontend (HTML, CSS)
* Backend (Flask)
* ML Model (Random Forest)
* Model File (.pkl)
* Templates & Static Files

---

## Workflow

1. User enters details in the web form
2. Data is sent to Flask backend
3. Backend preprocesses input
4. ML model predicts insurance cost
5. Result is displayed instantly

---

## Example Output

```
Expected amount is $3957.76
```

---

## Use Cases

* Financial planning for individuals
* Insurance risk assessment
* Healthcare analytics insights
* Cost transparency for users

---

## Why This Project Matters

* Rising healthcare costs demand accurate predictions
* Helps users plan budgets effectively
* Enables insurers to evaluate risk profiles
* Supports data-driven healthcare decisions

---

## Performance Metrics

* Model Accuracy: 85%+
* Evaluation Metrics:

  * R² Score
  * Mean Squared Error (MSE)

---

## Future Enhancements

* Deep Learning integration
* Mobile application (iOS & Android)
* More features (medical history, lifestyle)
* Integration with insurance providers

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/<your-username>/Medical-Cost-Prediction.git
cd Medical-Cost-Prediction
```

### Create Virtual Environment

```bash
py -3.8 -m venv venv
```

### Activate Environment

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000/
```

---

## System Requirements

### Hardware

* CPU: Dual-Core (Min) / Quad-Core (Recommended)
* RAM: 4GB (Min) / 8GB+ (Recommended)

### Software

* Python 3.8+
* VS Code / PyCharm
* Chrome / Firefox

---

## Application Pages

* Home Page → Input user data
* Prediction Page → Displays cost
* About Page → Project details

---

## Conclusion

This project demonstrates how **Machine Learning + Web Development** can be combined to solve real-world problems like healthcare cost prediction.

It provides a **practical, scalable, and user-friendly solution** for accurate insurance estimation.

