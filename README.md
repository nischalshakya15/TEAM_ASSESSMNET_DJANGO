## Description 
This project contains the list of API end points for the team assessment. 

## Setup 
* Install the python
* Install the **virtualenv**
    ```shell
    sudo apt-get install virtualenv
    ```
* Create the **virtualenv**
    ```shell
    virtualenv venv
    source venv/bin/activate
    ```
* Install the **pip**
    ```shell
    sudo apt-get install python-pip
    ```
* Install the dependencies from **requirements.txt**
    ```shell
    pip install -r requirements.txt
    ```

* Run the application 
    ```shell
     gunicorn --bind 0.0.0.0:8000 team_assessment_comparison_backend.wsgi:application
    ```
