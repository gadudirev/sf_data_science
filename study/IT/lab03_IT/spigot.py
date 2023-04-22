
def spigot(number_of_decimal:int = 3, counter_of_operation:int = 0) -> int:
    """Функция реализовывает работу алгоритма Spigot,
       который служит для вычисления числа Пи.

    Args:
        number_of_decimal (int, optional): Количество знаков числа Пи. Defaults to 1.
        counter_of_operation (int, optional): Счетчик элементарных операций. Defaults to 0.

    Returns:
        int: Возвращает значений числа Пи
    """
    digits_of_pi = [] #Создаем список значений числа Пи, которые мы будем получать

    """
    Создаем список, с которым будет работать алгоритм Spigot
    Далее по формуле получаем длину этого списка и заполняем его двойками
    """

    list_of_number = []                             
    len_of_list = (number_of_decimal * 10) // 3 
    for i in range(len_of_list):
        list_of_number.append(2)                    

    k = 100
    counter_of_operation = counter_of_operation + 2 #Увеличиваем счетчик операций

    transfer = 0 #Задаем переменную, в которую будем помещать значение переноса

    invalid_number_counter = 0 #Задаем переменную, которая будет считать недействительные числа

    for i in range(number_of_decimal):
    #Наружный цикл ищет все заданные значениям числа Пи
        for numerator in range(len_of_list - 1, -1, -1):
        #Внутренний цикл реализует работу алгоритма Spigot по поиску значения числа Пи
            if numerator == 0: 
                sum = (list_of_number[numerator] * 10) + transfer
                list_of_number[numerator] = sum % 10
                digit_of_pi = sum // 10
                counter_of_operation = counter_of_operation + 4

                if digit_of_pi < 9: invalid_number_counter = 1

                if digit_of_pi == 9:
                    invalid_number_counter += 1
                    counter_of_operation += 1

                if digit_of_pi == 10:
                    digit_of_pi = 0
                    len_of_digits = len(digits_of_pi)
                    for j in range(len_of_digits - invalid_number_counter, len_of_digits):
                        digits_of_pi[j] += 1

                        counter_of_operation += 1

                digits_of_pi.append(digit_of_pi)

                if number_of_decimal > k and i == k - 1:
                    print(f"The number of operation to calculate {k} digits, when calculating {number_of_decimal}: {counter_of_operation}.")
                    k *= 10


                transfer = 0
            else:
                denominator = numerator * 2 + 1
                sum = (list_of_number[numerator] * 10) + transfer
                list_of_number[numerator] = int(sum % denominator) 
                transfer = (sum // denominator) * numerator

                counter_of_operation = counter_of_operation + 7

    print(f"Number of digits of PI:{number_of_decimal}\nCount of operation: {counter_of_operation}")

    return digits_of_pi


def pi(number_of_decimal:int = 3) -> str:
    """Переделывыет список значений числа Пи,
       который мы получаем с помощью алгоритма Spigot,
       в одну строку числа Пи

    Args:
        number_of_decimal (int, optional): Количество знаков числа Пи. Defaults to 3.

    Returns:
        str: Число Пи
    """
    pi = ""
    digits_of_pi = spigot(number_of_decimal)

    for i in list(range(number_of_decimal)):
        if i == 1:
            pi = pi + '.' + str(digits_of_pi[i])
        else:
            pi = pi + str(digits_of_pi[i])

    return pi


def tests_of_pi(list_of_tests = [100, 1000, 10000]):
    for test in list_of_tests:
        PI = pi(test)
        print(PI, "\n")


tests_of_pi()

print("Test for digits from 1 to 15")
tests_of_pi(list(range(1, 16)))



