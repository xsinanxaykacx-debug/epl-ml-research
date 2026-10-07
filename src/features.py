"""Feature engineering."""

import pandas as pd
import numpy as np


FORM_5 = [
    "ev_xg_5", "ev_gol_5", "ev_isabet_5", "ev_deep_5", "ev_ppda_5",
    "dep_xg_5", "dep_gol_5", "dep_isabet_5", "dep_deep_5", "dep_ppda_5",
]

FORM_10 = [
    "ev_xg_10", "ev_gol_10", "dep_xg_10", "dep_gol_10",
]

FARK_OZELLIKLER = [
    "fark_xg_5", "fark_gol_5", "fark_isabet_5", "fark_deep_5", "fark_ppda_5",
    "fark_xg_10", "fark_gol_10",
]

TUM_OZELLIKLER = FORM_5 + FORM_10 + FARK_OZELLIKLER


def form_hesapla(df: pd.DataFrame, pencere: int = 5) -> pd.DataFrame:
    """Form özelliklerini hesapla."""
    gecmis = {}

    yeni_sutunlar = [
        f"ev_xg_{pencere}", f"ev_gol_{pencere}",
        f"ev_isabet_{pencere}", f"ev_deep_{pencere}", f"ev_ppda_{pencere}",
        f"dep_xg_{pencere}", f"dep_gol_{pencere}",
        f"dep_isabet_{pencere}", f"dep_deep_{pencere}", f"dep_ppda_{pencere}",
    ]

    for s in yeni_sutunlar:
        if s not in df.columns:
            df[s] = 0.0

    for idx, mac in df.iterrows():
        for prefix, takim in [("ev", mac["team_h"]), ("dep", mac["team_a"])]:
            son = gecmis.get(takim, [])[-pencere:]
            if son:
                n = len(son)
                df.at[idx, f"{prefix}_xg_{pencere}"] = sum(m["xg"] for m in son) / n
                df.at[idx, f"{prefix}_gol_{pencere}"] = sum(m["gol"] for m in son) / n
                df.at[idx, f"{prefix}_isabet_{pencere}"] = sum(m["isabet"] for m in son) / n
                df.at[idx, f"{prefix}_deep_{pencere}"] = sum(m["deep"] for m in son) / n
                df.at[idx, f"{prefix}_ppda_{pencere}"] = sum(m["ppda"] for m in son) / n

        gecmis.setdefault(mac["team_h"], []).append({
            "xg": mac["h_xg"], "gol": mac["h_goals"],
            "isabet": mac["h_shotOnTarget"], "deep": mac["h_deep"], "ppda": mac["h_ppda"],
        })
        gecmis.setdefault(mac["team_a"], []).append({
            "xg": mac["a_xg"], "gol": mac["a_goals"],
            "isabet": mac["a_shotOnTarget"], "deep": mac["a_deep"], "ppda": mac["a_ppda"],
        })

    return df


def fark_ozellikleri(df: pd.DataFrame) -> pd.DataFrame:
    """Fark özelliklerini hesapla."""
    df["fark_xg_5"] = df["ev_xg_5"] - df["dep_xg_5"]
    df["fark_gol_5"] = df["ev_gol_5"] - df["dep_gol_5"]
    df["fark_isabet_5"] = df["ev_isabet_5"] - df["dep_isabet_5"]
    df["fark_deep_5"] = df["ev_deep_5"] - df["dep_deep_5"]
    df["fark_ppda_5"] = df["ev_ppda_5"] - df["dep_ppda_5"]
    df["fark_xg_10"] = df["ev_xg_10"] - df["dep_xg_10"]
    df["fark_gol_10"] = df["ev_gol_10"] - df["dep_gol_10"]
    return df


def market_olasilik(df: pd.DataFrame) -> pd.DataFrame:
    """Marj-normalize edilmiş market olasılıkları."""
    q_home = 1 / df["B365H"]
    q_draw = 1 / df["B365D"]
    q_away = 1 / df["B365A"]
    toplam = q_home + q_draw + q_away

    df["m_home"] = q_home / toplam
    df["m_draw"] = q_draw / toplam
    df["m_away"] = q_away / toplam
    df["marj"] = toplam

    return df