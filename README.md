
# Spam Email Classifier using Naive Bayes Algorithm

This repository contains Python code that demonstrates the process of building a simple spam email classifier using the Naive Bayes algorithm. The classifier is designed to distinguish between spam and non-spam (ham) emails based on their text content.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example Emails](#example-emails)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Spam emails are a common nuisance in our inboxes. This project aims to develop a basic spam email classifier using the Naive Bayes algorithm. The classifier processes email text data, converts it into numerical feature vectors, and trains a model to make predictions.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have the required libraries installed. You can install them using:
   ```
   pip install pandas scikit-learn
   ```
3. Place your email dataset in the appropriate directory (e.g., `data/spam.csv`).
4. Open the Jupyter Notebook or Python script provided in the repository.

## Usage

The main steps in the provided code include:

1. Loading the email data using pandas.
2. Preprocessing the data, including encoding labels and splitting into training and testing sets.
3. Converting email text into numerical feature vectors using CountVectorizer.
4. Training a Multinomial Naive Bayes model on the training data.
5. Evaluating the model's accuracy on the testing data.

## Example Emails

The code provides two example emails in the `Email` list. You can modify or extend this list to test the classifier with different emails.

## Results

The code outputs the following results:

- Descriptive statistics about the data (grouped by 'Category').
- Accuracy score of the Naive Bayes model on the testing data.
- Accuracy score using a pipeline that includes both data transformation and model training.

Feel free to modify the code, experiment with different preprocessing techniques, or try other machine learning algorithms to potentially improve the classifier's performance.

## Contributing

If you'd like to contribute to this project, you can:

- Submit bug reports or feature requests by opening an issue.
- Fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).

