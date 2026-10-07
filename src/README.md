# \# Kaynak Kod (src/)

# 

# \## Yapı

# 

# \- `data\_loader.py` — Veri yükleme fonksiyonları

# \- `features.py` — Feature engineering

# \- `models/` — Model eğitimi (V7)

# \- `analysis/` — Edge analizi

# 

# \## Kullanım

# 

# ```python

# from src.data\_loader import load\_merged, load\_v7\_predictions

# from src.features import form\_hesapla, fark\_ozellikleri, market\_olasilik

# 

# df = load\_merged()

# df = form\_hesapla(df, pencere=5)

# df = fark\_ozellikleri(df)

# df = market\_olasilik(df)

