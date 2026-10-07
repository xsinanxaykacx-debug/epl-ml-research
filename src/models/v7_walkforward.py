"""V7 walk-forward model."""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.calibration import CalibratedClassifierCV
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings("ignore")


def v7_model_egit(X_train, y_train):
    """V7 ensemble model (XGBoost + Random Forest + Isotonic)."""
    xgb = XGBClassifier(
        n_estimators=300, max_depth=6, learning_rate=0.05,
        random_state=42, eval_metric="mlogloss",
        use_label_encoder=False,
    )
    rf = RandomForestClassifier(
        n_estimators=300, max_depth=10,
        min_samples_split=20, random_state=42, n_jobs=-1,
    )
    ensemble = VotingClassifier(
        estimators=[("xgb", xgb), ("rf", rf)],
        voting="soft", n_jobs=-1,
    )
    ensemble.fit(X_train, y_train)

    kalibre = CalibratedClassifierCV(ensemble, method="isotonic", cv=3)
    kalibre.fit(X_train, y_train)

    return kalibre
