def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    elif n < 1000:
        return ones[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' and ' + number_to_words(n % 100))
    else:
        return 'one thousand'

total_letters = 0
for i in range(1, 1001):
    total_letters += len(number_to_words(i).replace(" ","").replace("-",""))

print(total_letters)
