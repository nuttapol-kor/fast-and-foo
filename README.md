<div id="top"></div>

Fast and Foo
===========================================

<!-- ABOUT THE PROJECT -->
## About The Project
The Fast and Foo project establishes a link between vehicle speed and meteorological variables. Measure vehicle speed and factors influencing vehicle speed i.e, Air quality, Humidity that affect the speed and density of traffic.

### Prerequisites
  1. Install [Node.js](https://nodejs.org/en/download/)
  2. Install [Python](https://www.python.org/downloads/)

## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Change directory
    ```sh
   cd some-folder
   ```
3. Install required libraries
   ```sh
   pip install -r requirements.txt
   ```
4. Install OpenAPI-to-GraphQL
   ```sh
   npm install -g openapi-to-graphql-cli@2.5.0
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

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributor

- Nuttapol Korcharoenrat 6210546404 nuttapol.kor@ku.th
- Pitchapa 	Sae-lim 6210546421 pitchapa.sae@ku.th
- Phinyaphak Chiradejthanankorn 6210545572 phinyaphak.c@ku.th

<p align="right">(<a href="#top">back to top</a>)</p>
