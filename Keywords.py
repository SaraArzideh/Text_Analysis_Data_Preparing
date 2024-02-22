import nltk
nltk.download('punkt')
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Load the data
data_file = 'ScopusSourceUse.xlsx'  # path to data file
thesaurus_file = 'Thesaurus.xlsx' # path to thesaurus file

# Read the Excel file
df = pd.read_excel(data_file)
thesaurus_df = pd.read_excel(thesaurus_file)

# Extract the relevant columns
texts = df['Abstract'].astype(str) + ' ' + df['Title'].astype(str) + ' ' + df['Author Keywords'].astype(str)

# Tokenization and counting
stop_words = set(stopwords.words('english'))
words = word_tokenize(' '.join(texts).lower())
words = [word for word in words if word not in stop_words and word.isalpha()]

# Count the frequency of each word
word_counts = Counter(words)

# Clean the data using the thesaurus
for index, row in thesaurus_df.iterrows():
    if row['Label'] in word_counts:
        word_counts[row['Replace by']] += word_counts.pop(row['Label'])

# Save the cleaned data
cleaned_counts_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
cleaned_counts_df.to_excel('cleaned_word_counts.xlsx', index=False)

# Analyze relationships and categorize
