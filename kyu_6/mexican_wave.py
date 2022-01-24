def wave(people):
    wave = []

    if len(people) == 0:
        return wave

    for i in range(len(people)):

        if people[i] == ' ':
            continue

        wave.append(people[:i] + people[i].upper() + people[i + 1:])

    return wave

print(wave('abc de'))

# clever
# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]