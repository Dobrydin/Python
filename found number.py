import numpy as np
number = np.random.randint(1, 101)
print (f"Загадано число {number}. Не подсматривать!")
infimum=1
supremum=100
count=0
while True:
    count += 1
    predict_number = (infimum+supremum)//2

    if predict_number > number:
        print("Число должно быть меньше!")
        supremum=predict_number
    elif predict_number < number:
        print("Число должно быть больше!")
        infimum=predict_number
    else:
        print(f"Вы угадали число! Это число = {predict_number}, за {count} попыток")
        break # конец игры, выход из цикла
schet=0
for i in range(1,101):
    inf=1
    sup=101
    while True:
        schet+=1
        mut=(inf+sup)//2
        if mut > i:
            sup=mut
        elif mut < i:
            inf=mut
        else:
            break
M_COUNT=schet/100
print(f"Математическое ожидание количества попыток угадывания {M_COUNT}")