from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def home(request):
    return render(request,'home.html')
def predict(request):
    return render(request,'predict.html')
def result(request):
    df = pd.read_csv('/home/shubham-sharma/Downloads/HousePricePrediction/USA_Housing.csv')
    df.drop('Address',axis=1,inplace=True)
    df.isnull().sum()

    X = df.drop('Price',axis=1)
    y = df['Price']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=10)
    model = LinearRegression()
    model.fit(X_train,y_train)

    income = float(request.GET['income'])
    house_age = float(request.GET['house_age'])
    rooms = float(request.GET['rooms'])
    bedrooms = float(request.GET['bedrooms'])
    population = float(request.GET['population'])

    pred = model.predict(np.array([[income,house_age,rooms,bedrooms,population]]))
    pred = round(pred[0])

    price = f"The predicted price is ${pred}"
    return render(request,'predict.html', {"result2":price})