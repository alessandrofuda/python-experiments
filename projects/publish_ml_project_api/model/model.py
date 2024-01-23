import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
import joblib


def create_model(current_dir):
    df = pd.read_csv('../../../data/salaries-2023.csv')

    # filter only some languages to train the model, excluding "go" and others
    allowed_languages = ['php', 'js', '.net', 'java']
    df = df[df['language'].isin(allowed_languages)]

    # Fixing the city names
    vilnius_names = ['Vilniuj', 'Vilniua', 'VILNIUJE', 'VILNIUS', 'vilnius', 'Vilniuje']
    condition = df['city'].isin(vilnius_names)
    df.loc[condition, 'city'] = 'Vilnius'

    kaunas_names = ['KAUNAS', 'kaunas', 'Kaune']
    condition = df['city'].isin(kaunas_names)
    df.loc[condition, 'city'] = 'Kaunas'

    # Cities we want to use in our model
    allowed_cities = ['Vilnius', 'Kaunas']
    df = df[df['city'].isin(allowed_cities)]

    # Filtering out  the salaries  that are too high
    df = df[df['salary'] <= 6000]

    # for the moment, go next ...
    one_hot = pd.get_dummies(df['language'],
                             prefix='lang')  # generate BOOL cols foreach different values in 'language' col
    df = df.join(one_hot)
    df = df.drop('language', axis=1)
    # print(df)

    one_hot = pd.get_dummies(df['city'], prefix='city')
    df = df.join(one_hot)
    df = df.drop('city', axis=1)
    # print(df)

    print(df)
    x = df.iloc[:, 0:2].values
    y = df.iloc[:, 2].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(x_train, y_train)

    # here we might add testing with model.predict(x_test) to calculate accuracy_score
    # ...

    joblib.dump(model, os.path.join(current_dir, 'model.pkl'))


def predict_salary(experience, level):
    current_dir = os.path.dirname(__file__)

    # check if model already exists, if not --> create it
    if not os.path.isfile(os.path.join(current_dir, 'model.pkl')):
        create_model(current_dir)

    # Load saved model
    model = joblib.load(os.path.join(current_dir, 'model.pkl'))
    # Use the loaded model to make predictions
    salaries = model.predict([[int(level), int(experience)]])

    return salaries[0]

# predict a salary by seniority and experience years
# predicted_salaries = model.predict([[3, 8]])  # 3 is seniority level, 8 is years of experience
# print(predicted_salaries)  # 3391.89

# print(predict_salary(10, 3))

