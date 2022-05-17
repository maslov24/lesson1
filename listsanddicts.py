def print_list(new_list):
    if len(str(new_list)) == 1:
        print(new_list)
    else:
        for i in range(len(new_list)):
            print(f'SUPER LIST: {type(new_list[i])} {new_list[i]}', end=' ')
        print()

#Создайте список из чисел 3, 5, 7, 9 и 10.5 Выведите содержимое списка на экран
new_list=[3, 5, 7, 9, 10.5]
print_list(new_list)

#Добавьте в конец списка строку "Python"  Выведите длину списка на экран
new_list.append('Python')
print_list(new_list)
#Выведите на экран начальный элемент списка
print_list(new_list[0])
#Выведите на экран последний элемент списка
print(new_list[-1])
#Напечатайте элементы списка со второго по четвертый включительно
print(new_list[1:4])
#Удалите из списка строку "Python"
del new_list[-1]
print_list(new_list)

#Создайте словарь: {"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
weather_forecast={"city": "Москва", "temperature": '20'}
print(weather_forecast["city"])
#Уменьшите значение "temperature" на 5
weather_forecast["temperature"]=int(weather_forecast["temperature"])-5
#Выведите на экран весь словарь
print(weather_forecast)

#Проверьте, есть ли в словаре ключ country
print(weather_forecast.get('country'))
#Выведите значение по-умолчанию "Россия" для ключа country
print(weather_forecast.get('country', 'Россия'))
#Добавьте в словарь элемент date со значением "27.05.2019"
weather_forecast["date"]="27.05.2019"
print(weather_forecast)
#Выведите на экран длину словаря
print(len(weather_forecast))