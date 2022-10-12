### Question 1

Version of pipenv: `**version 2022.10.11**`

### Question 2

- Use Pipenv to install Scikit-Learn version 1.0.2
- What's the first hash for scikit-learn you get in Pipfile.lock?
	
"sha256:08ef968f6b72033c16c479c966bf37ccd49b06ea91b765e1cc27afefe723920b"

- Download these models (trained and saved with pickle) using wget:
```
PREFIX=https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```

### Question 3

- Write a script to load models from question 2
- Score this client: `{"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}`
- Probability that the client will get a credit card: `**0.162**`

### Question 4

- Serve the model as a web service:
	- Install flask and gunicorn
	- Write flask code for serving the model
	- Score this client using `requests`:
	`client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}`
	- What is the probability that this client will get a credit card: `**0.928**`

### Question 5

- Download this base image using `docker pull`: ```svizor/zoomcamp-model:3.9.12-slim```
- What is it's size: `**125MB**`

- Create a dockerfile based on the image and build it.

### Question 6

- Run the docker container
- Score the client in Question 4 again
- What is the probability that the client will get a credit card now: `**0.769**` 
