"""Module d'exécution des requêtes SQL GTFS et d'analyse avec Pandas."""

import pandas as pd

from src.connexion import engine
from src.requetes import (
    QUERY_AMPLITUDE_HORAIRE_MAX,
    QUERY_ARRETS_PAR_MODE,
    QUERY_CORRESPONDANCES_PAR_STATION,
    QUERY_TOP_LIGNES_ARRETS,
)


def analyser_arrets_par_mode() -> pd.DataFrame:
    """Retourne le nombre d'arrêts uniques par mode de transport."""
    with engine.connect() as conn:
        return pd.read_sql_query(QUERY_ARRETS_PAR_MODE, conn)


def analyser_top_lignes_arrets() -> pd.DataFrame:
    """Retourne les 10 lignes avec le plus d'arrêts."""
    with engine.connect() as conn:
        return pd.read_sql_query(QUERY_TOP_LIGNES_ARRETS, conn)


def analyser_amplitude_max() -> pd.DataFrame:
    """Retourne la ligne avec la plus grande amplitude horaire."""
    with engine.connect() as conn:
        return pd.read_sql_query(QUERY_AMPLITUDE_HORAIRE_MAX, conn)


def analyser_correspondances() -> pd.DataFrame:
    """Retourne le nombre de correspondances par station."""
    with engine.connect() as conn:
        return pd.read_sql_query(QUERY_CORRESPONDANCES_PAR_STATION, conn)
