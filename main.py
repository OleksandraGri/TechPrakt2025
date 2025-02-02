a = int(input("a:"))
b = int(input("b:"))
c = float(input("c:"))
d = float(input("d:"))

sum = a + b
sub = a - b
mult = a * b
div = a / b
ed = c ** d
id = c // d
rd = c % d

list = [sum, sub, mult, div, ed, id, rd]
print(list)
print(len(list))

for x in results_list:
    if x % 2 == 0 and x != 0:
        print(x)

list[1],list[4] = list[4],list[1]
print(list)

name = str(input("Ім'я та прізвище: "))
print(name, "виконала лабораторну роботу №1\nЗасвоїла основні правила роботи з Pathon\nОзнайомилась з алгоритмами послідовної (лінійної) структури, з процедурами запуску програм, які реалізують ці алгоритми.")
