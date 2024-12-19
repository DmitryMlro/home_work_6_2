seconds = int(input("Введіть кількість секунд: "))
day, seconds = divmod(seconds, 24 * 60 * 60)
hours, seconds = divmod(seconds, 60 * 60)
minutes, seconds = divmod(seconds, 60)

if day % 10 == 1 and day % 100 != 11:
    day_word = "день"
elif 2 <= day % 10 <= 4 and (day % 100 < 10 or day % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"

time_formatted = f"{day} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(time_formatted)