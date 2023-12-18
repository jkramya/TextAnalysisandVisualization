import re
from collections import Counter
import matplotlib.pyplot as plt

def clean_text(text):
    # Remove punctuation and numbers, convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()

def word_frequency(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    return Counter(words)

def most_common_words(text, n):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

def plot_word_frequency(word_freq):
    words, frequencies = zip(*word_freq)
    plt.bar(words, frequencies)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Most Common Words')
    plt.xticks(rotation=45, ha='right')
    plt.show()

if __name__ == "__main__":
    # Read text from a file
    file_path = "sample_text.txt"  # Change to the path of your text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Word frequency analysis
    word_freq_dict = word_frequency(text_content)

    # Top 10 most common words
    top_words = most_common_words(text_content, 10)

    # Display results
    print("Word Frequency Dictionary:")
    print(word_freq_dict)

    print("\nTop 10 Most Common Words:")
    for word, freq in top_words:
        print(f"{word}: {freq}")

    # Plotting the word frequency
    plot_word_frequency(top_words)
