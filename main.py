import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
df = pd.read_csv("flats_moscow.csv")


df = df.drop(columns=['code','livesp','kitsp','dist','metrdist','walk','brick','floor'])

x = df[['totsp']]
y = df['price']

model = LinearRegression()

model.fit(x,y)

print('Модель успешно обучено!')

def predict_price(metrs):
	metrs_array = np.array([[metrs]])
	predicted = model.predict(metrs_array)
	return int(predicted[0])

user_input = int(input("Узнайте цену кв.метр: "))

estimated_price = predict_price(user_input)

turn_to_tenge = estimated_price * 4470.24

print(f'Примерная цена за {user_input} кв.м: {turn_to_tenge} тг')

