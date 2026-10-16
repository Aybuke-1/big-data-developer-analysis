import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Dosya secimi penceresi
root = tk.Tk()
root.withdraw()
print("Lutfen masaustundeki 'temiz_veri.csv' dosyasini secin...")
dosya_yolu = filedialog.askopenfilename(title="temiz_veri.csv dosyasini secin")

if dosya_yolu:
  print("Veri yukleniyor ve grafikler ciziliyor...")
  df = pd.read_csv(dosya_yolu)
  kayit_klasoru = os.path.dirname(dosya_yolu)
  sns.set_theme(style="whitegrid")

  # --- GRAFIK 1: EN COK TERCIH EDILEN OGRENME YONTEMLERI ---
  plt.figure(figsize=(10, 5))
  ogrenme = (
      df["LearnCode"]
      .dropna()
      .str.split(";")
      .explode()
      .str.strip()
      .value_counts()
      .head(6)
  )
  sns.barplot(
      x=ogrenme.values,
      y=ogrenme.index,
      hue=ogrenme.index,
      palette="Blues_r",
      legend=False,
  )
  plt.title(
      "Yazilimcilar Kodlamayi Nasil Ogreniyor? (Top 6)",
      fontsize=13,
      fontweight="bold",
  )
  plt.xlabel("Kisi Sayisi")
  plt.tight_layout()
  g1_yol = os.path.join(kayit_klasoru, "grafik1_ogrenme_yontemleri.png")
  plt.savefig(g1_yol, dpi=200)

  # --- GRAFIK 2: EN COK KAZANDIRAN POPULER DILLER ---
  plt.figure(figsize=(10, 5))
  diller_df = df.dropna(
      subset=["LanguageHaveWorkedWith", "ConvertedCompYearly"]
  ).copy()
  # Noktali virgulle ayrilan dilleri alt alta satirlara ayiriyoruz
  diller_df["Dil"] = diller_df["LanguageHaveWorkedWith"].str.split(";")
  diller_df = diller_df.explode("Dil")
  diller_df["Dil"] = diller_df["Dil"].str.strip()

  populer_diller = (
      diller_df["Dil"].value_counts().head(10).index
  )  # En cok kullanilan ilk 10 dil
  dil_maas = (
      diller_df[diller_df["Dil"].isin(populer_diller)]
      .groupby("Dil")["ConvertedCompYearly"]
      .median()
      .sort_values(ascending=False)
  )

  sns.barplot(
      x=dil_maas.values,
      y=dil_maas.index,
      hue=dil_maas.index,
      palette="Greens_r",
      legend=False,
  )
  plt.title(
      "En Cok Kullanilan Dillerin Medyan Yillik Maasi ($)",
      fontsize=13,
      fontweight="bold",
  )
  plt.xlabel("Yillik Medyan Maas ($)")
  plt.tight_layout()
  g2_yol = os.path.join(kayit_klasoru, "grafik2_en_cok_kazandiran_diller.png")
  plt.savefig(g2_yol, dpi=200)

  # --- GRAFIK 3: AI KULLANIMI VE MAAS ILISKISI ---
  plt.figure(figsize=(8, 5))
  ai_df = df.dropna(subset=["AISelect", "ConvertedCompYearly"]).copy()
  ai_maas = (
      ai_df.groupby("AISelect")["ConvertedCompYearly"]
      .median()
      .sort_values(ascending=False)
  )

  sns.barplot(
      x=ai_maas.index,
      y=ai_maas.values,
      hue=ai_maas.index,
      palette="Oranges_r",
      legend=False,
  )
  plt.title(
      "Yapay Zeka (AI) Kullanimi ve Medyan Maas ($)",
      fontsize=13,
      fontweight="bold",
  )
  plt.ylabel("Yillik Medyan Maas ($)")
  plt.xlabel("Is Akisinda AI Kullaniyor mu?")
  plt.tight_layout()
  g3_yol = os.path.join(kayit_klasoru, "grafik3_ai_kullanimi_ve_maas.png")
  plt.savefig(g3_yol, dpi=200)

  print("\n" + "=" * 50)
  print("GRAFIKLER BASARIYLA CIZILDI VE KAYDEDILDI!")
  print("=" * 50)
  print(f"1. {g1_yol}")
  print(f"2. {g2_yol}")
  print(f"3. {g3_yol}")
  print("=" * 50)
  plt.show()
