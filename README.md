
# **Telegram monitoring bot**

### *For the test task at Ohara Media.*


## 🚀 Features

**1. Telethon:** *High-performance, easy-to-use library for interacting with the Telegram API*

**2. Docker Deployment:** *Easy deployments with Docker.*

## 📦 Setup with Docker
![](https://1000logos.net/wp-content/uploads/2021/11/Docker-Logo-2013.png)

**1. Clone the repository.**

```
git clone https://github.com/vurrau/telegram_monitoring
```

**2. Open the directory.**

```
cd telegram_monitoring
```

**3. Build and start docker containers.**

```
docker-compose up --build
```


## 🖥 Setup manualy



**1. Open the app directory and setup virtual environment.**

```
cd app
python -m venv venv
```

**2. Activate the virtual enviroment and install all modules.**

```
source venv/bin/activate
pip install -r requirements.txt
```

**3. Run application.**

```
python main.py
```
## ⚙️ Settings

* You can set-up your own settings in dot env files.
* The project uses PostgreSQL as default database.
* You can read the docs for the Telethon here: https://docs.telethon.dev/

```

TELEGRAM_TOKEN (str): Telegram bot token.
API_ID (int): API ID for the Telegram API.
API_HASH (str): API hash for the Telegram API.
DB_HOST (str): Host of the database.
DB_PORT (int): Port of the database.
DB_NAME (str): Name of the database.
DB_PASS (int): Password for the database.
DB_USER (str): Username for the database.




