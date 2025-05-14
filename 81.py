
original_countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Япония": "Токио",
    "Германия": "Берлин",
    "Италия": "Рим"
}


countries = {country.lower(): capital for country, capital in original_countries.items()}


print("Список стран и столиц:")
for country, capital in original_countries.items(): # items возвращает все пары ключ - значения
    print(f"{country} — {capital}")


country_name = input("\nВведите название страны: ").lower()
capital = countries.get(country_name) # get возвращает значение по ключу
if capital:

    for original in original_countries:
        if original.lower() == country_name:
            print(f"Столица страны {original}: {capital}")
            break
else:
    print("Страна не найдена в словаре.")


print("\nСортировка по названиям стран:")
for country in sorted(original_countries):
    print(f"{country}-{original_countries[country]}")
