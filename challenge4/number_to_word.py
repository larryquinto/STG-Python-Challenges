def convert(num):
    units = ("", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ",
             "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen ")
    tens = ("", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety ")

    if num == 0:
        return "Zero"

    if num < 0:
        return "Minus "+convert(-num)

    if num < 20:
        return units[num]

    if num < 100:

        return tens[num // 10] + units[int(num % 10)]

    if num < 1000:
        return units[num // 100] + "Hundred " + convert(int(num % 100))

    if num < 1000000:
        return convert(num // 1000) + "Thousand " + convert(int(num % 1000))

    if num < 1000000000:
        return convert(num // 1000000) + "Million " + convert(int(num % 1000000))

    if num < 1000000000000:
        return convert(num // 1000000000) + "Billion " + convert(int(num % 1000000000))

    if num < 1000000000000000:
        return convert(num // 1000000000000) + "Trillion " + convert(int(num % 1000000000000))

    if num < 1000000000000000000:
        return convert(num // 1000000000000000) + "Quadrillion " + convert(int(num % 1000000000000000))

    return convert(num // 1000000000000000000) + "Quintillion " + convert(int(num % 1000000000000000000))

# try:
#     num = (int(input("Enter A Whole Number Please, Then Press Enter: ")))
# except:
#     print("Try Again")
# else:
#     print(convert(num))