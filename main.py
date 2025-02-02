a = int(input("a:"))
b = int(input("b:"))
c = float(input("c:"))
d = float(input("d:"))

sum_result = a + b
sub = a - b
mult = a * b
div = a / b
ed = c ** d
id = c // d
rd = c % d

results_list = [sum_result, sub, mult, div, ed, id, rd]
print(results_list)
print(len(results_list))

for x in results_list:
    if x % 2 == 0 and x != 0:
        print(x)

results_list[1],results_list[4] = results_list[4],results_list[1]
print(results_list)

name = str(input("Ім'я та прізвище: "))
print(name, "виконала лабораторну роботу №1\nЗасвоїла основні правила роботи з Pathon\nОзнайомилась з алгоритмами послідовної (лінійної) структури, з процедурами запуску програм, які реалізують ці алгоритми.")
