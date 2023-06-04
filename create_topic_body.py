import re

def extract_topic_body(input_file_path, output_file_path):
    categories = {"earn", "acquisitions", "money-fx", "grain", "crude", "trade", "interest", "ship", "wheat", "corn"}
    pattern = r'<TOPICS>(.*?)</TOPICS>.*?<BODY>(.*?)</BODY>'
    # pattern = r'<REUTERS[^<>]*LEWISSPLIT="TRAIN"[^<>]*><DATE>[^<>]*</DATE><TOPICS>(.*?)</TOPICS>.*?<BODY>(.*?)</BODY>'
    # pattern = r'<REUTERS[^>]*?LEWISSPLIT="TRAIN"[^>]*?><DATE>.*?</DATE><TOPICS>(.*?)</TOPICS>.*?<BODY>(.*?)</BODY>'
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'a') as output_file:
        content = input_file.read()
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            topics = re.findall(r'<D>(.*?)</D>', match[0])
            body = match[1].replace('\n', ' ')
            body = normalize_text(body)

            for topic in topics:
                if topic in categories:
                    output_file.write(f'{topic}\t{body}\n')

def normalize_text(text):
	text = text.lower()
	text = re.sub(r"\d+", "100", text)

	return text.strip()

def main():

    output_file_path = 'all_ten_categories.tsv'

    # Usage example:
    for i in range(0,22):
        input_file_path = 'reut2-{:03}.sgm'.format(i)
        print(input_file_path)

        extract_topic_body(input_file_path, output_file_path)
    
if __name__ == '__main__':
    main()
