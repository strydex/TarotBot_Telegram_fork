# Tarot Bot

A Telegram bot for receiving tarot card layouts, written using aiogram3.

## Installation

### Prerequisites

- Python 3.6 or higher
- Aiogram
- OpenPyxl
- A VPS server with a public IP address

### Steps

1. Clone the repository to your VPS server:
```
git clone https://github.com/yourusername/tarot-bot.git
```

2. Create a new Python virtual environment and activate it:
```
cd TarotBot_Telegram_fork
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```
pip3 install aiogram
pip3 install openpyxl
```

4. Create a `config.py` file in the project directory and add the following variables:

- `BOT_TOKEN`: your Telegram bot token, which you can obtain from the Telegram bot @BotFather
- `PAYMENTS_TOKEN`: your Telegram payments token, which you can obtain from the Telegram bot @BotFather
- `CHANNELS`: a list of your Telegram channels that users must subscribe to in order to use the bot

5. Start the bot:
```
python3 main.py
```

## Usage

To use the bot, users must first subscribe to the channels listed in the `config.py` file. Once they have subscribed, they can interact with the bot to receive tarot card layouts.

At the moment, each new user is given a balance of 100,000 rubles to test all functions.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
