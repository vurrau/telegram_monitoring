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

**3. Run FastAPI application.**

```
python main.py
```