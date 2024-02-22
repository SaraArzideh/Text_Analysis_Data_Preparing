import pandas as pd

# Load data
co_occurrence_df = pd.read_csv('filtered_co_occurrence_data.csv')

# List of words to exclude
exclude_words = {"the", "days", "might", "usually", "people", "health", "diseases", 
                 "nurse", "hospital", "alcohol", "Wi-Fi", "student", 
                 "mobile health", "e-health", "health information systems", ...}

# Normalization mappings
normalization_map = {
    "user center design": "user-centered design",
    "user centered design": "user-centered design",
    "user-center design": "user-centered design",
    "access to health care": "access to healthcare",
    "behaviour change": "behavior change",
    "health outcome": "health outcomes",
    "tam": "technology acceptance model",
    # more mappings
}

# Function to normalize words
def normalize_word(word):
    return normalization_map.get(word, word)

# Filter and normalize words
co_occurrence_df['Co-occurring Word'] = co_occurrence_df['Co-occurring Word'].apply(lambda x: normalize_word(x))
co_occurrence_df = co_occurrence_df[~co_occurrence_df['Co-occurring Word'].isin(exclude_words)]
co_occurrence_df = co_occurrence_df[co_occurrence_df['Co-occurring Word'].str.len() >= 3]

# Remove duplicates
co_occurrence_df = co_occurrence_df.drop_duplicates()

# Categorization
category_map = {
    "user-centric design": ["user-centered care", "human-computer interaction","user prticipation", "user center", "human factors", ...],
    "usability": ["usability", "usability testing", "usability assessment", "usability evaluation", "user experience", "perceived ease of use", "perceived usefulness", ...],
    "utility": ["utility", "technology acceptance", "technology adoption", "technology adaptation", ...],
    "sustainable development": ["sustainability", "accessibility", "digital divide", "healthcare disparities", "digital health literacy", "health literacy", ...],
    "ethical consideration": ["privacy", "security", ...],
}

def categorize_word(word):
    for category, keywords in category_map.items():
        if word in keywords:
            return category
    return "Other"

co_occurrence_df['Category'] = co_occurrence_df['Co-occurring Word'].apply(categorize_word)

# Save the cleaned and categorized data
co_occurrence_df.to_csv('categorized_co_occurrence_data.csv', index=False)
