# 😊 Emotion Detection Using Machine Learning

A machine learning-based NLP project that predicts the emotion expressed in a given text. The project uses text preprocessing and feature extraction to classify input text into different emotion categories.

## 📌 Project Overview

The **Emotion Detection System** analyzes a user's text and predicts the underlying emotion using a trained machine learning model.

The project demonstrates the application of **Natural Language Processing (NLP)** and **Machine Learning** for text classification.

## 🚀 Features

* 📝 Accepts user text as input
* 🔤 Converts text into numerical features using **Count Vectorization**
* 🤖 Uses a trained machine learning classification model
* 😊 Predicts the emotion associated with the input text
* 🌐 Interactive interface built using **Streamlit**

## 🛠️ Technologies Used

* **Python**
* **NLP**
* **Scikit-learn**
* **Pandas**
* **Joblib**
* **Streamlit**
* **CountVectorizer**

## 📂 Project Structure

```text
Emotion-Detection/
│
├── app.py
├── emotion_model.pkl
├── count_vectorizer.pkl
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

```text
User Input
    ↓
Text Preprocessing
    ↓
Count Vectorization
    ↓
Trained ML Model
    ↓
Emotion Prediction
    ↓
Display Result
```

## 💻 Installation & Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
cd Emotion-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧪 Example

**Input:**

```text
I am extremely happy today!
```

**Predicted Emotion:**

```text
Happy
```
## 📸 Screenshots

### Application Preview
![Application Preview](assets/app-preview.png)

### Emotion Prediction
![Emotion Prediction](assets/app1-preview.png)


## 📊 Machine Learning

The project uses:

* **CountVectorizer** for converting text into numerical features.
* A trained **machine learning classification model** for emotion prediction.
* **Joblib** for saving and loading the trained model and vectorizer.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Natural Language Processing
* Text feature extraction
* Machine learning classification
* Model serialization using Joblib
* Building ML applications with Streamlit
* Deploying a trained ML model through an interactive interface

## 🔮 Future Improvements

* Improve model accuracy using advanced NLP techniques
* Add more emotion categories
* Experiment with TF-IDF and word embeddings
* Try deep learning models such as LSTM or Transformers
* Deploy the application online

## 👩‍💻 Author

**Anjana Reddy**

B.Tech – Computer Science & Engineering
Interested in Machine Learning and Artificial Intelligence
