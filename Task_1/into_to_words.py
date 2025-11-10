def into_to_words(n):
    units = [
        "", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    hundred = "hundred"
    thousand = "thousand"

    result = []
    if n == 0:
        result.append("zero")
        return result

    elif n <= 19:
        result.append(units[n])
        return result
    elif n <= 99:
        result.append(tens[n // 10])
        result.append(units[n % 10])
        return result
    elif n <= 999:
        result.append(units[n // 100])
        result.append(hundred)
        result.append(tens[(n % 100) // 10])
        result.append(units[n % 10])
        return result
    elif n == 1000:
        result.append("one thousand")
        return result



digit = int(input())

print(*into_to_words(digit))