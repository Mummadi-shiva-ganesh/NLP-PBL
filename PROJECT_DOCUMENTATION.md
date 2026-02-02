# Context-Aware Sentiment Classification using BERT

## Problem Statement
Traditional sentiment analysis models often fail to capture the context of words in a sentence. For example, the word "cold" can be positive in "This drink is cold" but negative in "The service was cold." Understanding language contextually is critical for accurate sentiment classification in complex datasets like IMDb reviews or Twitter feeds.

## Objectives
- Implement a sentiment classification pipeline using the BERT architecture.
- Demonstrate context-aware tokenization using `bert-base-uncased`.
- Load and configure a pre-trained `BertForSequenceClassification` model for binary sentiment analysis.
- Provide a clear methodology for transforming raw text into sentiment labels.

## BERT Architecture in Simple Terms
BERT (Bidirectional Encoder Representations from Transformers) is like a student who reads an entire sentence at once, rather than word-by-word from left to right.
- **Bidirectional**: It looks at the words before and after a specific word to understand its meaning.
- **Encoder**: It converts text into a dense mathematical representation (numbers) that captures meaning.
- **Attention Mechanism**: It focuses on the most important words in a sentence to determine sentiment.

## Dataset Description (IMDb)
- **Source**: IMDb Movie Reviews.
- **Samples**: 50,000 highly polar movie reviews.
- **Labels**: 2 (Positive and Negative).
- **Split**: 25,000 for training, 25,000 for testing (balanced).

## Methodology Flow
1. **Text**: Raw movie review (e.g., "The acting was superb!").
2. **Tokenizer**: BERT Tokenizer converts text into tokens and adds special tokens like `[CLS]` and `[SEP]`.
3. **BERT Model**: The processed tokens are fed into the BERT model.
4. **Classification Head**: A linear layer on top of BERT produces the final sentiment score.
5. **Output**: Label (Positive/Negative).

## Current Status
- [x] Project structure defined.
- [x] Documentation completed.
- [x] Requirements listed.
- [/] Sample code implementation.
