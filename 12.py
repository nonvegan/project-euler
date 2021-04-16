# def triangle_num(n):
#     if n == 1:
#         return 1
#     return n + triangle_num(n - 1)
#
#
# def num_factors(n):
#     if n == 1:
#         return 1
#     counter = 2
#     for i in range(2, int(n / 2) + 1):
#         if n % i == 0:
#             counter += 1
#     return counter
