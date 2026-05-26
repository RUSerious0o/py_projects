from datetime import datetime

user_name = input("Введите имя атлета: ")
type = input("Введите сложность нагрузки (простая / сложная): ")
load_type = input("Введите тип нагрузки (статика / динамика): ")
exercise = input("Введите название упражнения: ")
result = input("Введите ваш результат: ")

date_string = datetime.now().strftime("%d.%m.%Y")
data_string = f"{date_string}, {user_name}, {load_type}, {type}, {exercise}, {result}\n"

with open("records.txt", "a", encoding="utf-8") as file:
    file.write(data_string)

print("\n[OK] Данные сохранены.")
