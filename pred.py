#Import the libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
import yfinance as yf
from keras.models import Sequential
from datetime import datetime
import pickle
import keras


def main_prediction(symbol):
   today=datetime.utcnow().date()
   scalar=MinMaxScaler(feature_range=(0,1))

   reconstructed_model = keras.models.load_model("model")

   #Get the quote
   df = yf.download(symbol, data_source='yahoo', start='2021-05-28',end=today)
   #Create a new dataframe
   new_df = df.filter(['Close'])
   #Get teh last 60 day closing price 
   last_60_days = new_df[-60:].values
   #Scale the data to be values between 0 and 1
   last_60_days_scaled = scalar.fit_transform(last_60_days)
   #Create an empty list
   X_test = []
   #Append teh past 60 days
   X_test.append(last_60_days_scaled)
   #Convert the X_test data set to a numpy array
   X_test = np.array(X_test)
   #Reshape the data
   X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
   #Get the predicted scaled price
   pred_price = reconstructed_model.predict(X_test)
   #undo the scaling 
   pred_price = scalar.inverse_transform(pred_price)
   print(pred_price)
   return pred_price



