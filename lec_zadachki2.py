a = int(input("Введите первый член прогрессии:"))
q = int(input("Введите знаменатель:"))
n = int(input("Ведите количество членов прогрессии:"))
if q == 0:
    print("ОШИБА 0_0")
else:
    for i in range(n):
        print(a)
        a *= q
     
    