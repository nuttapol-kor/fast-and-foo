<div id="top"></div>

Fast and Foo
===========================================

<!-- ABOUT THE PROJECT -->
## About The Project
The Fast and Foo project establishes a link between vehicle speed and meteorological variables. Measure vehicle speed and factors influencing vehicle speed i.e, Air quality, Humidity that affect the speed and density of traffic.

### Prerequisites
  1. Install [Node.js](https://nodejs.org/en/download/)
  2. Install [Python](https://www.python.org/downloads/)
  3. Create database and table for connect to this project see on the below section

### Database and Table
   1. Create datebase with any name in phpMyAdmin (MySQL)
   2. Create 3 table in the datebase that you just created
      - aqiProject ![Imgur](https://i.imgur.com/TOmJ2ko.jpg)
      - speedmeter ![Imgur](https://i.imgur.com/6Bu7II7.jpg)
      - tmdProject ![Imgur](https://i.imgur.com/jTXPN5m.jpg)
<p align="right">(<a href="#top">back to top</a>)</p>

## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/nuttapol-kor/fast-and-foo.git
   ```
2. Change directory
    ```sh
   cd fast-and-foo
   ```
3. Install required libraries
   ```sh
   pip install -r requirements.txt
   ```
4. Install OpenAPI-to-GraphQL
   ```sh
   npm install -g openapi-to-graphql-cli@2.5.0
   ```
5. Edit `example.env` for your credential
   ```
   OPENAPI_AUTOGEN_DIR="autogen"
   DB_HOST="Your database host"
   DB_USER="Your username"
   DB_PASSWD="Your password"
   DB_NAME="Your table name"
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
1. Start the REST API server
   ```sh
   python app.py
   ```
   - swagger tool avalible on http://localhost:8080/speed/v1/ui
2. Start openapi-to-graphql in another terminal
   ```sh
   openapi-to-graphql --cors -u http://localhost:8080/speed/v1 openapi/speed-api.yaml
   ```
   -  GraphQL window avalible on http://localhost:3000/graphql
3. Open the index page in `html\index.html`

## Interact with our database
1. Your can just download openapi-to-graphql and run with this command
   ```sh
   openapi-to-graphql --cors -u https://daq-fast-and-foo.herokuapp.com/speed/v1 openapi/speed-api.yaml
   ```
   - GraphQL window avalible on http://localhost:3000/graphql

But the query it quite slow, you need to wait for 15-30 second

2. Open the index page in `html\index.html`
<p align="right">(<a href="#top">back to top</a>)</p>

## Contributor

- Nuttapol Korcharoenrat 6210546404 nuttapol.kor@ku.th
- Pitchapa 	Sae-lim 6210546421 pitchapa.sae@ku.th
- Phinyaphak Chiradejthanankorn 6210545572 phinyaphak.c@ku.th

<p align="right">(<a href="#top">back to top</a>)</p>
