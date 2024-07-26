FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client cron

COPY . .

# Add cron job
COPY crontab /etc/cron.d/telethon-cron
# Make the cron file executable
RUN chmod 0644 /etc/cron.d/telethon-cron

# Create a log file for cron
RUN touch /var/log/cron.log

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
