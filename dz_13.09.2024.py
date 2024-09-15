def num_spliting(num, part):
    num_arr = str(num).split(",")
    return str(num_arr[part])

def is_sixty_num(num, num_base):
    if num_base == 10:
        num = int(num)
        if num == 10:
            return "A"
        elif num == 11:
            return "B"
        elif num == 12:
            return "C"
        elif num == 13:
            return "D"
        elif num == 14:
            return "E"
        elif num == 15:
            return "F"
        else:
            return str(num)
    else:
        if num == "A":
            return 10
        elif num == "B":
            return 11
        elif num == "C":
            return 12
        elif num == "D":
            return 13
        elif num == "E":
            return 14
        elif num == "F":
            return 15
        else:
            return int(num)

def wrap_nulls(num):
    result = ""
    nulls_arr = []
    ones_arr = []
    for i in range(len(num)):
        if num[i] == "0":
            nulls_arr.append(i)
        elif num[i] == "1":
            ones_arr.append(i)
    for j in range(len(num)):
        if j in nulls_arr:
            result += "1"
        elif j in ones_arr:
            result += "0"
    return result

def adding_twoss(num1, num2):
    sum = int(str(num1), 2) + int(str(num2), 2)
    result = bin(sum)[2:]
    return str(result)

def subtraction_twoss(num1, num2):
    sum = int(str(num1), 2) - int(str(num2), 2)
    result = bin(sum)[2:]
    return str(result)

def from_tenss_in_base_intpart(int_part, base, base2, minus = 0):
    int_part = int(int_part)
    result = ""
    while int_part >= base:
        # print(is_sixty_num(int_part % base, base2))
        result = is_sixty_num(int_part % base, base2) + result
        int_part //= base
    else:
        result = is_sixty_num(int_part, base2) + result
    if minus == 0:
        return result
    elif minus == 1 and base == 2:
        result = wrap_nulls(result)
        result = adding_twoss(int(result), "1")
        return result
    elif minus == 1 and base == 16:
        return f"-{result}"

def from_tenss_in_base_fractpart(fract_part, base, base2):
    result = ""
    compose = fract_part
    while int(compose[-len(fract_part):]) >= base and len(result) < 10:
        compose = str(int(compose[-len(fract_part):]) * base)
        if len(compose) > len(fract_part):
            # print(compose[:-len(fract_part)])
            result += is_sixty_num(int(compose[:-len(fract_part)]), base2)
        else:
            result += "0"
    else:
        if result == "":
            result += is_sixty_num(compose[-len(fract_part):], base2)
    return result

def from_base_in_tenss_intpart(int_part, base2, minus = 0):
    index = len(int_part) - 1
    result = 0
    for i in int_part:
        result += is_sixty_num(i, base2) * (base2 ** index)
        index -= 1

    if minus == 0:
        return result
    elif minus == 1 and base2 == 10:
        result = wrap_nulls(str(result))
        result = adding_twoss(int(result), "1")
        return result
    elif minus == 1 and base2 == 16:
        return f"-{result}"
    elif minus == 1 and base2 == 2:
        result = subtraction_twoss(int(result), "1")
        result = wrap_nulls(str(result))
        index = len(int_part) - 1
        for i in int_part:
            result += is_sixty_num(i, base2) * (base2 ** index)
            index -= 1
        return result

def from_base_in_tenss_fractpart(fract_part, base2):
    index = 1
    result = 0
    for i in fract_part:
        if index <= len(fract_part):
            result += is_sixty_num(str(i), base2) * (base2 ** -index)
            index += 1
    return str(result)[2:]

# №1 и №2
def from_tenss_to_internal_intpart(num, minus = 0):
    num = num.zfill(16)
    if minus == 0:
        return num
    elif minus == 1:
        num = wrap_nulls(num)
        num = adding_twoss(int(num), "1")
        return num

def from_sixtyss_or_iternal_to_base_intpart(num, base, minus = 0):

    sixty_two_ss_dict = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    result = ""
    if base == 16:
        temp_result = ""
        for i in [num[i:i + 4] for i in range(0, len(num), 4)]:
            temp_result += sixty_two_ss_dict[i]
        for j in range(len(temp_result)):
            if temp_result[j] != "0":
                result = temp_result[j:]
                break
        if result:
            if minus == 0:
                return result
            else:
                result = wrap_nulls(result)
                result = adding_twoss(int(result), "1")
                return result
        else:
            return "0"
    elif base == 2:
        for i in num:
            result += sixty_two_ss_dict[i]
        result = result.zfill(16)
        if minus == 1:
            result = wrap_nulls(result)
            result = adding_twoss(int(result), "1")
        return result

def negative_wrap_intfractpart(num, minus = 0):
    index = 0
    for i in range(len(num)):
        if num[i] == ",":
            index = i
            break

    quan_nuls = from_tenss_in_base_intpart(len(num[:index]), 2, 10)
    result = num[:index] + num[index + 1:]
    result = "1" + str(str(1000000 + int(quan_nuls)) + result)
    result = result + "0" * (32 - len(result))

    return result

def converter(num, base, base2, mode = 1):
    if mode == 1:
        znak = ""
        if "-" in str(num):
            znak = "-"
            num = str(num[1:])
        int_part = num_spliting(num, 0)
        if base2 == 10:
            if "," in str(num):
                fract_part = num_spliting(num, 1)
                return f"{znak}{from_tenss_in_base_intpart(int_part, base, base2)},{from_tenss_in_base_fractpart(str(fract_part), base, base2)}"
            return f"{znak}{from_tenss_in_base_intpart(int_part, base, base2)}"
        elif base2 == 2 or base2 == 8 or base2 == 16:
            if "," in str(num):
                fract_part = num_spliting(num, 1)
                return f"{znak}{from_base_in_tenss_intpart(str(int_part), base2)},{from_base_in_tenss_fractpart(str(fract_part), base2)}"
            return f"{znak}{from_base_in_tenss_intpart(str(int_part), base2)}"
    elif mode == 2:
        if num[0] != "-":
            minus = 0
            int_part = num_spliting(num, 0)
        else:
            minus = 1
            int_part = num_spliting(num[1:], 0)

        if base2 == 10 and base == 2:
            if ',' in str(num):
                fract_part = num_spliting(num, 1)
                return negative_wrap_intfractpart(f"{from_tenss_in_base_intpart(int_part, base, base2, minus=0)},"
                                           f"{from_tenss_in_base_fractpart(fract_part, base, base2)}")
            return from_tenss_to_internal_intpart(from_tenss_in_base_intpart(int_part, base, base2), minus=minus)
        elif base2 == 10 and base == 16:
            if ',' in str(num):
                fract_part = num_spliting(num, 1)
                return f"{from_tenss_in_base_intpart(int_part, base, base2, minus=minus)},{from_tenss_in_base_fractpart(fract_part, base, base2)}"
            return from_tenss_in_base_intpart(int_part, base, base2, minus=minus)
        elif base2 == 16 and base == 2:
            if ',' in str(num):
                pass # из 16 сс в 2сс с ","
            return from_sixtyss_or_iternal_to_base_intpart(int_part, base, minus=minus)
        elif base2 == 16 and base == 10:
            if ',' in str(num):
                fract_part = num_spliting(num, 1)
                return f"{from_base_in_tenss_intpart(int_part, base2, minus=minus)},{from_base_in_tenss_fractpart(fract_part, base2)}"
            return from_base_in_tenss_intpart(int_part, base2, minus=minus)
        elif base2 == 2 and base == 16:
            if ',' in str(num):
                pass
            return from_sixtyss_or_iternal_to_base_intpart(int_part, base, minus=minus)
        elif base2 == 2 and base == 10:
            if int_part[0] == "1":
                minus = 1
            if ',' in str(num):
                fract_part = num_spliting(num, 1)
                return negative_wrap_intfractpart(f"{from_tenss_in_base_intpart(int_part, base, base2, minus=0)},"
                                           f"{from_tenss_in_base_fractpart(fract_part, base, base2)}")
            return from_base_in_tenss_intpart(int_part, base2, minus=minus)

if __name__ == "__main__":
    pass
    # Режим работы обозначаются переменной mode, если mode = 1, то он просто переводит числа из сс в другую сс,
    # если mode = 2, то он переводит из 10сс или 16сс во внутренние представление и обратно в 10сс или 16сс
    # в первом варианте работы его можно не задавать, т.к дефолт значение = 1

    # __________________________________________________________________________________________________________________
    # Перевод чисел из 10сс в любую и из любой в 10сс (base2 или base должна быть = 10)
    # num = str(input("Введите число: ")) # с "," обязательно если оно вещественное
    # base2 = int(input("В какой системе счисления находится число: "))
    # base = int(input("В какую систему счисления перевести число: "))
    # print(converter(num, base, base2))

    # Пример:
    # num = "55,2" # что
    # base2 = 8 # откуда
    # base = 10 # куда
    # print(converter(num, base, base2))
    # __________________________________________________________________________________________________________________

    # Эта часть работает криво, нормально сработает пока только из 10cc в 16сс и обратно
    # Что всё в этой части считало правильно, нужно указывать везде mode = 2
    # Внутренние представление это base = 2 или 2сс у меня тут записано
    # Перевод из любой сс в любую
    # Принимаются отрицательные/положительные/целые числа

    # Примеры:
    # num = "10001,12"  # что
    # base2 = 10 # откуда
    # base = 16 # куда
    # mode = 2 # режим работы
    # print(converter(num, base, base2, mode))

    # num = "-69,A"  # что
    # base2 = 16 # откуда
    # base = 2 # куда
    # mode = 2  # режим работы
    # print(converter(num, base, base2, mode))

    # num = "-258,125" # что
    # base2 = 10  # откуда
    # base = 2  # куда
    # mode = 2  # режим работы
    # print(converter(num, base, base2, mode))

    # num = "-A2"  # что
    # base2 = 16  # откуда
    # base = 2  # куда
    # mode = 2  # режим работы
    # print(converter(num, base, base2, mode))
