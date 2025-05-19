

```markdown
# 🏠 House Price Prediction Web App

This is a Django-based web application that predicts house prices using a pre-trained machine learning model. The user inputs features such as income, house age, number of rooms, bedrooms, and population, and the app returns a predicted house price.

---

## 🚀 Features

- Built with Django (Python Backend Framework)
- Takes user input from a web form
- Uses a trained scikit-learn model to predict house price
- Clean and minimal UI with predictions rendered on a results page

---

## 📁 Project Structure

```

HousePricePrediction/
├── HousePricePrediction/
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── predict/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   └── result.html
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── model/
│   └── model.pkl
├── static/
├── db.sqlite3
├── manage.py
└── README.md

````

---

## ⚙️ Requirements

- Python 3.10+
- Django 5.x
- scikit-learn
- numpy
- joblib or pickle

Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## 💡 How to Use

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

2. **Run the server**

```bash
python manage.py runserver
```

3. **Access the app**

Go to `http://127.0.0.1:8000/` in your browser.

4. **Enter the inputs** and view the predicted house price on the result page.

---

## 🧠 Model Training

The machine learning model was trained using `scikit-learn` and saved as `model.pkl`. The features used:

* Median Income
* House Age
* Number of Rooms
* Number of Bedrooms
* Population

---

## 🛠️ Deployment (Optional)

You can deploy this project to platforms like:

* **Render**
* **Railway**
* **Heroku**
* **VPS** (e.g., DigitalOcean)

## 👨‍💻 Author

**Shubham Sharma**

---

## 📄 License

MIT License

```
