def format_phone_number(number: list[int]) -> str:
    if len(number) == 10:
        output = ""
        output += "("
        output += str(number[0]) + str(number[1]) + str(number[2])
        output += ") "
        output += str(number[3]) + str(number[4]) + str(number[5])
        output += "-"
        output += str(number[6]) + str(number[7]) + str(number[8]) + str(number[9])
        return output
    else: return

output = format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(output)

output = format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])
print(output)

output = format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7])
print(output)