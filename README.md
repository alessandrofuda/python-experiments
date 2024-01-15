### Python3 and ML experiments

Likelihood = probability

supervised learning = we have already data/values (input/output) to train the model with `train_test_split` method

ML Process:

1. data collection (pd.read_csv('...csv'))
2. data exploration (df.shape, df.info(), df.describe() .plot() charts...)
3. data preparation 
   - check/resolve missing data (dropna(), fillna() ...), 
   - normalize data,
   - split train/test data and input/output (x/y), split data 'horizontally'/'vertically'

     `x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state  = 1234)`

     Feature = Input = Independent Variables = x
     
     Target = Output = Dependent Variable (Only one) = y  ==> TO PREDICT by Model

These 3 steps get 80% of the time

4. modeling (train model via train data)
   - `LinearRegression().fit(x_train, y_train)`
5. evaluation (accuracy of the model comparing test run results with real data)
   - `model.score(x_test, y_test)`
   - `y_pred = model.predict(x_test)`

These 2 steps iterate to find model that have the best accuracy rate

6. actionable insight



<br><br><br><br>


Other notes:
- to launch jupyter `jupyter notebook`