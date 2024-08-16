# README - Analyse du Code Décompilé et de l'ASM

## Introduction

Ce document fournit une analyse détaillée du code décompilé en C ainsi que de l'assemblage (ASM) correspondant pour un programme de type "bombe". Ce programme est conçu pour tester vos compétences en débogage et en compréhension de code bas niveau. Vous devrez examiner les différentes phases du programme, comprendre la logique implémentée dans chaque phase, et déterminer les entrées correctes pour désamorcer la bombe.

## Structure du Programme

Le programme est structuré autour de six phases, chacune nécessitant une entrée correcte pour éviter l'explosion de la bombe. Les phases sont implémentées dans le code décompilé et sont associées à des fonctions spécifiques en ASM.

### Fonctions Principales

1. **main** : La fonction principale qui orchestre le déroulement des phases. Elle initialise la bombe, puis passe successivement à chaque phase, en vérifiant l'entrée de l'utilisateur.
   
2. **initialize_bomb** : Fonction appelée au début pour initialiser l'état de la bombe.

3. **phase_defused** : Fonction appelée après chaque phase réussie pour marquer la phase comme désamorcée.

4. **explode_bomb** : Fonction appelée si une mauvaise entrée est détectée, provoquant l'explosion de la bombe.

### Phases du Programme

#### Phase 1 : Comparaison de Chaînes

- **Code décompilé** :
  ```c
  void phase_1(const char *line) {
      if (strings_not_equal(line, "Public speaking is very easy."))
          explode_bomb();
  }
  ```
- **ASM** :
  ```asm
  0x08048b20 <+0>:	push   %ebp
  0x08048b21 <+1>:	mov    %esp,%ebp
  0x08048b23 <+3>:	sub    $0x8,%esp
  ...
  0x08048b46 <+38>:	ret
  ```

- **Explication** : Cette phase compare l'entrée de l'utilisateur avec la chaîne `"Public speaking is very easy."`. Si elles ne correspondent pas, la bombe explose.

#### Phase 2 : Séquence Numérique

- **Code décompilé** :
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
- **ASM** :
  ```asm
  0x08048b48 <+0>:	push   %ebp
  0x08048b49 <+1>:	mov    %esp,%ebp
  0x08048b4b <+3>:	sub    $0x20,%esp
  ...
  0x08048b96 <+78>:	ret
  ```

- **Explication** : L'utilisateur doit entrer une séquence de 6 nombres où chaque nombre suivant est le précédent multiplié par son indice (commençant à 2).

#### Phase 3 : Switch et Validation

- **Code décompilé** :
  ```c
  void phase_3(const char *line) {
      int num, result;
      char c, expected_char;
      sscanf(line, "%d %c %d", &num, &c, &result);
      switch (num) {
          case 0: expected_char = 'q'; if (result != 777) explode_bomb(); break;
          ...
          default: explode_bomb();
      }
      if (c != expected_char) explode_bomb();
  }
  ```
- **ASM** :
  ```asm
  0x08048b98 <+0>:	push   %ebp
  0x08048b99 <+1>:	mov    %esp,%ebp
  0x08048b9b <+3>:	sub    $0x14,%esp
  ...
  0x08048c9f <+263>:	ret
  ```

- **Explication** : Un nombre, une lettre et un autre nombre doivent être entrés. Le programme vérifie ces valeurs selon un `switch-case`.

#### Phase 4 : Fonction de Calcul

- **Code décompilé** :
  ```c
  void phase_4(const char *line) {
      int value;
      if (sscanf(line, "%d", &value) != 1 || value <= 0) explode_bomb();
      if (func4(value) != 55) explode_bomb();
  }
  ```
- **ASM** :
  ```asm
  0x08048ce0 <+0>:	push   %ebp
  0x08048ce1 <+1>:	mov    %esp,%ebp
  0x08048ce3 <+3>:	sub    $0x18,%esp
  ...
  0x08048d2a <+74>:	ret
  ```

- **Explication** : L'utilisateur doit entrer un nombre positif qui, passé à `func4`, doit renvoyer 55. `func4` implémente une logique de type Fibonacci modifié.

#### Phase 5 : Masquage de Chaînes

- **Code décompilé** :
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
- **ASM** :
  ```asm
  0x08048d2c <+0>:	push   %ebp
  0x08048d2d <+1>:	mov    %esp,%ebp
  0x08048d2f <+3>:	sub    $0x10,%esp
  ...
  0x08048d94 <+104>:	ret
  ```

- **Explication** : L'utilisateur entre une chaîne de 6 caractères. Chaque caractère est masqué par une table de correspondance, et la chaîne résultante doit correspondre à `"giants"`.

#### Phase 6 : Ordre des Nombres

- **Code décompilé** :
  ```c
  void phase_6(const char *line) {
      int nums[6];
      read_six_numbers(line, nums);
      for (int i = 0; i < 5; i++) {
          for (int j = i + 1; j < 6; j++) {
              if (nums[i] == nums[j]) explode_bomb();
          }
      }
  }
  ```
- **ASM** :
  ```asm
  0x08048d98 <+0>:	push   %ebp
  0x08048d99 <+1>:	mov    %esp,%ebp
  0x08048d9b <+3>:	sub    $0x4c,%esp
  ...
  0x08048e90 <+248>:	ret
  ```

- **Explication** : L'utilisateur doit entrer 6 nombres dans un ordre spécifique, sans répétitions, basés sur la valeur de nœuds ordonnés par grandeur.
