from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def countdown_to_saturday():
    today = datetime.now()
    # Визначаємо кількість днів до суботи (5 - субота в Python)
    days_until_saturday = (5 - today.weekday() + 7) % 7 or 7
    return f"<h1>Днів до наступної суботи: {days_until_saturday}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
