# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.
#
# def read_num_names(file_nums, file_names):
#     with(
#             open(file_nums,"r",encoding="UTF-8") as f_num,
#             open(file_names, "r", encoding="UTF-8") as f_names,
#             open("result_multi.txt","w",encoding="UTF-8") as result
#     ):
        # bigger,smaller = f_num,f_names  if len(f_num.readlines()) > len(f_names.readlines())  else f_names,f_num
        # f_num.seek(0)
        # f_names.seek(0)
        # both_end = False
        # while True:
        #     for num_pair in f_num:
        #         num_pair = num_pair.split("|")
        #         int_num = int(num_pair[0])
        #         float_num = float(num_pair[1])
        #         if current_name := f_names.readline():
        #
        #         else:
        #             f_names.seek(0)
        #             current_name =f_names.readline()
        #         if (int_num*float_num > 0):
        #         result.write('')




