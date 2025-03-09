import requests

# Подставьте ваш токен вместо 'YOUR_TOKEN_HERE'
TOKEN = '...'

# Задайте базовый URL для API Telegram
base_url = f"https://api.telegram.org/bot{TOKEN}/"

# Отправка сообщения
chat_id = '...'  # Уникальный идентификатор чата
text = 'Привет, iDONi! С праздником тебя. Тебя же никто не поздравляет! Бот будет тебя поздравлять.'
url = base_url + f"sendMessage?chat_id={chat_id}&text={text}"
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    print("Сообщение успешно отправлено!")
else:
    print("Ошибка при отправке сообщения.")

# код работает но ты это зубришь думаю или уже забыла, а iDONi