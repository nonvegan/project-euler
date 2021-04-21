digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
dozens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def sum_len_list_words(list_words):
    return sum(list(map(len, list_words)))


first_99_card_nums = digits + tens + dozens + list(dozen + digit for dozen in dozens for digit in digits)  # unordered

sum_len_one_to_one_thousand = 0
sum_len_one_to_one_thousand += sum_len_list_words(first_99_card_nums)  # First 99 numbers
sum_len_one_to_one_thousand += 100 * (sum_len_list_words(digits) + len("hundred") * 9)  # <digit> hundreds
sum_len_one_to_one_thousand += 9 * (99 * len("and") + sum_len_list_words(first_99_card_nums))  # and <99 numbers>
sum_len_one_to_one_thousand += len("onethousand")  # One Thousand

print(sum_len_one_to_one_thousand)
