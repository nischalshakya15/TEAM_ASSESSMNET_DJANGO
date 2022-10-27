## Description 
This project contains the list of API end points for the team assessment. 

## Running the project 
* Install python
* Install **virtualenv**
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
     gunicorn --bind 0.0.0.0:8000 backend.wsgi:application
    ```

## With Docker
* Install the docker and docker compose.
* Run docker compose up.
* Run docker ps to view the running container.