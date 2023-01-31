def str_set(string):
    if len(string) == 9 and "0" not in string:
        return len(set(string))
    else:
        return 0

pan_nums = []
for i in range(1,2000):
    for j in range(1,2000):
        k = i*j
        all_nums = str(i) + str(j) + str(k)
        if str_set(all_nums) == 9:
            pan_nums.append(k)

pan_num = list(set(pan_nums))

print(sum(pan_num))