# Text Generation Model Evaluation using TOPSIS

## Overview

This project aims to assess the performance of various text generation models using the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. Evaluating models based on multiple criteria such as accuracy, F1 Score, precision, and recall provides a comprehensive understanding of their effectiveness in generating high-quality text.

## Model Ranking Table

The table below displays the model ranking based on key evaluation metrics:

```markdown
| Rank | Model                    | Accuracy | F1_Score | Precision | Recall |
|------|---------------------------|----------|----------|-----------|--------|
| 1.0  | distilbert-base-uncased   | 0.88     | 0.91     | 0.89      | 0.90   |
| 2.0  | roberta-base              | 0.87     | 0.90     | 0.88      | 0.89   |
| 3.0  | t5-base                   | 0.89     | 0.92     | 0.91      | 0.80   |
| 4.0  | electra-base              | 0.86     | 0.89     | 0.87      | 0.88   |
| 5.0  | bert-base-uncased         | 0.85     | 0.89     | 0.88      | 0.87   |
| 6.0  | gpt2                      | 0.82     | 0.87     | 0.85      | 0.84   |
