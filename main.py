"""Point d'entrée principal de l'application d'analyse GTFS.

Usage:
    $ python main.py
"""

from src.analyses import (
    analyser_amplitude_max,
    analyser_arrets_par_mode,
    analyser_correspondances,
    analyser_top_lignes_arrets,
)


def main() -> None:
    """Exécute et affiche l'ensemble des analyses GTFS dans la console."""
    print("==================================================")
    print("          RAPPORT D'ANALYSE DONNÉES GTFS          ")
    print("==================================================\n")

    # 1. Nombre d'arrêts par mode de transport
    print("--- 1. NOMBRE D'ARRÊTS PAR MODE DE TRANSPORT ---")
    df_modes = analyser_arrets_par_mode()
    print(df_modes.to_string(index=False))
    print("\n" + "-" * 50 + "\n")

    # 2. Top 10 des lignes avec le plus d'arrêts
    print("--- 2. TOP 10 DES LIGNES PAR NOMBRE D'ARRÊTS ---")
    df_top_lignes = analyser_top_lignes_arrets()
    print(df_top_lignes.to_string(index=False))
    print("\n" + "-" * 50 + "\n")

    # 3. Ligne avec la plus grande amplitude horaire
    print("--- 3. LIGNE AVEC LA PLUS GRANDE AMPLITUDE HORAIRE ---")
    df_amplitude = analyser_amplitude_max()
    print(df_amplitude.to_string(index=False))
    print("\n" + "-" * 50 + "\n")

    # 4. Top 10 des correspondances par station
    print("--- 4. TOP 10 DES CORRESPONDANCES PAR STATION ---")
    df_correspondances = analyser_correspondances()
    print(df_correspondances.to_string(index=False))
    print("\n==================================================")


if __name__ == "__main__":
    main()
