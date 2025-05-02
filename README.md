# 5402-ENLP-Indian-NER
Group 5's final project for COSC 5402 ENLP

# Paper
(Kalamkar et al. 2022) https://arxiv.org/pdf/2211.03442 created a corpus of 16,570 Indian court sentences and preambles and trained a Roberta-based transformer Named Entity Recognizer to emit spans for 14 entity types (COURT, PETITIONER, STATUTE, JUDGE, …). Their data and models are available on the GitHub and Hugging Face websites.

# Unannotated US legal opinions
* https://static.case.law/
* opinions.sample.csv is a small subset, as is the .spacy file
* Originals are very large (~50GB compressed). Takes 2.5 hours to decompress entirely, producing a 259GB file with many opinions.
* Note that legal opinions are in the public domain and therefore **not** [subject to copyright](https://www.supremecourt.gov/opinions/19pdf/18-1150_7m58.pdf)

# Generating alldocs.spacy
```
# Warning 43GB download
$ wget https://storage.courtlistener.com/bulk-data/opinions-2025-03-31.csv.bz2 
$ bunzip2 -d -c opinions-2025-03-31.csv.bz2 | head -n 1000000 | ./opinion_to_spacy.py docs > /dev/null
...
$ ls -l alldocs.spacy

```

 
