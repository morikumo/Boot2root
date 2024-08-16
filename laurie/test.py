def simulate_phase_5_minuscules():
    static_string = "isrveawhobpnutfg"
    target = "giants"
    indices_needed = []

    for char in target:
        index = static_string.index(char)
        indices_needed.append(index)

    print("Indices needed to form 'giants':", indices_needed)

    print("\nPossible lowercase characters for each index to form 'giants':")
    for i, index in enumerate(indices_needed):
        possible_chars = []
        #Pour chaque caractère de l'alphabet en minuscule
        for char in range(97, 123):
            if (char & 0xF) == index:
                possible_chars.append(chr(char))
        print(f"{target[i]} (index {index}): {possible_chars}")

simulate_phase_5_minuscules()
