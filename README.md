# Mtcars Flask API

This project builds a linear regression model using the `mtcars.csv` dataset to predict miles-per-gallon (`mpg`) and serves predictions via a Flask API inside a Docker container.

## Files in this Repo

- `mtcars.csv`: Dataset used to train the model  
- `prediction.py`: Defines the model and prediction function  
- `server.py`: Flask API with prediction and home routes  
- `Dockerfile`: Container configuration  
- `requirements.txt`: Python dependencies  
- `README.md`: Instructions for building and testing

## Step-by-Step Instructions 

### Step 1: Clone the repo
```bash
git clone https://github.com/yesitsmary/Mtcars-Flask-API.git
cd Mtcars-Flask-API
```

### Step 2: Build and run  Docker container
```bash
docker build -t mtcars-flask-api .
docker run -p 8080:8080 mtcars-flask-api
```

### Step 3: Tag and push image to DockerHub
#### *This step is only required if you plan to deploy to a cloud platform like Google Cloud Run.*
```bash
docker tag mtcars-flask-api maryv8/mtcars-flask-api:latest
docker push maryv8/mtcars-flask-api:latest
```

### Step 4: Send a test prediction
```bash
curl -X POST http://localhost:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'
```
