#1
name = input("Введите имя: ")

name = name.strip()        # удаляем пробелы по краям
if name.isalnum():         # проверяем, что только буквы и цифры
    name = name.lower()    # приводим к нижнему регистру
    print("Имя корректно")
else:
    print("Ошибка")
#2
password = input("Введите пароль: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password):
    print("Пароль надёжен")
else:
    print("Пароль слаб")
#3
log = "ACCESS DENIED"
message = log.capitalize() + " – вход запрещён"
print(message)
#4
data = "ERROR connection ERROR failed access"
filtered = data.replace("ERROR", "ALERT")
count_alerts = filtered.count("ALERT")
print(filtered)
print("Количество предупреждений:", count_alerts)
#5
email = input("Введите email: ")

if "@" in email:
    parts = email.split("@")
    if len(parts) == 2 and parts[1].endswith(".com"):
        print("Домен:", parts[1])
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")
#6
text = input("Введите текст: ")
normalized = text.strip().lower().replace(" ", "_")
print(normalized)
#7
message = input("Введите сообщение: ")

if message.find("SECRET") != -1:
    message = message.replace("SECRET", "******")
    print(message)
    print("⚠️ Предупреждение: обнаружена конфиденциальная информация!")
else:
    print("Сообщение безопасно.")
#8
word = input("Введите слово: ")

codes = ""     # строка для кодов символов
for ch in word:
    codes += str(ord(ch)) + " "   # преобразуем символ в код

print("Коды символов:", codes)

# Восстанавливаем слово обратно
decoded = ""
for code in codes.split():
    decoded += chr(int(code))

print("Расшифровка:", decoded)
#9
text = "login attempt failed access denied unauthorized access"

failed_count = text.count("failed")
denied_count = text.count("denied")

if failed_count > 0 or denied_count > 0:
    print("Попытка несанкционированного доступа!")
else:
    print("Система в норме.")
#10
report = input("Введите текст отчёта: ")
1. Количество предложений
sentences = len(report.split('.'))

2. Количество символов без пробелов
chars = len(report.replace(" ", ""))

3. Проверка начала на "Report"
starts = report.lower().startswith("report")

4. Проверка ошибок
errors = report.lower().count("error")

print("Предложений:", sentences)
print("Символов (без пробелов):", chars)

if starts:
    print("Текст начинается со слова 'Report'")
else:
    print("Текст не начинается со слова 'Report'")

if errors >= 2:
    print("Ошибки найдены")
else:
    print("Ошибок не обнаружено")
     