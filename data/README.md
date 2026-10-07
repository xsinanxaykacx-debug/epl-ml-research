# \# Veri

# 

# \## Ham Veri (data/raw/)

# 

# \### Understat (`understat\_match\_1524.csv`)

# \- Kaynak: understat.com

# \- İçerik: EPL 2015-2024 maçları, xG dahil

# \- Boyut: \~3420 maç

# \- Sütunlar: id, fid, date, season, team\_h, team\_a, h\_goals, a\_goals, h\_xg, a\_xg, h\_shot, a\_shot, h\_shotOnTarget, a\_shotOnTarget, h\_deep, a\_deep, h\_ppda, a\_ppda

# 

# \### Football-Data (`buyuk\_veri.csv`, `epl\_2022\_2025.csv`)

# \- Kaynak: football-data.co.uk

# \- İçerik: EPL + diğer ligler, oranlar

# \- Sütunlar: Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR, B365H, B365D, B365A

# 

# \## İşlenmiş Veri (data/processed/)

# 

# \### `epl\_v10\_merged.csv`

# \- Boyut: 760 maç

# \- Dönem: 2022-2024

# \- Kaynak: Understat + Football-Data

# \- İçerik: xG + oranlar + sonuçlar

# 

# \### `v11a\_final\_predictions.csv`

# \- Boyut: 379 maç (2023/24)

# \- İçerik: V7, Market, V11-A, V11-C olasılıkları

# 

# \## Erişim

# 

# ```python

# import pandas as pd

# df = pd.read\_csv('data/processed/epl\_v10\_merged.csv')

