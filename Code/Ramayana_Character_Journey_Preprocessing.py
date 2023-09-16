import re
import nltk
from nltk.tokenize import sent_tokenize
# # Download the NLTK sentence tokenizer if you haven't already
# nltk.download('punkt')
# Specify the path to your .txt file
file_path = 'Ramayana.txt'
# Read the content from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Split the text into sentences using regular expressions
# sentences = re.split(r'\.\s+', text.strip())
sentences = sent_tokenize(text)

# Remove empty sentences and extra whitespace
# sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
# sentences = sentences[131:7178]
sentences = sentences[95:8213]
# for i, sentence in enumerate(sentences, start=1):
#     print(f"Sentence {i}: {sentence}")

def regex_clean(sentences):
    sentences = [re.sub('\[(.*)\]', ' ', x) for x in sentences]
    sentences = [re.sub('\[(.*)\.', ' ', x) for x in sentences]
    sentences = [re.sub('\(', ' ', x) for x in sentences]
    sentences = [re.sub('\)', ' ', x) for x in sentences]
    sentences = [re.sub('[wW]anna', 'want to ', x) for x in sentences]
    sentences = [re.sub('[gG]onna', 'going to ', x) for x in sentences]
    sentences = [re.sub('[gG]otta', 'have to ', x) for x in sentences]
    sentences = [re.sub("\'em", ' them ', x) for x in sentences]
    sentences = [re.sub("\'ll", ' will ', x) for x in sentences]
    sentences = [re.sub("\'head", 'ahead ', x) for x in sentences]
    sentences = [re.sub("\'bout", 'about ', x) for x in sentences]
    sentences = [re.sub('[wW]hatcha', 'what are you ', x) for x in sentences]
    sentences = [re.sub('[tT]ryna', 'trying to ', x) for x in sentences]
    sentences = [re.sub("\'[cC]ause", " because ", x) for x in sentences]
    sentences = [re.sub("\'[rR]ound", "around ", x) for x in sentences]
    sentences = [re.sub("ain't", "am not ", x) for x in sentences]
    sentences = [re.sub("in\'(\s|\,|\.|\?)", "ing ", x) for x in sentences]
    sentences = [re.sub("on\'(\s|\,|\.|\?)", "oing to ", x) for x in sentences]
    sentences = [re.sub("o\'s", "o is ", x) for x in sentences]
    sentences = [re.sub("\'re", " are ", x) for x in sentences]
    sentences = [re.sub("\'ve", " have ", x) for x in sentences]
    sentences = [re.sub("\'d", " would ", x) for x in sentences]
    sentences = [re.sub("\'(m|ma)", " am ", x) for x in sentences]
    sentences = [re.sub('\?(\s*)\.', '? ', x) for x in sentences]
    sentences = [re.sub('\,(\s*)\.', ', ', x) for x in sentences]
    sentences = [re.sub('\.(\s*)\.', '. ', x) for x in sentences]
    sentences = [re.sub('\.(\s*)\.', '. ', x) for x in sentences]
    sentences = [re.sub('\.(\s*)\.', '. ', x) for x in sentences]
    sentences = [re.sub("\'", " ", x) for x in sentences]
    pattern = r'\d+\s*\d*\s*RAAMAAYANA'
    sentences = [re.sub(pattern, ' ', x) for x in sentences]
    sentences = [re.sub(r'CHAPTER [IVXLCDM]+', ' ', x) for x in sentences]
    sentences = [re.sub(r'[A-Z\s]+\n', ' ', x) for x in sentences]
    sentences = [re.sub(r'(.*[a-z])[\s,]*$', r'\1. ', x) for x in sentences]
    sentences = [re.sub(r'([a-z])([A-Z])', r'\1 \2', x) for x in sentences]
    sentences = [re.sub("\s*•\s*|\s*¬\s*|-\s+", "", x) for x in sentences]
    sentences = [re.sub(r'(\D)(\d+)|(\d+)(\D)|(\d+)', r'\1 \3', x) for x in sentences]
    sentences = [re.sub(r'(\s*\d+)(\'?)(\w+)', r'\2\3', x) for x in sentences]
    sentences = [re.sub(r'(\s*\d+)(\‘?)(\w+)', r'\2\3', x) for x in sentences]
    sentences = [re.sub(r'([.,!?;:"\'\(\)\[\]{}]+)(\w)',r'\1 \2', x) for x in sentences]
    sentences = [re.sub(r'%',' ', x) for x in sentences]
    sentences = [re.sub(r'\s+', ' ', x) for x in sentences]


    return sentences

# sentences = regex_clean(sentences)
sentences = regex_clean(sentences)
sentences = [sentence.strip() for sentence in sentences]
# corpus = ". ".join(sentences)
# Print the list of sentences
for i, sentence in enumerate(sentences, start=1):
    print(f"Sentence {i}: {sentence}")
# print(len(sentences))
# print(sentences[6889])


import pandas as pd
# Create a DataFrame from your list of sentences
df = pd.DataFrame({'Sentences': sentences})
# Define the file paths for text and Excel files
text_file_path = 'CleanedRamayana.txt'
excel_file_path = 'CleanedRamayana.xlsx'

# Save the list of sentences to a text file
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    for sentence in sentences:
        text_file.write(sentence + '\n')
# Save the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False, engine='openpyxl')
print("Text file and Excel file saved successfully.")
