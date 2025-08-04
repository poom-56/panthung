def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

my_list = [50, 500, 5000]
result = sum_of_squares(my_list)

print("ผลบวกของกำลังสองคือ:", result)
