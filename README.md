# Keyword Analysis and Data Cleansing 🔍

This repository contains Python scripts for analyzing and cleansing keyword co-occurrence data. The goal is to process textual data, perform co-occurrence analysis, and categorize keywords into meaningful categories for insights.

<img src="https://github.com/user-attachments/assets/21d05159-17eb-43f5-9d98-db6891259280" alt="Python Practice" width="300"/>

---

## 📂 Repository Contents

### 1. **`Keywords.py`**
- Extracts, cleans, and analyzes co-occurrence of keywords from textual data (Papers' abstracts, titles, and author keywords).
- **Features:**
  - Tokenization and stopword filtering.
  - Keyword normalization using a thesaurus.
  - Co-occurrence matrix creation.
  - Output: `cleaned_word_counts.xlsx`, `filtered_co_occurrence_data.csv`.

### 2. **`Cleansingdata.py`**
- Cleans and categorizes co-occurrence data.
- **Features:**
  - Removes irrelevant keywords and duplicates and merges different spelling.
  - Normalizes keywords using a predefined mapping.
  - Categorizes keywords into predefined themes.
  - Output: `categorized_co_occurrence_data.csv`.

---

## 🧰 Tools and Libraries
- Python
- NLTK
- Pandas
- Collections (for efficient data processing)

---

## 📦 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
