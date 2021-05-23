# Zadanie 1:
print("Lista Zakupów")
shopping_dikt = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

shopping_count = 0
for sklep in shopping_dikt:
    store_line = f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: "
    for artikle in shopping_dikt[sklep]:
        store_line += f"{artikle.capitalize()}, "
    store_line = store_line[:-2]+"."
    print(store_line)
    shopping_count += len(shopping_dikt[sklep])
print(f"W sumie kupuję {shopping_count} produktów.")

# Zmiana z na repozytorium zdalnym:
print("Edytowano w githubie...")
