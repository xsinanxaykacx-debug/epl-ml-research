"""Veri yükleme fonksiyonları."""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"


def load_understat() -> pd.DataFrame:
    """Understat xG verisi."""
    df = pd.read_csv(RAW_DIR / "understat_match_1524.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


def load_merged() -> pd.DataFrame:
    """V10 merge verisi."""
    df = pd.read_csv(PROCESSED_DIR / "epl_v10_merged.csv")
    df["Date"] = pd.to_datetime(df["Date"]).dt.normalize()
    return df


def load_v7_predictions() -> pd.DataFrame:
    """V7 walk-forward tahminler."""
    df = pd.read_csv(PROCESSED_DIR / "epl_walk_forward_predictions.csv")
    df["Date"] = pd.to_datetime(df["date"]).dt.normalize()
    return df


def load_v11a_predictions() -> pd.DataFrame:
    """V11-A final tahminleri."""
    return pd.read_csv(PROCESSED_DIR / "v11a_final_predictions.csv")


def load_v11c_predictions() -> pd.DataFrame:
    """V11-C final tahminleri."""
    return pd.read_csv(PROCESSED_DIR / "v11c_final_predictions.csv")