

zero = 8 * 60 + 30
n = int(input())
breaks = n - 1
time_end = n * 45 + breaks * 10 + zero
time_start = time_end - 45

print(f'Время начала урока - {time_start // 60}:{time_start % 60}, Время конца - {time_end // 60}:{time_end % 60}')


