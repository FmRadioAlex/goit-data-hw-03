from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")  # замінити на ваш MongoDB URI
db = client['cat_database']
collection = db['cats']

# Create (створення) запису
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return collection.insert_one(cat).inserted_id

# Read (читання) всіх записів
def read_all_cats():
    return list(collection.find())

# Read (читання) одного запису за ім'ям
def read_cat_by_name(name):
    return collection.find_one({"name": name})

# Update (оновлення) віку за ім'ям
def update_cat_age(name, new_age):
    return collection.update_one({"name": name}, {"set": {"age": new_age}})

# Update (оновлення) характеристик за ім'ям
def add_cat_feature(name, new_feature):
    return collection.update_one({"name": name}, {"$push": {"features": new_feature}})

# Delete (видалення) запису за ім'ям
def delete_cat_by_name(name):
    return collection.delete_one({"name": name})

# Delete (видалення) всіх записів
def delete_all_cats():
    return collection.delete_many({})

# Тестування функцій
if __name__ == "__main__":
    # Створення запису
    cat_id = create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    print(f"Створено кота з ID: {cat_id}")

    # Читання всіх записів
    print("Всі коти в базі:")
    for cat in read_all_cats():
        print(cat)

    # Читання кота за ім'ям
    print("Інформація про кота 'barsik':")
    print(read_cat_by_name("barsik"))

    # Оновлення віку кота
    update_cat_age("barsik", 4)
    print("Оновлений вік кота 'barsik':")
    print(read_cat_by_name("barsik"))

    # Додавання нової характеристики
    add_cat_feature("barsik", "любить рибу")
    print("Оновлені характеристики кота 'barsik':")
    print(read_cat_by_name("barsik"))

    # Видалення кота за ім'ям
    delete_cat_by_name("barsik")
    print("Кіт 'barsik' видалений")

    # Видалення всіх котів
    delete_all_cats()
    print("Всі коти видалені")
