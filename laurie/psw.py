# Toutes les possibilités de mots de passe sont affichées.
index1_options = [
    "0q777", "1b214", "2b755", "3k251", "4o160", "5t458", "6v780", "7b524"
]
index2_options = [
    "opekma", "opukmq", "opukma", "opekmq"
]

# Fonction pour générer et afficher les mots de passe
def generate_passwords():
    base_pattern = "Publicspeakingisveryeasy.12624120720{index1}9{index2}426135"
    passwords = []

    for index1 in index1_options:
        for index2 in index2_options:
            password = base_pattern.format(index1=index1, index2=index2)
            passwords.append(password)
    
    return passwords

if __name__ == "__main__":
    passwords = generate_passwords()
    for pwd in passwords:
        print(pwd)
