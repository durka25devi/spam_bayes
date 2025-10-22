
Spam Detection using Naive Bayes

This project demonstrates how to build a Spam Detection Model using Python and Machine Learning.
The model classifies text messages (SMS) as Spam or Ham (Not Spam) using the Multinomial Naive Bayes algorithm and the CountVectorizer for feature extraction.

🧠 Project Overview

Spam messages are a common problem in today’s communication systems.
This project uses the SMS Spam Collection Dataset, which contains labeled text messages —
ham for non-spam and spam for spam.

⚙️ Technologies Used

Python 3

Pandas – for data manipulation

scikit-learn (sklearn) – for ML model building

train_test_split – split dataset

CountVectorizer – convert text to numerical features

MultinomialNB – Naive Bayes classifier

accuracy_score, confusion_matrix, classification_report – evaluation metrics

📂 Dataset

File: spam.csv

The dataset includes two columns:

v1: Label (ham or spam)

v2: Message text

🧩 How It Works
1️⃣ Load Dataset

The dataset is read using pandas.read_csv() with Latin-1 encoding.

2️⃣ Preprocessing

Keep only v1 and v2 columns.

Rename columns to label and message.

Convert labels to numeric form (ham → 0, spam → 1).

3️⃣ Train-Test Split

Data is split into training (80%) and testing (20%) sets.

4️⃣ Text Vectorization

CountVectorizer transforms text into a bag-of-words representation, ignoring English stopwords.

5️⃣ Model Training

The MultinomialNB classifier is trained on the vectorized training data.

6️⃣ Prediction and Evaluation

The model predicts on test data and is evaluated using:

Accuracy Score

Confusion Matrix
