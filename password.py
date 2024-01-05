# Projet Script de sécurité : Outil de vérification de la sécurité des Mots de Passe par Othman BELAIDI.

import string

def is_secure(password):
    # Vérifie que le mot de passeS a au moins 8 caractères
    if len(password) < 8:
        return False
    # Vérifie la présence de chiffres
    if not any(char.isdigit() for char in password):
        return False
    # Vérifie la présence de lettres
    if not any(char.isalpha() for char in password):
        return False
    # Vérifie la présence de caractères spéciaux
    if not any(char in string.punctuation for char in password):
        return False
    # Vérifie la présence d'au moins 1 majuscule
    if not any(char.isupper() for char in password):
        return False
    return True

password = ''
while True:
    char = input("Entrez votre mot de passe ou 'e' pour exit: ")
    if char == "e":
        break
    password += char
    if is_secure(password):
        print('Le mot de passe est sécurisé !')
        break
    else:
        print("Le mot de passe n'est pas sécurisé; merci de réessayez")