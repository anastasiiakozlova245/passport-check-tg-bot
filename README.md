# Passport status bot

This telegram bot checks the status of the passport application on the info.midpass.ru website.

### Prerequisites:
Set the following env variables:
- BOT_TOKEN - the token of a custom telegram bot
- APPLICATION_ID - application ID
- EMBASSY_ID - ID of the embassy where the application was submitted

### Start the bot
1. Build a Docker image
docker build --tag passport-tg-bot:0.1.0 .

2. Run a Docker container passing the env variables
docker run -d --env BOT_TOKEN --env EMBASSY_ID --env APPLICATION_ID passport-tg-bot:0.1.0
