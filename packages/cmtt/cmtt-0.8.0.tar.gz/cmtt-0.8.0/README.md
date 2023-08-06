[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<div>
<img width="600px" height="180px" src= "https://user-images.githubusercontent.com/76529011/185376373-787f65d5-b78b-4f11-a7fb-e9aa19dc3a04.png">
</div>

-----------------------------------------
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)![Compatibility](https://img.shields.io/badge/compatible%20with-python3.9.x-blue.svg)

CMTT is a wrapper library that makes code-mixed text processing more efficient than ever. More documentation incoming!
 
## Installation
```
pip install cmtt
```

## Getting Started
How to use this library:

```Python
from cmtt.data import *
from cmtt.preprocessing import *

# Loading json files
result_json = load_url('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')

# Loading csv files
result_csv = load_url('https://gist.githubusercontent.com/rnirmal/e01acfdaf54a6f9b24e91ba4cae63518/raw/b589a5c5a851711e20c5eb28f9d54742d1fe2dc/datasets.csv')

# List the key properties available for the datasets provided by the cmtt library
keys = list_dataset_keys()

# List all datasets provided by cmtt based on search_key and search_term
data = list_cmtt_datasets(search_key="task", search_term = "ner", isPrint=True)

# Download multiple datasets provided by cmtt, returning a list of paths where the datasets get downloaded
# The Datasets are downloaded into a new 'cmtt' directory inside the user profile directory of the operating system
lst = download_cmtt_datasets(["linc_ner_hineng", "L3Cube_HingLID_all", "linc_lid_spaeng"])

# Download a dataset from a url, returning the path where the dataset gets downloaded
# The Dataset is downloaded into a new directory 'datasets' inside the current working directory
path = download_dataset_url('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')

# Whitespace Tokenizer
text = "Hello world! This is a python code. Adding random words activate code decrease wastage."
WhitespaceT = WhitespaceTokenizer()
tokenized_text_whitespace = WhitespaceT.tokenize(text)

# Word Tokenizer
WordT = WordTokenizer(do_lower_case=False)
tokenized_text_word = WordT.tokenize(text)

# Wordpiece Tokenizer
WordpieceT = Wordpiece_tokenizer()
tokenized_text_wordpiece  = WordpieceT.tokenize(text)

# Devanagari Tokenizer
devanagari_text = "मैं इनदोनों श्रेणियों के बीच कुछ भी० सामान्य नहीं देखता। मैं कुछ नहीं, ट ट॥"
DevanagariT = DevanagariTokenizer()
tokenized_text_devanagari_words  = DevanagariT.word_tokenize(devanagari_text)
tokenized_text_devanagari_characters  = DevanagariT.character_tokenize(devanagari_text)

# DeTokenizers
whitespace_text = WhitespaceT.detokenize(tokenized_text_whitespace)
word_text = WordT.detokenize(tokenized_text_word)
wordpiece_text = WordpieceT.detokenize(tokenized_text_wordpiece)
devanagari_text = DevanagariT.word_detokenize(tokenized_text_devanagari_words)

# Search functionality
instances, list_instances = search_word(text, 'this', tokenize = True, width = 3)

# Sentence piece based tokenizers for Hindi, Hinglish, English and Devnagari Hindi and Roman English Text
# Download the models for the tokenizers. If already downloaded then cmtt does not download it again.
download_model('hi')
download_model('hi-en')
download_model('en')
download_model('hinDev_engRom')

# Sentence piece based Tokenizer for English
_en = " This is a sentence-piece based tokenizer, supporting the english language."
Spm_en = Sentencepiece_tokenizer('en')
lst = Spm_en.tokenize(_en)
with open(r"test_en.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")

# Sentence piece based Tokenizer for Hindi
_hi = " मैं इनदोनों श्रेणियों के बीच कुछ भी० सामान्य नहीं देखता।"
Spm_hi = Sentencepiece_tokenizer('hi')
lst = Spm_hi.tokenize(_hi)
with open(r"test_hi.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")

# Sentence piece based Tokenizer for Hinglish
_hien = " hi kya haal chaal? hum cmtt naamkaran ki python library develop kar rahe hain"
Spm_hien = Sentencepiece_tokenizer('hi-en')
lst = Spm_hien.tokenize(_hien)
with open(r"test_hien.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")

# Sentence piece based Tokenizer for Devnagari Hindi and Roman English Mixed Text
_hinDev_engRom = " कैसे हो मित्र? How are you? I am good."
Spm_hien = Sentencepiece_tokenizer('hinDev_engRom')
lst = Spm_hien.tokenize(_hinDev_engRom)
with open(r"test_hinDev_engRom.txt", 'w', encoding = "utf-8") as f:
  for i in lst:
    f.write(i + "\n")

# Sentence Piece detokenizer
path = os.path.dirname(os.path.realpath(__file__))
f = open(os.path.join(path, "test_hien.txt"), encoding = "utf-8")
tokens = []
with f as reader:
  while True:
    token = reader.readline()
    if not token:
      break
    token = token.strip()
    tokens.append(token)
detokenized_text = Spm_hien.detokenize(tokens)

# Stemmer for English words
stemmer = PorterStemmer()
stemming = stemmer.stem("activate")
```

## Contributors
- [Paras Gupta](https://github.com/paras-gupt)
- [Tarun Sharma](https://github.com/tarun2001sharma)
- [Reuben Devanesan](https://github.com/Reuben27)