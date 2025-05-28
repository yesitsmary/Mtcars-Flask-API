# Mtcars Flask API

This project builds a linear regression model using the `mtcars.csv` dataset to predict miles-per-gallon (`mpg`) and serves predictions via a Flask API inside a Docker container.

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

# (Optional but required for deployment)
docker tag mtcars-flask-api maryv8/mtcars-api:latest
docker push maryv8/mtcars-flask-api:latest
```

### Step 3: Send a test prediction
```bash
curl -X POST http://localhost:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'
```
