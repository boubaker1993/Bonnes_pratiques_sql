import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, inspect, text
from IPython.display import display
load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
inspector = inspect(engine)

table_summary_list = []

# Récupération des schémas hors système
schemas = [
    s
    for s in inspector.get_schema_names()
    if s not in ["pg_catalog", "information_schema"]
]

with engine.connect() as conn:
    for schema in schemas:
        for table in inspector.get_table_names(schema=schema):
            # 1. Volumétrie (Nombre de lignes)
            volume = conn.execute(
                text(f'SELECT COUNT(*) FROM "{schema}"."{table}"')
            ).scalar()

            # 2. Liste des colonnes et Nombre de colonnes
            columns_info = inspector.get_columns(
                table_name=table, schema=schema
            )
            columns_list = [col["name"] for col in columns_info]
            nb_columns = len(columns_list)

            # 3. Clé(s) Primaire(s)
            pk_constraint = inspector.get_pk_constraint(
                table_name=table, schema=schema
            )
            pk_cols = pk_constraint.get("constrained_columns", [])
            primary_key_str = ", ".join(pk_cols) if pk_cols else "-"

            # 4. Clé(s) Étrangère(s) et références
            fk_constraints = inspector.get_foreign_keys(
                table_name=table, schema=schema
            )
            fk_list = []
            for fk in fk_constraints:
                for col, ref_col in zip(
                    fk["constrained_columns"], fk["referred_columns"]
                ):
                    fk_list.append(f"{col} -> {fk['referred_table']}({ref_col})")
            foreign_key_str = ", ".join(fk_list) if fk_list else "-"

            # Construction de la ligne pour la table
            table_summary_list.append({
                "schema": schema,
                "table_name": table,
                "volume_lignes": volume,
                "nb_colonnes": nb_columns,
                "liste_colonnes": ", ".join(columns_list),
                "cle_primaire": primary_key_str,
                "cle_etrangere": foreign_key_str,
            })

# DataFrame global (une ligne par table)
df_summary = pd.DataFrame(table_summary_list)

display(df_summary)