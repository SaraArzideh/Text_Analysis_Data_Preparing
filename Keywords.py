import nltk
import pandas as pd
from nltk.tokenize import word_tokenize, RegexpTokenizer, MWETokenizer
from nltk.corpus import stopwords
from collections import Counter, defaultdict
import string

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')


# Load the data
data_file = 'ScopusSourceUse.xlsx'  # path to data file
thesaurus_file = 'Thesaurus.xlsx' # path to thesaurus file

# Read the Excel file
df = pd.read_excel(data_file)
thesaurus_df = pd.read_excel(thesaurus_file)

# Extract the relevant columns
texts = df['Abstract'].astype(str) + ' ' + df['Title'].astype(str) + ' ' + df['Author Keywords'].astype(str)

# Ensure that 'Author Keywords' are strings and not NaN
df['Author Keywords'] = df['Author Keywords'].fillna('').astype(str)

# Tokenization and counting with compound words
tokenizer = RegexpTokenizer(r'\b\w[\w-]*\w\b') # Tokenizer that includes hyphens
stop_words = set(stopwords.words('english'))

# Tokenize and filter stopwords
words = tokenizer.tokenize(' '.join(texts).lower())
words = [word for word in words if word not in stop_words and word.isalpha()]

# Count the frequency of each word
word_counts = Counter(words)

# Clean the data using the thesaurus
for index, row in thesaurus_df.iterrows():
    if row['Label'] in word_counts:
        word_counts[row['Replace by']] += word_counts.pop(row['Label'])

# Build a Co-occurrence Matrix:
# For each word in "Author Keywords", track the frequency of other words
# appearing in the same abstract, title, or keyword list.

# Co-occurrence analysis
co_occurrences = defaultdict(Counter)
author_keywords = df['Author Keywords'].str.lower().str.split(';')

for keywords, text in zip(author_keywords, texts):
    if keywords is not None:
        keywords = [kw.strip() for kw in keywords]
        text_words = set(tokenizer.tokenize(text.lower()))
        for keyword in keywords:
            for word in text_words:
                if word != keyword and word.isalpha():
                    co_occurrences[keyword][word] += 1


# Save the cleaned data
cleaned_counts_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
cleaned_counts_df.to_excel('cleaned_word_counts.xlsx', index=False)

# Save the co-occurrence data
co_occurrence_df = pd.DataFrame([{'Keyword': k, 'Co-occurring Word': ck, 'Frequency': cf} 
                                for k, c in co_occurrences.items() 
                                for ck, cf in c.items()])
filtered_co_occurrence_df= co_occurrence_df[co_occurrence_df['Frequency']>=10]
filtered_co_occurrence_df.to_csv('filtered_co_occurrence_data.csv', index=False)

# Analyze relationships and categorize
