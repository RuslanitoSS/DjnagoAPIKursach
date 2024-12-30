import random
from portfolio.models import Project, Event
from faker import Faker

# Создание экземпляра Faker для генерации случайных описаний
fake = Faker('ru_RU')

# Список направлений для проекта и мероприятия
options = [
    "Выберите направление", "1. Дизайн", "2. Мультимедиа", "3. Научные", 
    "4. Социальные технологии", "5. Стратегические", "6. Технология", 
    "7. Транспорт", "8. Урбанистика и городское хозяйство", 
    "9. ХимБиотех", "10. IT"
]

# Список адресов для мероприятий
addresses = [
    "г. Москва, ул. Автозаводская, д. 16", 
    "г. Москва, ул. Б. Семёновская, д. 38", 
    "г. Москва, ул. Павла Корчагина, д. 22"
]

# Создание 12 проектов
for i in range(12):
    project = Project(
        title=f"Проект {i+1}",
        field=random.choice(options),
        description=fake.text(max_nb_chars=200),  # Сгенерировать описание
    )
    project.save()

# Создание 12 мероприятий
for i in range(12):
    event = Event(
        title=f"Мероприятие {i+1}",
        field=random.choice(options),
        address=random.choice(addresses),
        description=fake.text(max_nb_chars=200),  # Сгенерировать описание
    )
    event.save()

print("12 проектов и мероприятий успешно созданы!")
