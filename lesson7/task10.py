# 10. Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
# użytkowników:
# Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
# który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
# wielkimi literami.

users = [
    {"name": "alice", "age": 30, "active": True},
    {"name": "bob", "age": 17, "active": True},
    {"name": "charlie", "age": 25, "active": False},
    {"name": "david", "age": 18, "active": True},
    {"name": "giovanni", "age": 15, "active": True}
]


filtered_users = [u["name"].capitalize() for u in users if u["age"] >= 18 and u["active"]]
print(filtered_users)

