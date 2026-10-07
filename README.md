# ⚽ EPL ML Research — Premier League İddaa & Bahis Analizi

**Premier League futbol maçları için makine öğrenmesi tabanlı maç tahmini, xG analizi, bahis oranı karşılaştırması ve value bet araştırması.**

Bu proje, İngiltere Premier League maçlarında **ev sahibi / beraberlik / deplasman** olasılıklarını makine öğrenmesi ile tahmin edip, bu tahminleri **bahis piyasasının açılış oranlarıyla** karşılaştırır.

Amaç sadece maç sonucu tahmin etmek değildir.

> **Makine öğrenmesi modeli, bookmaker/bahis piyasasının zaten bildiği bilgiden daha iyi bir olasılık tahmini üretebilir mi?**

Ve daha önemlisi:

> **Modelin tahmin ettiği olasılık gerçekten bahis piyasasında ölçülebilir bir value bet avantajına dönüşüyor mu?**

Bu araştırmada cevap **OOS (out-of-sample) testleriyle** aranmıştır.

---

## 🎯 Araştırmanın Amacı

Futbol bahis analizinde çok sık görülen şu yaklaşımların gerçekten işe yarayıp yaramadığını test ediyoruz:

- Premier League maç tahmini
- İddaa maç sonucu tahmini
- 1X2 tahmin modeli
- xG (expected goals) tabanlı futbol analizi
- Machine Learning futbol tahmini
- Value bet / değerli bahis tespiti
- Bahis oranı ve model olasılığı karşılaştırması
- Bookmaker marketi ile model karşılaştırması
- Bahis stratejilerinin Out-of-Sample testi

Buradaki temel prensip:

**Model iyi tahmin yapıyor gibi görünüyorsa yeterli değildir. Gerçekten daha önce görmediği maçlarda da çalışması gerekir.**

---

# 📊 En Önemli Sonuç

Araştırmada birkaç farklı model ve bahis stratejisi test edildi.

Son karar **2023/24 Premier League sezonunun kilitlenmiş Out-of-Sample testinde** verildi.

| Model | LogLoss ↓ | Brier ↓ | Accuracy |
|---|---:|---:|---:|
| 🏆 Market Baseline | **0.91074** | **0.17807** | **59.63%** |
| V11-A Shrinkage | 0.91602 | 0.17905 | 58.05% |
| V11-C Dynamic | 0.91655 | 0.17907 | 58.84% |
| V7 ML Model | 0.96278 | 0.18961 | 55.15% |

### Sonuç

**Bahis piyasası, test edilen ML modellerinden daha iyi performans gösterdi.**

Bu proje bu nedenle bir **"garantili kazanç sistemi"** değildir.

Tam tersine, araştırmanın en değerli sonucu şudur:

> **Modeli marketi yenene kadar zorlamak yerine, marketi yenemediğimizi OOS testleriyle kanıtlayıp araştırmayı durdurduk.**

Bu sonuç, futbol bahis modellemesinde **overfitting ve backtest yanılgısının** ne kadar önemli olduğunu gösteriyor.

---

# 💰 Value Bet / Bahis Stratejisi Testleri

Tahmin modelinin iyi bir **LogLoss** değerine sahip olması otomatik olarak kârlı bahis anlamına gelmez.

Bu nedenle ayrıca value bet stratejileri test edildi.

## V10 — Value Bet Modeli

Model olasılığı ile bookmaker oranından hesaplanan implied probability karşılaştırıldı.

Temel yaklaşım:

```
Fair Probability = (1 / Odds) / Σ(1 / Odds)
```

Modelin beklenen değerinin belirli bir eşik üzerinde olması durumunda bahis sinyali üretildi.

Development döneminde seçilen eşik:

```
EV Threshold = 10%
```

### Development

```
275 bahis
+3,354 TL
ROI: +12.20%
```

İlk bakışta oldukça iyi görünmektedir.

Ancak parametre **Final OOS dönemine kilitlendiğinde**:

```
266 bahis
-6,417 TL
ROI: -24.12%
```

### Sonuç

**Development dönemindeki kârlılık Final OOS döneminde tekrarlanmadı.**

Bu, backtest sonuçlarına fazla güvenmenin neden tehlikeli olduğunu açık şekilde gösteriyor.

---

# 📉 V11 — Market Shrinkage

V7 modelinin tahminleri bookmaker marketinden fazla uzaklaştığında, tahmini tekrar markete doğru çekmek için shrinkage yöntemleri test edildi.

## V11-A

Temel formül:

```
P_final = α × P_model + (1 - α) × P_market
```

Development döneminde:

```
α = 0.20
```

seçildi.

Final OOS:

```
Market: 0.91074
V11-A:  0.91602
```

V11-A, V7'yi ciddi şekilde iyileştirdi.

Ancak:

**Marketi geçemedi.**

---

# 🔬 V11-C — Dynamic Shrinkage

Model ile market arasındaki olasılık farkına göre farklı shrinkage katsayıları test edildi.

Model:

```
< 5 percentage points
5–10 percentage points
≥ 10 percentage points
```

olmak üzere farklı divergence bölgelerinde ayrı α değerleri kullanacak şekilde test edildi.

343 farklı kombinasyon development döneminde karşılaştırıldı.

Seçilen kombinasyon:

```
(0.00, 0.40, 0.20)
```

Final OOS sonucu:

```
V11-C LogLoss = 0.91655
Market LogLoss = 0.91074
```

Yine market kazanmıştır.

Bu nedenle V11-C de **kilitlenmiş araştırma sonucunda başarısız kabul edilmiştir.**

---

# 📈 xG ve Futbol Verisi

Araştırmanın temel veri kaynaklarından biri:

**Understat Premier League maç verileri**

Kapsanan dönem:

```
2015-08-08 → 2024-05-19
```

Veri içerisinde aşağıdaki gibi futbol analizi değişkenleri bulunmaktadır:

- xG
- Goals
- Shots
- Deep
- PPDA
- Home Team
- Away Team
- Match Date
- Match Result
- çeşitli maç performans göstergeleri

Bahis marketi karşılaştırmasında ise:

**Football-Data / B365 opening odds**

kullanılmıştır.

---

# 🧠 Neden Bookmaker Marketi Baseline Olarak Kullanıldı?

Futbol bahis tahmininde yalnızca accuracy ölçmek yanıltıcı olabilir.

Örneğin:

```
Model Accuracy = 55%
```

tek başına modelin iyi olduğunu göstermez.

Eğer bahis piyasası aynı maçlarda:

```
Market Accuracy = 59%
```

seviyesindeyse model piyasadan daha iyi değildir.

Bu nedenle bu projede market:

> **Baseline**

olarak kullanılmıştır.

Karşılaştırmada özellikle:

- LogLoss
- Brier Score
- Accuracy
- implied probability
- model probability
- expected value
- ROI

birlikte değerlendirilmiştir.

---

# ⚠️ LogLoss ≠ Bahis Kârlılığı

Araştırmanın önemli sonuçlarından biri budur.

Bir model:

```
daha iyi LogLoss
```

ürettiğinde bunun anlamı:

**olasılık tahminleri daha iyi olabilir.**

Ama bu otomatik olarak:

```
daha yüksek ROI
```

anlamına gelmez.

Bahis stratejisinde ayrıca:

- bookmaker odds
- market margin
- selection bias
- bet frequency
- odds distribution
- variance
- sample size
- probability calibration

gibi faktörler devreye girer.

Bu nedenle:

> **İyi tahmin modeli ≠ otomatik olarak kârlı bahis sistemi**

---

# 🧪 Walk-Forward Validation

Bu projede klasik random train/test split kullanılmamıştır.

Çünkü futbol bahis tahmininde gelecekteki maçlardan bilgi alıp geçmiş maçları tahmin etmek **data leakage** oluşturabilir.

Bunun yerine kronolojik yapı kullanılmıştır:

```
GEÇMİŞ MAÇLAR
      ↓
TRAIN
      ↓
MODEL
      ↓
GELECEK MAÇ
      ↓
PREDICTION
      ↓
RESULT
```

Model gelecekteki maçların sonucunu önceden görmez.

V7 walk-forward testinde:

```
Usable matches: 3397
Train:          2377
Test:           1020
Refit interval: 10
```

Test dönemi:

```
2021-11-21 → 2024-05-19
```

---

# 💵 Bookmaker Overround

B365 opening odds üzerinden fair probability hesaplandı:

```
qH = 1 / OddsH
qD = 1 / OddsD
qA = 1 / OddsA

P(H) = qH / (qH + qD + qA)
P(D) = qD / (qH + qD + qA)
P(A) = qA / (qH + qD + qA)
```

Ortalama bookmaker overround yaklaşık:

```
5.40%
```

olarak ölçüldü.

Bu değer **ROI değildir**.

Bahis piyasasının marjını ifade eder.

---

# 🚨 Overfitting'e Karşı Kurallar

Bu araştırmada özellikle şu hatalardan kaçınılmaya çalışılmıştır:

### ❌ Final OOS üzerinde tekrar parametre seçmek

Yapılmadı.

### ❌ Kazançlı görünen sezonu seçmek

Yapılmadı.

### ❌ Marketi geçmeyen modeli zorla optimize etmek

Yapılmadı.

### ❌ Backtest sonucunu garanti olarak sunmak

Yapılmadı.

### ❌ Gelecek maç bilgisini feature olarak kullanmak

Kullanılmadı.

### ❌ Negatif sonucu gizlemek

Gizlenmedi.

---

# 📚 Test Edilen Modeller

Araştırmanın farklı aşamalarında:

```
V7
 ↓
V10 Value Bet
 ↓
V11-A Market Shrinkage
 ↓
V11-C Dynamic Shrinkage
```

yaklaşımı kullanılmıştır.

Amaç modeli sürekli karmaşıklaştırmak değil, her yeni yaklaşımın **daha önce görülmemiş veride** gerçekten işe yarayıp yaramadığını ölçmektir.

---

# 🏆 Final OOS Sonucu

2023/24 Premier League final testinde:

```
Market       0.91074
V11-A        0.91602
V11-C        0.91655
V7           0.96278
```

**LogLoss düşük olan model daha iyidir.**

Dolayısıyla sıralama:

```
🥇 Market
🥈 V11-A
🥉 V11-C
4️⃣  V7
```

Sonuç nettir:

> **Bu veri ve bu protokol altında test edilen ML modelleri bookmaker marketini geçemedi.**

---

# 🧩 Araştırmadan Çıkan Dersler

## 1. Backtest sonucu gerçek performans değildir

Development döneminde çalışan strateji Final OOS'ta çalışmayabilir.

## 2. Market güçlü bir baseline'dır

Futbol bahis piyasasını geçmek, yalnızca iyi bir ML modeli kurmaktan daha zordur.

## 3. Accuracy tek başına yeterli değildir

Olasılık tahmin kalitesi önemlidir.

## 4. LogLoss ile ROI farklı şeylerdir

Daha iyi probabilistic prediction doğrudan daha yüksek bahis getirisi anlamına gelmez.

## 5. Küçük bahis örneklemleri yanıltıcı olabilir

Özellikle yüksek oranlı az sayıdaki bahislerde ROI çok değişken olabilir.

## 6. Parametre grid search overfit olabilir

Development'ta en iyi kombinasyonu bulmak, gelecekte de en iyi kombinasyon olacağı anlamına gelmez.

## 7. Negatif sonuç da araştırma sonucudur

Bir modelin marketi yenemediğini göstermek başarısız bir araştırma değildir.

Aksine:

**hangi yaklaşımın işe yaramadığını bilmek, yeni araştırmanın başlangıç noktasıdır.**

---

# 📁 Repository Structure

```
epl-ml-research/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   └── README.md
│
├── docs/
│   ├── methodology.md
│   ├── results.md
│   ├── lessons_learned.md
│   └── glossary.md
│
├── results/
│   ├── figures/
│   └── tables/
│
├── src/
│   └── README.md
│
├── notebooks/
│   └── README.md
│
├── scripts/
│   └── README.md
│
└── tests/
    └── README.md
```

Tarihsel deneylerin doğrulanmış kaynak kodları bu arşive uydurma şekilde yeniden oluşturulmamıştır. Mevcut arşiv yalnızca doğrulanabilen sonuçları ve metodolojiyi içerir.

---

# 🔎 SEO / Research Keywords

Bu repository şu araştırma konularıyla ilgilenenler için hazırlanmıştır:

**Premier League prediction, EPL prediction, football prediction, soccer prediction, football betting analysis, soccer betting analysis, betting machine learning, football machine learning, Premier League machine learning, xG prediction, expected goals, value betting, value bet analysis, betting odds analysis, bookmaker odds, football betting model, sports betting model, football forecasting, Premier League forecasting, 1X2 prediction, match outcome prediction, İddaa tahmin, İddaa analiz, futbol bahis analizi, Premier League bahis analizi, futbol maç tahmini, bahis oranları analizi, value bet, xG bahis analizi.**

---

# ⚖️ Disclaimer

Bu proje **yatırım veya bahis tavsiyesi değildir**.

Geçmiş performans gelecekteki sonuçları garanti etmez.

Buradaki modeller ve sonuçlar yalnızca **istatistiksel / makine öğrenmesi araştırması** amacıyla sunulmaktadır.

Özellikle yüksek ROI gösteren küçük backtest örnekleri, sürdürülebilir kâr garantisi olarak yorumlanmamalıdır.

---

# 🚀 Research Status

**Status: FROZEN**

V7 → V10 → V11-A → V11-C araştırma hattı tamamlanmıştır.

Final OOS testinde market baseline geçilemediği için bu hat üzerinde daha fazla parametre optimizasyonu yapılmayacaktır.

Yeni bir model ancak:

- yeni feature seti,
- yeni veri dönemi,
- ayrı validation protokolü,
- yeni OOS dönemi

ile bağımsız bir araştırma olarak değerlendirilmelidir.

---

## Final Conclusion

Bu projenin amacı **“kesin kazandıran bahis sistemi” bulmak değildi.**

Amaç, makine öğrenmesinin Premier League bahis piyasasında gerçekten ölçülebilir bir avantaj üretip üretemediğini bilimsel olarak test etmekti.

Sonuç:

**Bu araştırmada üretilemedi.**

Ve araştırmanın en önemli sonucu tam olarak budur:

> ### “Modeli marketi yenene kadar zorlamak yerine, marketi yenemediğimizi OOS testleriyle kanıtlayıp araştırmayı durdurduk.”

---

### ⭐ Eğer bu araştırma ilginizi çekiyorsa

Repository'yi inceleyebilir, metodolojiyi takip edebilir ve özellikle **OOS validation, betting market efficiency, xG prediction, value betting ve football machine learning** konularındaki sonuçları kullanabilirsiniz.

**Tahmin etmek kolaydır.  
Tahminin gelecekte de çalıştığını kanıtlamak zordur.**
