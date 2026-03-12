from collections import Counter

def word_frequency_analysis(text):
    words = text.lower().split()  
    freq = Counter(words)
    total_words = len(words)
    top5 = freq.most_common(5)
    top5_count = sum(count for word, count in top5)
    proportion = (top5_count / total_words) * 100 if total_words > 0 else 0
    print("Top 5:", dict(top5))
    print("Total number of words:", total_words)
    print(f"Proportion of 5 most common words: {top5_count} / {total_words} = {proportion:.2f}%")




# Test funtion... | 0...0 |
text = "i am cao phong.I am now attending class TEC001.TEC001 is a very good class."
word_frequency_analysis(text)



