# Objectives APIs

These APIs include only CRUD objectives.

## How to run this?

### Create virtual environment

First run the command `python -m venv venv`

Do NOT forget to activate the virtualenv using the command

Windows: `call venv/Scripts/activate`

Linux / macOs: `src venv\bin\activate`

### Install the packages

After you activate the virtual environment as mentioned above, run the command `pip install -r requirements.txt`

### Run server

Now you can run the server with the following command: `uvicorn my_app.main:app --reload`

### Links

The RESTful API can be found here:

```
http://127.0.0.1:8000/objectives/
```

Documentation can be found here:

```
http://127.0.0.1:8000/docs
```
