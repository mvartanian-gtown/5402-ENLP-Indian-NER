#!/usr/bin/env python3

# import csv
# import os
import re
import sys

from bs4 import BeautifulSoup
import spacy
from spacy.lang.en import English
from spacy.tokens import DocBin


def reformat(text):
    # text = ' '.join(text.split())
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    text = text.replace('"",', " ")
    text = text.replace(",,", " ")
    text = text.replace('\\"', '"')
    text = text.replace("\u2019", "'")  # <E2><80><99>
    text = text.replace("\u201C", '"')  # <E2><80><9C>
    text = text.replace("\u201D", '"')  # <E2><80><9D>
    text = text.replace("\u2016", "'")
    text = text.replace("\u2018", "'")
    text = text.replace("\u2013", "-")
    text = text.replace("\u2014", "-")
    text = text.replace("\u2026", "...")
    text = text.replace(".", " . ")
    text = text.replace(",", " , ")
    text = text.replace("(", " ( ")
    text = text.replace(")", " ) ")
    text = text.replace('"', ' " ')
    text = text.replace("-", " - ")
    text = text.replace(":", " : ")
    text = text.replace(";", " ; ")
    text = text.replace("'", " ' ")
    soup = BeautifulSoup(text).get_text()
    soup = re.sub(r" +", " ", soup)
    soup = re.sub(r"-{3,}", "---", soup)
    soup = re.sub(r"_{3,}", "___", soup)
    # soup = ' '.join(re.findall(r'[.?]|\w+', soup))
    soup = soup[:-16]

    #    print(soup)

    return soup


def main():
    if len(sys.argv) != 2:
        print(f"Usage: bunzip2 -d -c file.csv.gz2 | {__file__} [vocab | docs]")
        return

    mode = sys.argv[1]

    if mode == "read":
        nlp = spacy.blank("en")

        # Load .spacy file
        spacy_file = "./alldocs.spacy"
        doc_bin = DocBin().from_disk(spacy_file)
        docs = list(doc_bin.get_docs(nlp.vocab))

        # Loop through docs and print entities
        for i, doc in enumerate(docs):
            print(f"Document {i+1}:")
            print("Text:", doc.text)
            print("Entities:")
            for ent in doc.ents:
                print(f"  {ent.text} ({ent.label_})")
            print("---")
        return

    vocab = set()
    text = ""
    alldocs = ""
    prev_vocab_len = 0
    doc_count = 0
    for line in sys.stdin:
        if not line.startswith('"') or len(line) < 90:
            text += line
            continue

        # New document
        doc_count += 1
        text = reformat(text)

        if len(text) > 100:
            if mode == "vocab":
                words = text.split(" ")
                vocab.update(words)
                if len(vocab) - prev_vocab_len > 10000:
                    print(
                        f"Docs={doc_count}, vocab length is {len(vocab)}",
                        file=sys.stderr,
                    )
                    prev_vocab_len = len(vocab)

            if mode == "docs":
                alldocs += text

            text = ""

    if mode == "vocab":
        for x in vocab:
            print(x)

    if mode == "docs":
        print(f"Dumping {doc_count} documents to alldocs.spacy", file=sys.stderr)
        print(alldocs)
        nlp = English()
        #        doc = nlp(alldocs)
        #        doc.to_disk("alldocs.spacy")

        k = 10000
        doc_bin = DocBin()
        #        chunks = []
        for i in range(0, len(alldocs), k):
            chunk = alldocs[i : i + k]
            print(f"Wrote chunk of size {k}", file=sys.stderr)
            nlp = English()
            doc = nlp(chunk)
            doc_bin.add(doc)
        # chunks.append(s[i:i+k])
        print(f"Emitting {len(doc_bin)} documents", file=sys.stderr)

        doc_bin.to_disk("./moredocs.spacy")


if __name__ == "__main__":
    main()
