def shennons_method(arr):
    half_index = 0
    last_index = 0
    while len(arr[last_index:]) > 1:
        half_sum = sum([i[1] for i in arr[last_index:]]) // 2
        temp_sum = 0
        for i in range(len(arr[last_index:])):
            temp_sum += arr[last_index + i][1]
            if temp_sum >= half_sum:
                half_index = last_index + i + 1
                break

        len_first_part = len(arr[last_index:half_index])

        if len_first_part == 1:
            arr[half_index-1][2] += "1"
            for i in arr[half_index:]:
                i[2] += "0"
        elif len_first_part > 1:
            for j in arr[last_index:half_index]:
                j[2] += "1"
            for k in arr[half_index:]:
                k[2] += "0"
            shennons_method(arr[last_index:half_index])

        last_index = half_index
    return arr

def array_creator(s):
    letters_arr = list(set([i for i in s.lower()]))
    letters_in_s_arr = [s.lower().count(i) for i in letters_arr]
    letters_dict = {i: j for i, j in sorted(zip(letters_arr, letters_in_s_arr), key=lambda item: item[1])}
    arr = list(reversed([[i, j, ""] for i, j in letters_dict.items()]))
    return arr

def efficiency_counter(result_arr, len_s):
    if len_s > 0:
        efficiency = 0.0
        for i in result_arr:
            efficiency += len(i[2]) * (i[1] / len_s)
        return round(efficiency, 2)
    else:
        return 0.0

def result_converter(s, result_arr, efficiency):
    s = (f'Строка: \"{s}\"\n'
         f'Закодированная методом Шеннона-Фано имеет эффективность = {efficiency}\n'
         f'А закодированные элементы имеют следующий вид:\n')
    for i in result_arr:
        s += f'\"{i[0]}\" - {i[2]}\n'
    return s

def converter(s):
    if len(s) > 1:
        arr = array_creator(s)
        result_arr = shennons_method(arr)
    elif len(s) == 1:
        result_arr = [[s, 1, "1"]]
    else:
        result_arr = [["", 0, "\"\""]]
    efficiency = efficiency_counter(result_arr, len(s))
    result = result_converter(s, result_arr, efficiency)
    return result

if __name__ == "__main__":
    print(converter(str(input("Введите строку, которую хотите закодировать: "))))