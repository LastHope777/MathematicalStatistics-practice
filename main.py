import math
from statistics import mode
from statistics import median
import numpy as np
import scipy.stats as st
import random


# Первый номер 🌈
print("====================Первый номер====================\n")
first_number = [23, 25, 42, 34, 27, 19, 21, 34, 41]
sr = 0
for i in range (len(first_number)):
    sr += first_number[i]
sr = sr/len(first_number)+1
sr = 30.66667
print(sr)
alpha1=0.95
loc1 = np.mean(sr)
scale1 = st.sem(first_number)
interval_first = st.norm.interval(alpha1, loc1, scale1)
print("95% доверительный интервал для средней дневной выручки:", interval_first)

# Для дисперсии 🌴
disperser = np.var(first_number)
mean1 = np.mean(disperser)
loc1=mean1
scale1 = st.sem(first_number)
interval_first2 = st.norm.interval(alpha1, loc1, scale1)
print("95% доверительный интервал для дисперсии выручки:", interval_first2)

# Для СКО 🐠
SVO = np.std(first_number)
mean1 = np.mean(SVO)

loc1=mean1
scale1 = st.sem(first_number)
interval_first3 = st.norm.interval(alpha1, loc1, scale1)
print("95% доверительный интервал для СКО:", interval_first3)


# Второй номер 🌈
print("\n====================Второй номер====================\n")
arr_time = [19, 21, 23, 25, 27, 29]
arr_worker = [2, 8, 24, 50, 12, 4]
arr = []

sum_workers = 0

# Средняя производительность труда рабочих 🌵
for j in range(len(arr_worker)):
    sum_workers += arr_worker[j]
sred_proizv = 0
for i in range(len(arr_worker)):
    sred_proizv += arr_time[i] * arr_worker[i]
print('Средняя производительность труда рабочих: ', sred_proizv / sum_workers)

#for n in range(len(arr_worker) ):
#    for m in range(arr_worker[n]):
#        arr.append(arr_time[n])
arr = [-4633, -1619, -3274, -1029, -1147, 775, -171, -1990,-2795, 25991, -2220,-921,-1862,-600,-1785,-2158,-1422,13873,1068,-3387,-454,97,-551,-2019,2267,19643,-3096,-152,-1697,1700]
# Мода 🍒
moda = mode(arr)
print("Мода: ", moda)

# Медиана 🍀
mediana = median(arr)
print("Медиана: ", mediana)

# Размах вариации 🌳
raZmah1 = 0
raZmah1 = max(arr_time) - min(arr_time)
print("Размах вариации: ", raZmah1)

# Дисперсия 🌲
dispersia = np.var(arr)
print("Дисперсия: ", dispersia)

# Среднее квадратическое отклонение 🎄
mid_square = np.std(arr)
print("Среднее квадратическое отклонение: ", mid_square)

# Коэффициент вариации 🍄
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
print("Коэффициент вариации: ", cv(arr))



# Доверительный интервал 🌱

# Для среднего времени обработки одной детали 🌿
mean = np.mean((19+21+23+25+27+29)/6)
std_err = st.sem(arr)
loc=mean
alpha=0.99
scale=std_err
interval = st.norm.interval(alpha, loc, scale)
print("99% доверительный интервал для среднего времени обработки одной детали:", interval)

# Для дисперсии ☘️
mean = np.mean(dispersia)
std_err = st.sem(arr)
loc=mean
alpha=0.99
scale=std_err
interval = st.norm.interval(alpha, loc, scale)
print("99% доверительный интервал для дисперсии:", interval)

# Для СКО 🎍
mean = np.mean(mid_square)
std_err = st.sem(arr)
loc=mean
alpha=0.99
scale=std_err
interval = st.norm.interval(alpha, loc, scale)
print("99% доверительный интервал для СКО:", interval)


# Третий номер 🌈
print("\n====================Третий номер====================\n")
third_arr = [1.6, 1.9, 2.0, 2.1, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8, 2.8, 2.9, 2.9, 3.0, 3.1, 3.2, 3.2, 3.3, 3.4, 3.4, 3.4, 3.5, 3.5, 3.5, 3.5, 3.6, 3.7, 3.9]
sr = 0
for o in range (len(third_arr)):
    sr += third_arr[o]
sr = sr/len(third_arr)

# Для средней себестоимости 🍁
mean = np.mean(sr)
std_err = st.sem(third_arr)
loc=mean
alpha=0.93
scale=std_err
interval = st.norm.interval(alpha, loc, scale)
print("93% доверительный интервал для средней себестоимости:", interval)

# Для среднеквадратического отклонения ⚡️
mid_square3 = np.std(third_arr)
mean = np.mean(mid_square3)
std_err = st.sem(third_arr)
loc=mean
alpha=0.93
scale=std_err
interval = st.norm.interval(alpha, loc, scale)
print("93% доверительный интервал для среднеквадратического отклонения:", interval)


# Четвёртый номер 🌈
print("\n====================Четвёртый номер====================\n")
array_time = [round(random.uniform(4.0, 4.5), 1), round(random.uniform(4.5, 5.0), 1), round(random.uniform(5.0, 5.5), 1), round(random.uniform(5.5, 6.0), 1), round(random.uniform(6.0, 6.5), 1), round(random.uniform(6.5, 7.0), 1), round(random.uniform(7.0, 7.5), 1), round(random.uniform(7.5, 8.0), 1), round(random.uniform(8.0, 9.5), 1)]
array_worker = [4, 14, 55, 92, 160, 96, 66, 11, 2]
array = []
for nn in range(len(array_worker) - 1):
    for MMM in range(array_worker[nn]):
        array.append(array_time[nn])

# Среднее время, которое рабочий тратит на изготовление детали 🐳
sred_znach = 0
for nnn in range (len(array)):
    sred_znach += array[nnn]
sred_znach = sred_znach / len(array)

# Доверительный интервал для cреднего времени, которое рабочий тратит на изготовление детали 🎋
mean = np.mean(sred_znach)
std_err = st.sem(array)
loc=mean
alpha=0.999
scale=std_err
interval4 = st.norm.interval(alpha, loc, scale)
print("99.9% доверительный интервал для cреднего времени, которое рабочий тратит на изготовление детали:", interval4)


# Пятый номер 🌈
print("\n====================Пятый номер====================\n")

count_items = np.array([8, 42, 51, 37, 12])
average_meaning = np.array([12, 14, 16, 18, 20])


# Общее количество изделий 🍉
n = np.sum(count_items)
# Дисперсия n/n-1
# Средний процент влажности 🥑
average_procent = np.sum(count_items * average_meaning) / n

# Стандартное отклонение 🍅
standart_otklonenie = np.sqrt(np.sum(count_items * (average_meaning - average_procent) ** 2) / n)

print("Средний процент влажности:", average_procent)
print("Стандартное отклонение:", standart_otklonenie)

# а) Вероятность того, что средний процент влажности заключен в границах от 12.5 до 17.5 🍎
down_border = 12.5
top_border = 17.5
probability = (top_border - average_procent) / standart_otklonenie - (down_border - average_procent) / standart_otklonenie
print("Вероятность:", probability)

# б) Границы, в которых с вероятностью 0.95 будет заключен средний процент влажности изделий во всей партии 🍍
border_95 = np.percentile(count_items, [2.5, 97.5], interpolation='nearest')
print("Границы:", average_procent + border_95 * standart_otklonenie)



# Вторая практика 🌈
print("\n====================Вторая практика====================\n")
# Первый номер 🍅
print("\nПервый номер:")
empire_arr = [14, 18, 32, 70, 36, 20, 10]
teory_arr = [10, 24, 34, 80, 22, 18, 12]
IhateCarrots = [0] * 7
empire_sum = 0
teory_sum = 0
nabludaemoe = 0
s = 7 # Запомним, в будущем нам это пригодится
for i in range(len(empire_arr)):
    empire_sum += empire_arr[i]
for i in range(len(empire_arr)):
    teory_sum += empire_arr[i]
for i in range(len(empire_arr)):
    IhateCarrots[i] = ((empire_arr[i] - teory_arr[i])**2)/teory_arr[i]
    nabludaemoe += IhateCarrots[i]
if (teory_sum != empire_sum):
    print("Сумма частот различается и дальше нет смысла проводить исследование")
else:
    print("Сумма частот совпадает")
    Hi = 9.48773
    if (Hi < nabludaemoe):
        print("Хи критическое меньше наблюдаемого, следовательно, H0 отвергается и принимается H1")
    elif (Hi > nabludaemoe):
        print("Хи критическое больше наблюдаемого, следовательно, H1 отвергается и принимается H0")

# Второй номер 🍅
print("\n\nВторой номер:")
# Данные
X = np.array([7.8, 8.2, 9.1, 8.9, 8.6])
Y = np.array([6.6, 7.1, 6.3, 7, 6.2, 5.8])

# t-критерий Стьюдента для независимых выборок и соответсвующего p-значения
t_statistic, p_value = st.ttest_ind(X, Y)

# Определение уровня значимости
alpha = 0.05

# Проверка статистической значимости
if p_value < alpha:
    print("Отвергаем нулевую гипотезу. Станки не обладают одинаковой точностью.")
else:
    print("Принимаем нулевую гипотезу. Станки обладают одинаковой точностью.")

print("t-статистика:", t_statistic)
print("p-значение:", p_value)


# Третий номер 🍅
print("\n\nТретий номер:")
# Данные
x_mean = 4.85
y_mean = 5.07
Sx = 0.94
Sy = 1.02
n_x = 15
n_y = 12

# Расчет t-статистики и p-значения
t_statistic, p_value = st.ttest_ind_from_stats(x_mean, Sx, n_x, y_mean, Sy, n_y)

# Определение уровня значимости
alpha = 0.01

# Проверка статистической значимости
if p_value < alpha:
    print("Отвергаем нулевую гипотезу. Существует существенное различие средней себестоимости единицы продукции на предприятиях.")
else:
    print("Принимаем нулевую гипотезу. Различие средней себестоимости единицы продукции на предприятиях несущественно.")

print("t-статистика:", t_statistic)
print("p-значение:", p_value)




# Четвёртый номер 🍅
print("\n\nЧетвёртый номер:")
# Данные для первой группы
x_values = [34, 35, 37, 39]
n_x = [2, 3, 4, 1]

# Данные для второй группы
y_values = [32, 34, 36]
n_y = [2, 2, 8]

# Расчет среднего и стандартного отклонения для каждой группы
mean_x = sum([x * n for x, n in zip(x_values, n_x)]) / sum(n_x)
mean_y = sum([y * n for y, n in zip(y_values, n_y)]) / sum(n_y)

# Стандартное отклонение и среднее для каждой выборки
S_x = (sum([n * ((x - mean_x) ** 2) for x, n in zip(x_values, n_x)]) / (sum(n_x) - 1)) ** 0.5
S_y = (sum([n * ((y - mean_y) ** 2) for y, n in zip(y_values, n_y)]) / (sum(n_y) - 1)) ** 0.5

# Расчет t-статистики и p-значения
t_statistic, p_value = st.ttest_ind_from_stats(mean_x, S_x, sum(n_x), mean_y, S_y, sum(n_y))

# Определение уровня значимости
alpha = 0.05

# Проверка статистической значимости
if p_value < alpha:
    print("Отвергаем нулевую гипотезу. Существует существенное различие средних значений дебиторской задолженности в группах.")
else:
    print("Принимаем нулевую гипотезу. Различие средних значений дебиторской задолженности в группах несущественно.")

print("t-статистика:", t_statistic)
print("p-значение:", p_value)



# Пятый номер 🍅
print("\n\nПятый номер:")
# Данные для первой группы
x_values = [139, 137, 134, 134, 137, 137, 135, 137, 135, 135]
mean_x = sum(x_values) / len(x_values)

# Данные для второй группы
y_values = [136, 136, 132, 134, 136, 136, 134, 132, 136, 136, 136, 136]
mean_y = sum(y_values) / len(y_values)

# Расчет t-статистики и p-значения
t_statistic, p_value = st.ttest_ind(x_values, y_values)

# Определение уровня значимости
alpha = 0.05

# Проверка статистической значимости
if p_value < alpha:
    print("Отвергаем нулевую гипотезу. Существует существенное различие средних значений средней выручки в группах.")
else:
    print("Принимаем нулевую гипотезу. Различие средних значений средней выручки в группах несущественно.")

print("t-статистика:", t_statistic)
print("p-значение:", p_value)