#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.

A = int(input("Координата точки A: "))
B = int(input("Координата точки B: "))
C = int(input("Координата точки C: "))

length_AC = abs(A - C)
length_BC = abs(B - C)

sum_of_length = length_AC + length_BC

print("Длина отрезка AC = ", length_AC)
print("Длина отрезка BC = ", length_BC)
print ("Сумма длин отрезков AC и BC = ", sum_of_length)
