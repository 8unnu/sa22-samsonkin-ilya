from math import log2

def task1(m, n):
    return f"Изображение займёт - {m * n * 1} бит" # * 1 т.к цвета 2, а они помещаются в 1 бит

def task2(init_quan_color, final_quan_color):
    return f"Объём увеличился в {int(log2(final_quan_color) / log2(init_quan_color))} раз"

def task3(m, n, kbytes):
    return f"Можно использовать {2 ** int((kbytes * 1024) / (m * n) * 8)} различных цветов"

def task4(quan_colors, bytes):
    return f"Рисунок состоит из {int(bytes / (log2(quan_colors) / 8))} точек"

def task5(mins, kHz, bit_depth):
    return f"Объём памяти для хранения цифрового аудиофайла {round(((mins * 60) * (kHz * 1000) * (bit_depth / 8)) / 1024, 2)} Кбайт"

def task6(mins, mbytes, bit_depth):
    return f"Звук записан с частотой {round((mbytes * 1024 * 1024) / (bit_depth / 8) / (mins * 60), 2)} Гц"

def task7(gbytes, bit_depth, hz):
    return f"Длительность звучания цифрового аудио файла {round(((gbytes * 1024 * 1024 * 1024) / (bit_depth / 8) / hz) / 60, 2)} минуты"

def task8(bit_depth, kHz, kbytes):
    return f"Время звучания монофайла составляет {round((kbytes * 1024 * 8) / (kHz * 1000) / bit_depth, 2)} секунд"

def task9(mins, bit_depth, kHz):
    return f"Информационный объём моноаудиофайла равен {round((mins * 60) * (bit_depth * (kHz * 1000)) / 8 / 1024, 2)} Кбайт"

if __name__ == "__main__":
    # Если в задачах необходимы числа с запятой, то нужно ввести их в виде float числа по типу 44.1,
    # также результаты задач были округлены до целой части с помошью int() и round() до 2 знаков после точки
    # __________________________________________________________________________________________________________________
    # Представление графической информции
    # №1
    # print(task1(10, 10))
    # №2
    # print(task2(16, 256))
    # №3
    # print(task3(64, 32, 1))
    # №4
    # print(task4(256, 120))
    # __________________________________________________________________________________________________________________
    # Представление звуковой информации
    # №1
    # print(task5(2, 44.1, 16))
    # # №2
    # print(task6(1, 1.3, 8))
    # # №3
    # print(task7(0.01, 16, 44100))
    # №4
    # print(task8(16, 32, 700))
    # №5
    # print(task9(1, 16, 8))
    pass