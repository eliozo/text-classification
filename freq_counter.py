import re
import nltk
from collections import Counter

def normalize_text(text):
	text = text.lower()
	text = re.sub(r"\d+", "100", text)

	return text.strip()

def count_words_between_body_tags(file_path):
    word_counts = Counter()
    pattern = r'<BODY>(.*?)</BODY>'

    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            # words = re.findall(r'\b\w+\b', match)
            # text = match.group(1)
            
            words = nltk.word_tokenize(normalize_text(match))
            word_counts.update(words)

    return word_counts

# def write_word_counts_to_file(word_counts, output_file_path):
#    with open(output_file_path, 'w') as file:
#        for word, count in word_counts.items():
#            file.write(f'{count}\t{word}\n')

def write_word_counts_to_file(word_counts, output_file_path):
    sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))

    with open(output_file_path, 'w') as file:
        for word, count in sorted_counts:
            file.write(f'{count}\t{word}\n')


def main():

    # Usage example:
    for i in range(0,22):
        input_file_path = 'reut2-{:03}.sgm'.format(i)
        print(input_file_path)
    # input_file_path = 'reut2-000.sgm'
    output_file_path = 'output_freq.tsv'

    word_counts = count_words_between_body_tags(input_file_path)
    write_word_counts_to_file(word_counts, output_file_path)
    
if __name__ == '__main__':
    main()

