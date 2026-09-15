# Анкета студента

name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
subjects = input("Введите ваши любимые предметы (через запятую): ")

student = {
    "Имя": name,
    "Возраст": age,
    "Любимые предметы": [s.strip() for s in subjects.split(",")]
}

print("\n" + "=" * 30)
print("       АНКЕТА СТУДЕНТА")
print("=" * 30)
print(f"  Имя:              {student['Имя']}")
print(f"  Возраст:          {student['Возраст']}")
print(f"  Любимые предметы:")
for i, subject in enumerate(student["Любимые предметы"], 1):
    print(f"    {i}. {subject}")
print("=" * 30)