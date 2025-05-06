# 5402-ENLP-Indian-NER
Group 5's final project for COSC 5402 ENLP

# Paper
(Kalamkar et al. 2022) https://arxiv.org/pdf/2211.03442 created a corpus of 16,570 Indian court sentences and preambles and trained a Roberta-based transformer Named Entity Recognizer to emit spans for 14 entity types (COURT, PETITIONER, STATUTE, JUDGE, …). Their data and models are available on the GitHub and Hugging Face websites.

# Unannotated US legal opinions
* https://static.case.law/
* opinions.sample.csv is a small subset, as is the .spacy file
* Originals are very large (~50GB compressed). Takes 2.5 hours to decompress entirely, producing a 259GB file with many opinions.
* Note that legal opinions are in the public domain and therefore **not** [subject to copyright](https://www.supremecourt.gov/opinions/19pdf/18-1150_7m58.pdf)

# Generating unannotated legal documents in spaCy format
```
# Warning 43GB download
$ wget https://storage.courtlistener.com/bulk-data/opinions-2025-03-31.csv.bz2 
$ bunzip2 -d -c opinions-2025-03-31.csv.bz2 | head -n 1000000 | ./opinion_to_spacy.py docs > /dev/null
...
$ ls -l alldocs.spacy

```

# Baseline Model
Due to size issues with GitHub, our models can be found at https://github.com/peterngng/AI_NER-main

# 📦 Testing the Baseline Model

## 1. Install the pre-trained baseline model

```bash
pip install -r requirements.txt
```

```bash
pip install https://huggingface.co/opennyaiorg/en_legal_ner_trf/resolve/main/en_legal_ner_trf-3.2.0-py3-none-any.whl
```

## 2. Run the baseline model

```bash
python run_legal_ner.py
```

This script will run the baseline model and display the output in your browser for easy visualization of the extracted entities.

---

# 🛠 Using the Designed Model

Our designed model is located in the `training` folder and includes the best-trained configuration for improved performance.

## Components

- `best_model`: The best-trained version of the custom model.
- `train2.py`: Script to train the model using provided datasets.
- `pred.py`: Script to predict legal entities from documents.
- `evaluate2.py`: Script to evaluate the model and calculate performance metrics.
- `check.py` and `check_label.py`: Scripts to ensure data integrity and validate dataset labels.

---

# 🚀 Steps to Use the Designed Model

## 1. Train the Model

Use `train2.py` to train the model with your dataset:

```bash
python ./training/train2.py
```

## 2. Make Predictions

Use `pred.py` to predict legal entities on new documents:

```bash
python ./training/pred.py
```

## 3. Evaluate the Model

Run `evaluate2.py` to calculate accuracy, precision, recall, and other performance metrics:

```bash
python ./training/evaluate2.py
```

## 4. Check Data Integrity

Use `check.py` and `check_label.py` to verify the integrity of your dataset:

```bash
python ./training/check.py
python ./training/check_label.py
```

---

## 📚 Repository Reference

This project is based on the open-source work available at the [Legal NER GitHub Repository](https://github.com/Legal-NLP-EkStep/legal_NER?tab=readme-ov-file).

---

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

```plaintext
MIT License

Copyright (c) 2025 Peter Ng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
 
