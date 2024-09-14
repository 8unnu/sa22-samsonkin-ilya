def ascii_conv(s):
    s = s.encode('cp1251')
    ss2_arr = []
    ss16_arr = []
    for i in s:
        ss2_arr.append(str(bin(i))[2:])
        ss16_arr.append(str(hex(i)[2:].upper()))
    return f"Двоичное представление:\n{" ".join(ss2_arr)}\n\nШестнадцатеричное представление:\n{" ".join(ss16_arr)}"


if __name__ == "__main__":
    print(ascii_conv("Мы не помогаем людям, когда делаем за них работу, которую они в состоянии сделать сами."))