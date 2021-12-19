# Дано n є N. Побудівати алгоритм для того,чи утворюють цифри арифметичну прогресію

def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
            return False
    return True
print(is_arithmetic([5,7,9,11]))
print(is_arithmetic([1,5,3,8]))
print(is_arithmetic([1487,1847,4817,4871,7481,7841,8147,8741]))

