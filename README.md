# German Advertising Analysis (2019–2024)

This is a synthetic data project that simulates analysis of the 1,000 most advertised campaigns in Germany over the past five years. The goal is to explore what trends dominate German advertising: who advertises the most, which platforms they use, which celebrities show up, and what language they use to sell.

## Project Objectives

- Identify which brands dominate the ad space
- Understand which platforms are preferred across industries
- Map celebrity endorsements by brand
- Analyze ad copy for patterns in tone and language
- Build a clean, interactive dashboard to explore the data

## Core Findings

### Platforms
YouTube and Instagram dominate. TikTok is picking up, but still not mainstream. TV is used mostly by established players like Mercedes.

### Brands
Top brands by frequency:
- Lidl
- Edeka
- Nike
- Adidas
- Volkswagen

These brands appear across multiple platforms, often with a recurring tone of affordability, lifestyle, or innovation.

### Celebrities
Most featured public figures:
- Florian David Fitz
- Lena Meyer-Landrut
- Joko Winterscheidt
- Helene Fischer
- Manuel Neuer
- Palina Rojinski
- Elyas M'Barek

Their presence often overlaps with major consumer brands or auto companies. There's a pattern of consistency—brands tend to reuse familiar faces.

### Celebrity–Brand Map
A heatmap in the visuals folder breaks this down. Example:

- **Fitz → Lidl, Telekom**
- **Meyer-Landrut → Nike, Adidas**
- **Neuer → McDonald's, Volkswagen**
- **Rojinski → Hornbach, Edeka**

### Ad Copy
Common themes in scripts:
- Experience, freshness, local/regional quality
- Forward-looking language (e.g., "Zukunft", "Projekt")
- Words like “entdecke”, “genial”, “vielfalt” occur frequently

Typical tone = lifestyle + optimism.

## How to Run

```bash
git clone https://github.com/sriraamp/ads-analysis-germany.git
cd ads-analysis-germany

pip install -r requirements.txt
streamlit run app.py
