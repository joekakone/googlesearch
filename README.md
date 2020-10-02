# Automation - Studely

## Clonage du code source
`git clone https://github.com/joekakone/googlesearch.git`

`cd automation`

## Mise en place de l'environnement virtuel
`virtualenv -p /usr/bin/python3 env`

`source env/bin/activate`

`pip install -r requirements.txt`

## Installation des dépendances de Selenium
**Geckodriver**

`wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz`

`tar -xf geckodriver-v0.26.0-linux64.tar.gz`

`sudo mv geckodriver /usr/local/bin/`

**PhantomJs**

`sudo apt install phantomjs`

### Chrome
`sudo apt-get update`

`sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4`

`sudo apt-get install default-jdk `

## ChromeDriver
`wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip`

`unzip chromedriver_linux64.zip`

`sudo mv chromedriver /usr/bin/chromedriver`

`sudo chown root:root /usr/bin/chromedriver`

`sudo chmod +x /usr/bin/chromedriver`


Suivre ces instructions: https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

## Lancer
`python google.py`
