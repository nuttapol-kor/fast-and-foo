<div id="top"></div>

# Fast and Foo
*by Big Foo with the T*
***
## Contents
- [Overview](#overview)
- [Features](#features)
   - [APIs features](#apis-features)
   - [Data visualization features](#data-visualization-features)
- [Required libraries and tools](#required-libraries-and-tools)
   - [Prerequisite (required) software](#prerequisite-(required)-software)
      - [How to Check Python Version](#how-to-check-python-version)
      - [How to Check Nodejs Version](#how-to-check-nodejs-version)
   - [Prerequisite (required) database](#prerequisite-(required)-database)
      - [How to create the Database and Table](#how-to-create-the-database-and-table)
- [Instructions for building and running](#instructions-for-building-and-running)    
   - [How to clone Fast and Foo project](#how-to-clone-Fast-and-Foo-project)
   - [Instructions for setting up a virtual environment (virtualenv)](#instructions-for-setting-up-a-virtual-environment-(virtualenv))
   - [Interact with our database](#interact-with-our-database)
- [Team Members](#team-members)

***
## Overview
![0c287d2c0459705e09761c5fd9991f1b.png](https://www.img.in.th/images/0c287d2c0459705e09761c5fd9991f1b.png)
In our daily lives, we must all travel regularly, whether from home to work or from home to university. As a result, travel is a vital and unavoidable aspect of our everyday lives, and vehicles have virtually become an extension of our bodies. It is indisputable that we have no means of knowing how long it will take us to reach our destination or what may cause delays when we are on a vehicle. As a result, it is where our project began. The pain points of our project are that users don't know what days of the week the traffic will be heavy and what variables will cause travel delays. So *Big Foo with the T* team created the **Fast and Foo** project. Our project is to monitor vehicle speed and the factors that influence it. Also show a graph to anticipate which variable affects the vehicle's speed i.e, [air quality](https://aqicn.org/city/bangkok), [humidity](https://en.wikipedia.org/wiki/Humidity), and [PM 2.5](https://molekule.science/what-is-pm-2-5-and-how-can-you-reduce-your-exposure/). **The purpose of the project is to let the user know what variables affect the vehicle speed and average daily speed graph.**

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

## Features
### APIs features
| Method | Endpoint(s) | Feature(s) |
|--------|--------------|------------|
| `GET` | /pm25/`{lat}`/`{lon}`/report|Shows air quality report (Unhealthy, Moderate, or Good)|
| `GET` | /pm25/`{speedId}`|Shows PM 2.5 value|
| `GET` | /speeds |Shows a list of average speed data|
| `GET` | /speeds/`{lat}`/`{lon}`/traffic-report|Shows a traffic report (Clear road or Traffic jam)|
| `GET` | /speeds/`{speedId}` |Shows average speed value in km/hr|
| `GET` | /tmd/`{lat}`/`{lon}`/report|Shows rainfalls report (Rain or Clear sky)|
| `GET` | /tmd/`{speedId}`/humidity|Shows humidity value|
| `GET` | /tmd/`{speedId}`/rainfall|Shows rainfalls value|
| `GET` | /tmd/`{speedId}`/temperature|Shows temperature|

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

### Data visualization features
| Graph Title | Feature(s) |
|----------------------|------------|
|Speed and Date| Let the user knows which days are most likely to be traffic jams, as indicated by the reduced speed. Help the user chooses travel dates that are convenient for travel.|
|Speed and PM 2.5|Shows the user where traffic is prone to traffic jams, which can be seen from the higher PM 2.5 value resulting from the high amount of car smoke along the route resulting in lower average speed.|
|Speed and Rainfalls|Shows the user how much rainfall affects average speed, which is helpful so they can avoid picking days with low temperatures and high humidity that result in rainfall.
|

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

## Required libraries and tools
### Prerequisite (required) software
|    Name of software    | Versions |
|:----------------------:|:--------:|
|Python|Using at least version 3.6 or higher|
|Nodejs|Using at least version 16.13.0 or higher|

* **Python** is a programming language that lets you work more quickly and integrate your systems more effectively.
   - Install [Python](https://www.python.org/downloads/)
* **Nodejs** is a JavaScript runtime built on Chrome's V8 JavaScript engine.
   - Install [Node.js](https://nodejs.org/en/download/)

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

#### How to Check Python Version 
> To check the version installed, open a terminal window and entering the following:
* Linux/MacOS:
    ```
    python3 –-version
    ``` 
* Windows: 
    ``` 
    python ––version
    ```

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

#### How to Check Nodejs Version 
> To check the version installed, open a terminal window and entering the following:
* Linux/MacOS:
    ```
    node –-version
    ``` 
* Windows: 
    ``` 
    node ––version
    ```

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

### Prerequisite (required) database

> Create database and table for connect to Fast and Foo project

#### How to create the Database and Table
   1. Create datebase in phpMyAdmin (MySQL)
   2. Create 3 tables in your datebase with schema as follows:
      - aqiProject ![Imgur](https://i.imgur.com/TOmJ2ko.jpg)
      - speedmeter ![Imgur](https://i.imgur.com/6Bu7II7.jpg)
      - tmdProject ![Imgur](https://i.imgur.com/jTXPN5m.jpg)
<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

## Instructions for building and running

1. **Clone** [Fast and Foo](https://github.com/nuttapol-kor/fast-and-foo) project to your machine. [*See how to clone the project.*](https://github.com/nuttapol-kor/fast-and-foo#how-to-clone-fast-and-foo)

2. Change directory to the directory that contain `fast-and-foo` folder
    ```sh
   cd fast-and-foo
   ```
3. Follows the [**setting up a virtual environment**](https://github.com/nuttapol-kor/fast-and-foo#instructions-for-setting-up-a-virtual-environment-virtualenv).

3. Install required libraries
   ```sh
   pip install -r requirements.txt
   ```
   > Description of the require packages
   * **PyMySQL** This package contains a pure-Python MySQL client library, based on PEP 249. Most public APIs are compatible with mysqlclient and MySQLdb.
   * **python-dotenv** reads key-value pairs from a .env file and can set them as environment variables.
   * **gunicorn** is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model.
4. Install OpenAPI-to-GraphQL
   ```sh
   npm install -g openapi-to-graphql-cli@2.5.0
   ```
   * **OpenAPI-to-GraphQL** generates a GraphQL schema for a given OpenAPI Specification (OAS).
5. Edit `example.env` for your credential
   ```
   OPENAPI_AUTOGEN_DIR="autogen"
   DB_HOST="Your database host"
   DB_USER="Your username"
   DB_PASSWD="Your password"
   DB_NAME="Your table name"
   ```
6. Start the REST API server
   * Linux/MacOS:
      ```
      python3 app.py
      ``` 
   * Windows: 
      ``` 
      python app.py
      ```
   - Swagger UI avalible on http://localhost:8080/speed/v1/ui
   
      * **Swagger UI** allows anyone — be it your development team or your end consumers — to visualize and interact with the API’s resources without having any of the implementation logic in place.
7. In another terminal, start openapi-to-graphql
   ```sh
   openapi-to-graphql --cors -u http://localhost:8080/speed/v1 openapi/speed-api.yaml
   ```
   -  GraphQL window avalible on http://localhost:3000/graphql

8. Open the index page in path of `html\index.html` file
![c9450a73a36714449872e9c2d34a1164.png](https://www.img.in.th/images/c9450a73a36714449872e9c2d34a1164.png)
   - Right click at `html\index.html` file location > Copy Path > Paste path in browser

9. Quit the server
    * Exit the terminal window
        * Linux/MacOS: Press `CTRL + C` button
        * Windows: Press `CTRL + C` button
    
    * Deactivate virtualenv
        ```
        deactivate 
        ``` 

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

### How to clone [Fast and Foo](https://github.com/nuttapol-kor/fast-and-foo) project
* Access to a command-line/terminal window.
    * Linux:
        ```
        CTRL-ALT-T or CTRL-ALT-F2
        ``` 
    * Windows: 
        ``` 
        WIN+R > type powershell > Enter/OK or Type in search tap "cmd"
        ```
    * MacOS: 
        ```
        Finder > Applications > Utilities > Terminal
        ```
* Change directory to the directory that the user wants to run the project.
    ```
    cd directory name
    ```
* Use git clone in the command line. (Link to clone the project `https://github.com/nuttapol-kor/fast-and-foo.git`)
    ```
    git clone https://github.com/nuttapol-kor/fast-and-foo.git
    ```

<p align="right"><i><a href="#contents">Bact to contents</a></i></p>

### Instructions for setting up a virtual environment (virtualenv)
> **a virtual environment** is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.
* Access to a command-line/terminal window.
    * Install a virtual environment.
        * Linux/MacOS:
            ```
            python3 -m pip install virtualenv
            ```
        * Windows:
            ```
            python -m pip install virtualenv
            ```    
    * Create new virtual environment.
        * Linux/MacOS:
            ```
            virtualenv venv
            ```
        * Windows:
            ```
            virtualenv env
            ``` 
    * Activate a virtual environment.
        * Linux/MacOS:
            ```
            . env/bin/activate
            ```
        * Windows:
            ```
            env\Scripts\activate
            ```
<p align="right"><i><a href="#contents">Bact to contents</a></i></p>



### Interact with our database
1. You can just download `openapi-to-graphql` and run with this command
   ```sh
   openapi-to-graphql --cors -u https://daq-fast-and-foo.herokuapp.com/speed/v1 openapi/speed-api.yaml
   ```
   - GraphQL window available on http://localhost:3000/graphql

   *(The query is quite slow, you need to wait for 15-30 second.)*

2. Open the index page in `html\index.html`
<p align="right"><i><a href="#contents">Bact to contents</a></i></p>


## Team Members


> [Nuttapol Korcharoenrat](https://github.com/nuttapol-kor)
<br>
Software and Knowledge Engineering
<br>
Faculty of Engineering
<br>
*Kasetsart University*
<br>
nuttapol.kor@ku.th
<br>
<br>

> [Phinyaphak Chiradejthanankorn](https://github.com/vnsvakanda) <br>
Software and Knowledge Engineering
<br>
Faculty of Engineering
<br>
*Kasetsart University*
<br>
phinyaphak.c@ku.th
<br>
<br>

> [Pitchapa Sae-lim](https://github.com/PitchapaSaelim) <br>
Software and Knowledge Engineering
<br>
Faculty of Engineering
<br>
*Kasetsart University*
<br>
pitchapa.sae@ku.th


<p align="right"><i><a href="#contents">Bact to contents</a></i></p>
