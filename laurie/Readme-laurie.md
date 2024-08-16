
---

### Phase 1 : Vérification de la chaîne de caractères

**Code :**
```c
void phase_1(const char *line) {
    if (strings_not_equal(line, "Public speaking is very easy."))
        explode_bomb();
}
```

**Explication :**
La première phase consiste simplement à entrer une chaîne de caractères spécifique. La fonction `strings_not_equal` compare l'entrée utilisateur avec la chaîne `"Public speaking is very easy."`. Si la chaîne entrée ne correspond pas exactement, la bombe explose.

**Solution :**
Entrez `"Public speaking is very easy."` pour désamorcer cette phase.

### Phase 2 : Séquence de nombres

**Code :**
```c
void phase_2(const char *line) {
    int nums[6];
    read_six_numbers(line, nums);
    for (int i = 0; i < 5; i++) {
        if (nums[i + 1] != nums[i] * (i + 2))
            explode_bomb();
    }
}
```

**Explication :**
La deuxième phase vous demande de fournir une séquence de six nombres. Chaque nombre suivant dans la séquence doit être égal au précédent multiplié par son indice (commençant à 2).

**Calcul :**
- 1 * 2 = 2
- 2 * 3 = 6
- 6 * 4 = 24
- 24 * 5 = 120
- 120 * 6 = 720

**Solution :**
Entrez la séquence `1 2 6 24 120 720` pour désamorcer cette phase.

### Phase 3 : Switch case avec des conditions

**Code :**
```c
void phase_3(const char *line) {
    int num, result;
    char c, expected_char;
    sscanf(line, "%d %c %d", &num, &c, &result);
    
    switch (num) {
        case 0: expected_char = 'q'; if (result != 777) explode_bomb(); break;
        case 1: expected_char = 'b'; if (result != 214) explode_bomb(); break;
        case 2: expected_char = 'b'; if (result != 755) explode_bomb(); break;
        case 3: expected_char = 'k'; if (result != 251) explode_bomb(); break;
        case 4: expected_char = 'o'; if (result != 160) explode_bomb(); break;
        case 5: expected_char = 't'; if (result != 458) explode_bomb(); break;
        case 6: expected_char = 'v'; if (result != 780) explode_bomb(); break;
        case 7: expected_char = 'b'; if (result != 524) explode_bomb(); break;
        default: explode_bomb();
    }

    if (c != expected_char) explode_bomb();
}
```

**Explication :**
Dans cette phase, vous devez entrer trois valeurs : un nombre, une lettre et un autre nombre. Le code utilise un `switch` pour vérifier si les entrées correspondent à celles attendues pour chaque cas (de 0 à 7).

**Solution :**
Par exemple, si vous entrez `1 b 214`, cela correspond au cas 1, où la lettre est 'b' et la valeur est 214. Vous devez choisir l'une des combinaisons valides en fonction du numéro.

### Phase 4 : Suite de Fibonacci modifiée

**Code :**
```c
void phase_4(const char *line) {
    int value;
    if (sscanf(line, "%d", &value) != 1 || value <= 0) explode_bomb();

    if (func4(value) != 55) explode_bomb();
}
```

**Explication :**
Cette phase nécessite de calculer une valeur qui, une fois passée à la fonction `func4`, doit renvoyer 55. Cette fonction simule une suite de Fibonacci. Le défi est de trouver combien de coups il faut pour atteindre 55.

**Solution :**
Le nombre de coups requis pour atteindre 55 dans une suite de Fibonacci est 9.

### Phase 5 : Masquage de chaînes

**Code :**
```c
void phase_5(const char *line) {
    if (string_length(line) != 6) explode_bomb();

    char mapped[7];
    for (int i = 0; i < 6; i++) {
        mapped[i] = array_123[line[i] & 0xF];
    }
    mapped[6] = '\0';

    if (strings_not_equal(mapped, "giants")) explode_bomb();
}
```

**Explication :**
Cette phase vous demande d'entrer une chaîne de 6 caractères. Chaque caractère est masqué (ou transformé) via une table de correspondance (array_123) et doit se transformer en `"giants"`.

**Solution :**
L'une des combinaisons qui fonctionne est `"opekmq"`.

### Phase 6 : Ordre des nombres

**Code :**
```c
void phase_6(const char *line) {
    int nums[6], i, j, k;
    read_six_numbers(line, nums);

    for (i = 0; i < 5; i++) {
        for (j = i + 1; j < 6; j++) {
            if (nums[i] == nums[j]) explode_bomb();
        }
    }
}
```

**Explication :**
La dernière phase consiste à entrer une séquence de six nombres qui ne doivent pas se répéter. L'ordre est déterminé par un tri en fonction des valeurs de nœuds dans une structure de données (dans ce cas, une liste liée).

**Solution :**
L'ordre correct des nœuds est `4 2 6 1 3 5`.

### Conclusion

Une fois toutes les phases complétées, le mot de passe final est constitué de toutes les réponses concaténées. Par exemple :

```plaintext
Publicspeakingisveryeasy.126241207201b2149opekmq426135
```

Ce mot de passe est ensuite utilisé pour vous connecter en tant qu'utilisateur "thor".

---