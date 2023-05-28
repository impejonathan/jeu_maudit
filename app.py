import streamlit as st
import pandas as pd
import random

# Chargement des mots à partir du fichier CSV
mots_df = pd.read_csv('666_mots.csv')
mots_liste = mots_df.iloc[:, 0].tolist()

# Fonction pour mélanger les mots
def melanger_mots():
    random.shuffle(mots_liste)

# Fonction pour sélectionner les mots et les indices
def selectionner_mots_indices():
    melanger_mots()
    mots_secrets = mots_liste[:7]
    indices = random.choices(range(2, 6), k=7) # Nombre d'indices pour chaque mot secret
    return mots_secrets, indices

# Fonction pour jouer une manche
def jouer_manche(mots_secrets, indices):
    pass

# Fonction principale
def main():
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
