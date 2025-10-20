def sum(digits):
    cloud = [int(i) for i in digits if i.isdigit()]

    total = 0
    for digit in cloud:
        total += digit

    return total

n = input().split()

print(sum(n))