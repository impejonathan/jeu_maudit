import streamlit as st
import pandas as pd
import random

# Chargement des mots à partir du fichier CSV
mots_df = pd.read_csv('666_mots.csv')
mots_liste = mots_df.iloc[:, 0].tolist()

def melanger_mots():
    """Mélange les mots dans la liste des mots."""
    random.shuffle(mots_liste)

def selectionner_mots_indices():
    """Sélectionne les mots secrets et les indices pour chaque mot secret.
    
    Retourne:
        tuple: Un tuple contenant une liste de mots secrets et une liste d'indices pour chaque mot secret.
    """
    melanger_mots()
    mots_secrets = mots_liste[:7]
    indices = random.choices(range(2, 6), k=7) # Nombre d'indices pour chaque mot secret
    return mots_secrets, indices

def jouer_manche(mots_secrets, indices):
    """Joue une manche du jeu avec les mots secrets et les indices donnés.
    
    Args:
        mots_secrets (list): Liste des mots secrets pour la manche.
        indices (list): Liste des indices pour chaque mot secret.
    """
    pass

def main():
    """Fonction principale pour exécuter le jeu."""
    st.title("Jeu des 666 mots ")
    mots_secrets, indices = selectionner_mots_indices()

    # Génération de la liste des pénalités
    penalites = []
    for i in range(len(mots_secrets)):
        if random.random() < 0.25: # 1 chance sur 4 d'avoir une pénalité
            penalites.append("Oui")
        else:
            penalites.append("Non")

    # Création du DataFrame à partir des listes mots_secrets, indices et penalites
    data = {'Mots secrets': mots_secrets, 'Indices': indices, 'Pénalité': penalites}
    df = pd.DataFrame(data)

    # Affichage du DataFrame sous forme de tableau avec st.table
    st.table(df)

    if st.button("Nouveaux indices"):
        mots_secrets, indices = selectionner_mots_indices()

if __name__ == '__main__':
    main()
