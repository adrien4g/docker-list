# Docker-py

> List the containers created from base directory.

## 💻 Requirements

* `Python 3`
* `Docker`
* `Pip 3`
* Containers created by a docker-compose file

## 🚀 Installation
* Clone repository from gitlab or github
    ```
    git clone https://gitlab.com/adrien4g/docker-list.git
    or
    git clone https://github.com/adrien4g/docker-list.git
    ```
* Install modules
    ```
    cd docker-list
    pip install -r src/requirements.txt
    ```
## 🚀 Installation (Virtual Env)
* Clone repository from gitlab or github
    ```
    git clone https://gitlab.com/adrien4g/docker-list.git
    or
    git clone https://github.com/adrien4g/docker-list.git
    ```

* Create a virtual env
    ```
    cd docker-list
    python3 -m venv .env
    source .env/bin/activate
    ```

* Install modules
    ```
    pip install -r src/requirements.txt
    ```

## ☕ Usage
* Set the base and output directory editing the file `src/config.ini`. Example:
    ```
    [Default]
    base_path = /home/mark/docker/
    output_path = /home/mark/output/
    ```
* Run on your terminal
    ```
    python3 main.py
    ```