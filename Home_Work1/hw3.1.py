def get_length(length):
    return len(length)


print(get_length("Hello World"))


def plus_length(second_length, first_length):
    return second_length + first_length


print(plus_length("Hello World", "Hello World"))


def quadrat(number):
    return number**2


print(quadrat(5))


def summa(num1, num2):
    return num1 + num2


print(summa(3, 4))


def division(num1, num2):
    return (num1 // num2), (num1 % num2)


print(division(17, 5))


def mid(numbers):
    return sum(numbers) / len(numbers)


print(mid([1, 2, 3, 4, 5, 6]))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
new_list = []
for number2 in list2:
    if number2 in list1:
        new_list.append(number2)
print(new_list)


def list_gw(person):
    for key in person:
        print(key)


person = {"name": "Illia", "age": 21, "city": "Stuttgart"}
list_gw(person)


def summa_dict(dict1, dict2):
    new_dict = {}
    for key, value in dict1.items():
        new_dict[key] = value
    for key, value in dict2.items():
        new_dict[key] = value
    return new_dict


dict1 = {"name": "Illia", "age": 21, "city": "Stuttgart"}
dict2 = {"study": "Python", "training": "Muai-Thai", "favorite game": "Dota 2"}
print(summa_dict(dict1, dict2))


def marge_sets(set1, set2):
    return set1 | set2


set1 = {
    1,
    2,
    3,
    4,
    5,
}
set2 = {5, 6, 7, 8, 9}
print(marge_sets(set1, set2))


def subset(set1, set2):
    return set1.issubset(set2)


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(subset(set1, set2))


def even_number(number):
    if number % 2 == 0:
        print("Парне")
    else:
        print("Не парне")


even_number(5)


def even_list(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


print(even_list([1, 2, 3, 4, 5, 6]))
check_number = lambda x: "парне" if x % 2 == 0 else "не парне"
print(check_number(5))
print(check_number(6))
