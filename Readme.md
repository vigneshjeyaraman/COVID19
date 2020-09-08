## Welcome to Covidtracker. It provides graph below features
1. Top 15 country mappint
2. Particular Country stats
3. World wide overview

## Setup
Setting up this is very easy.

1. git clone < REPO >

2. create a virtualenv with below command
    * virtualenv -p < location to python3.8 > venv
    ## if it says virtualenv not found you have to run below commands as per you OS
        - Mac- brew install virtualenv (if you don't have brew then run /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)")
        - Ubuntu- sudo apt-get install python-virtualenv

3. Activate the venv you created by running 
    * source venv/bin/activate

4. Install all the dependencies by running
    * pip install -r requirements.txt

6.  Now
    * python manage.py runserver --> It will run project by default on port 8000 if you want to change the port then run
        * python manage.py runserver 9000 --> it can be any port of your choice.

7. Now open localhost:8000 on your web browser.

## It is using Python's Covid module which has inbuilt function to fetch all the required data. We haven't used any DB in this.
https://pypi.org/project/covid/