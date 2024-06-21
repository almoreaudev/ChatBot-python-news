
# ChatBot-python-news

A simple chatbot python which give recent news.




## Installation



### 1. Python environnement

First, install virtualenv for creating python virtual environnement
```bash
pip install virtualenv
```
Then, create the environnement

```bash
python3 -m venv env
```

Finally, activate the environnement
```bash
source env/bin/activate
```

### 2. Install the dependencies
When the environnement is activate, you will see (.venv) at the start of your line command

Exemple :
```bash
(.venv) $ _____
```

You need to install the dependencies with the file requirements.txt 
```bash
pip install -r requirements.txt
```

### 3. Prepare Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Create a .env file with this :

    .env
    
    `GUARDIAN_API_KEY`
    `OPENAI_API_KEY`


## How to use
When the environnement, the dependencies and the environnement variables are setup, you can use the programm

Simply, run the file main.py in the terminal

```bash
python3 main.py
```

To modify the question, go to the main and modify the variable "question" at the start of the file
```python
14 question="Que c'est t'il passé récemment à propos de la France ?"
```