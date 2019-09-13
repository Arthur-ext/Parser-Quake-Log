# Quake Log Parser - test

## quake log parser

This project runs on Python>=3.6

## Installation

### Step 1 - create and use a virtualenv:

Install virtualenv: 
``` $ pip install virtualenv ```

Create virtualenv
``` $ virtualenv venv ```

Use virtualenv
``` $ source venv/bin/activete ```

### Step 2 - Install python dependencies

Install python dependencies in virtualenv
``` $ pip install -r requirements.txt ```

### Step 3 - Create containers docker to use MongoDB:

Run docker-compose.yml
``` $ docker-compose up -d ```

## Using - Parser

View Parser description/help
``` $ python main.py -l games.log -h ```

### Run parser - Task 1
``` $ python main.py -l games.log ```

### Run parser - Task 2
``` $ python main.py -l games.log -r ```

## Using - API (Task 3)

#### First save parsed object in MongoDB
``` $ python main.py -l games.log -s ```

#### Access `api/` directory

### Run api
``` $ python exec.py ```

### Example consult
##### All games
`` http://localhost:5000/games ``

##### One Game
`` http://localhost:5000/games/1 ``

in this example 1 is a number of the game