from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
import pandas as pd

# Load data
data = pd.read_csv("C:/Users/USER/Desktop/Data_Science/Test_DataScience/Social_Network_Ads.csv")

x = data.iloc[:, 2:4]
y = data.iloc[:, 4]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=47)

standardScaler = StandardScaler()
x_train = standardScaler.fit_transform(x_train)
x_test = standardScaler.transform(x_test)

gaussianNB = GaussianNB()
gaussianNB.fit(x_train, y_train)

def generate_prediction(age, salary):
    x_test1 = [[age, salary]]
    x_test1 = standardScaler.transform(x_test1)
    y_pred = gaussianNB.predict(x_test1)
    return str(y_pred[0])
