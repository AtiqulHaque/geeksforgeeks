def camelcase(s):
    i = 0
    sl = len(s) - 1
    totalCount = 0

    while True:
        if i > sl:
            return totalCount
        else:
            if s[i].isupper():
                if totalCount == 0:
                    totalCount += 2
                else:
                    totalCount += 1
            i += 1


print(camelcase("saveChangesInThe"))