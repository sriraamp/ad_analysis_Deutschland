<h2 id="lang-toggle">Language: <button onclick="toggleLanguage()">🇬🇧 EN / 🇩🇪 DE</button></h2>

<div id="english-section">

## German Advertising Analysis (2019–2024)

This is a synthetic data project that simulates analysis of the 1,000 most advertised campaigns in Germany over the past five years. The goal is to explore what trends dominate German advertising: who advertises the most, which platforms they use, which celebrities show up, and what language they use to sell.

### Project Objectives

- Identify which brands dominate the ad space
- Understand which platforms are preferred across industries
- Map celebrity endorsements by brand
- Analyze ad copy for patterns in tone and language
- Build a clean, interactive dashboard to explore the data

### Key Insights

**Platforms:** YouTube and Instagram dominate. TikTok is growing, but TV is still used by legacy brands like Mercedes.

**Brands:** Lidl, Edeka, Nike, Adidas, and Volkswagen appear the most.

**Celebrities:** Florian David Fitz, Lena Meyer-Landrut, Joko Winterscheidt, Helene Fischer, Manuel Neuer, Palina Rojinski, and Elyas M’Barek.

**Celebrity–Brand Mapping:** See heatmap in visuals.

**Ad Copy:** Common words include “entdecke”, “frisch”, “vielfalt”, “zukunft”. Tone is lifestyle-oriented, fresh, optimistic.

### How to Run

```bash
git clone https://github.com/sriraamp/ads-analysis-germany.git
cd ads-analysis-germany

pip install -r requirements.txt
streamlit run app.py

ads_analysis_germany/
├── data/
├── notebooks/
├── src/
├── visuals/
├── app.py
└── requirements.txt
