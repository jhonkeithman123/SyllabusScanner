def clean_text(raw_text):
    # Remove unwanted characters and whitespaces
    cleaned_text = ' '.join(raw_text.split())
    return cleaned_text

def remove_stopwords(text, stopwords):
    # Remove stopwords from the text
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(filtered_words)

def  preprocess_text(raw_text, stopwords):
    # Clean and preprocess the text
    cleaned_text = clean_text(raw_text)
    return remove_stopwords(cleaned_text, stopwords)