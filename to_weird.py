def to_weird(cloud):
    result = []
    new_word = ''

    for i in cloud:
        for k in range(len(i)):
            if k == 0 or k % 2 ==0:
                new_word += i[k].upper()
            elif k % 2 == 1:
                new_word += i[k].lower()

        result.append(new_word)
        new_word = ''

    return result


s = input().split()

print(*to_weird(s))