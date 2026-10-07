"""Edge analizi fonksiyonları."""

import numpy as np
from sklearn.metrics import log_loss


def ll_3sinif(y_true, P):
    """Çok sınıflı LogLoss."""
    return log_loss(y_true, P, labels=[0, 1, 2])


def divergence_hesapla(P_v7, P_market):
    """V7 ile market arasındaki maksimum ayrışma."""
    return np.abs(P_v7 - P_market).max(axis=1)


def shrunk_olasilik(P_v7, P_market, alpha_bands):
    """Divergence-based shrinkage.

    alpha_bands: [(lo, hi, alpha), ...]
    """
    divergence = divergence_hesapla(P_v7, P_market)
    P_out = np.zeros_like(P_v7)

    for lo, hi, alpha in alpha_bands:
        maske = (divergence >= lo) & (divergence < hi)
        if maske.sum() == 0:
            continue
        P_out[maske] = alpha * P_v7[maske] + (1 - alpha) * P_market[maske]

    P_out = P_out / P_out.sum(axis=1, keepdims=True)
    return P_out