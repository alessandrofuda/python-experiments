### Python3 and ML experiments

#### Glossary
Likelihood = probability
supervised learning = we have already data/values (input/output) to train the model with `train_test_split` method
samples, sampling = campioni, campionamento
LLM = is a Language Model like, for example: GPT-3.5 by OpenAI (..there are much others LLM (ex. PaLM 2 by Google/Bard), also open source (LLaMA, BLOOM, Bert,...))
LangChain framework (for python) = stay between client and LLM/Vector DB. It's like a proxy before LLM. There are others too, like 4 ex: Llamaindex.



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




## Deploy without container
GUNICORN is a substitute of Flask ready to PROD env

`$ pip install gunicorn==20.1.0`  on server


```
$ gunicorn -w 2 -b 0.0.0.0:5000 app:app

[INFO] Starting gunicorn 20.1.0
[INFO] Listening at: http://0.0.0.0:5000 (1)
[INFO] Using worker: sync
[INFO] Booting worker with pid: 3
[INFO] Booting worker with pid: 4
```

## DEPLOY in CONTAINER

In **Nginx** level: configure it as a Reverse Proxy, so, in `example.conf`:
```
#  ROUTING TO DOCKER CONTAINER
server {
        listen 80;
        listen 443 ssl;
        server_name python.example.it;
        
        location / {
                include proxy_params;
                proxy_pass http://localhost:5000;
        }
}
```

Test conf && restart nginx process: 
```
$ sudo nginx -t 
$ sudo systemctl restart nginx
```

Build and Run **docker image**:
```
$ docker build -t test-python-app:1.0 .
$ docker images   # (--> to see generated image)
$ docker run -d -p 5000:5000 --rm --name "test-python-app" test-python-app:1.0
```
(adding `-d` to detach mode, adding --volumes if in dev)

<br><br><br>

### Deploy flow
```
$ git pull

# IF there is '--volumes' on the app code --> Not necessary re-build container
# ELSE --> re-build container
$ docker build -t name-to-assign:TAG .

# restart container (inside: restart web server)
$ docker run -d -p...:... --rm --name .... image-name:TAG
```
see `./deploy.sh` script (wip...)
<br><br><br>

## Deploy using Docker-Compose
Configure all via `docker-compose up`

***...todo...***


<br><br><br><br>

Some other commands:

`pip3 freeze > requirements.txt`


