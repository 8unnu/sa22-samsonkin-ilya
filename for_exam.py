def func2(decimal_number):
    if ',' in decimal_number:
        integer_part, fractional_part = decimal_number.split(',')
    else:
        integer_part = decimal_number
        fractional_part = '0'

    integer_part = int(integer_part)
    binary_integer_part = ''

    if integer_part == 0:
        binary_integer_part = '0'
    else:
        while integer_part > 0:
            binary_integer_part = str(integer_part % 2) + binary_integer_part
            integer_part //= 2

    fractional_part = float('0.' + fractional_part)
    binary_fractional_part = ''

    while fractional_part > 0:
        fractional_part *= 2
        if fractional_part >= 1:
            binary_fractional_part += '1'
            fractional_part -= 1
        else:
            binary_fractional_part += '0'

        if len(binary_fractional_part) > 10:
            break

    if binary_fractional_part:
        return binary_integer_part + ',' + binary_fractional_part
    else:
        return binary_integer_part

def func(byt, num):
    if "-" not in num:
        znak = 0
    else:
        znak = 1
        num = num[1:]

    num = func2(num)
    total_len = byt * 8

    num = num.replace(",", ".")
    mil_len = str(len(str(int(float(num)))))
    num = num.replace(".", "")
    print(mil_len)
    mil_len_for_twoss = func2(mil_len)
    print(mil_len_for_twoss)
    mantissa = str(1000000 + int(mil_len_for_twoss))

    alf = {
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
        "1111": "F",
    }

    internal_perf_temp = f"{znak}{mantissa}{num}"
    internal_perf = internal_perf_temp + ("0" * (total_len - len(internal_perf_temp)))
    print(f"Внутренние представление: {internal_perf}")
    for_16ss_arr = [internal_perf[i:i+4] for i in range(0, len(internal_perf), 4)]
    print(f"\nМассив: {for_16ss_arr}")
    result_16ss = "".join([alf[i] for i in for_16ss_arr])
    print(f"В 16сс: {result_16ss}")

if __name__ == "__main__":
    byt = 4
    num = "-168,375"
    func(byt, num)

