doubles = [x * 2 for x in range(1, 11) ]
print(doubles)
Triples = [x * 3 for x in range(1, 11) ]
print(Triples)
squared = [x * x for x in range(1, 11) ]
print(squared)

fruits = ['apple', 'orange', 'banana', 'coconut']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruits = ['apple', 'orange', 'banana', 'coconut']
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)

numbers = [1,-2,3,-4,5,-6, 8,-7,-9,10,11]
positive_nums = [number for number in numbers if number >= 0]
negative_nums = [number for number in numbers if number < 0]
even_nums = [number for number in numbers if number % 2 == 0]
odd_nums = [number for number in numbers if number % 2 != 0]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [89,79,56,34,76,89,76,87,65,53,61]
passed_grades = [num for num in grades if num >= 60]
print(passed_grades)