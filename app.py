import streamlit as st
import joblib

# Load the saved model and vectorizer
nb_model = joblib.load("emotion_model.pkl")
bow_vectorizer = joblib.load("count_vectorizer.pkl")
st.set_page_config(
    page_title="Emotion Detection",
    page_icon="😊"
)

st.title("😊 Emotion Detection using NLP")

st.write("Enter a sentence and click **Predict Emotion**.")

# Text input
text = st.text_area("Enter your sentence here:")
emotion_map = {
    0: "sadness",
    1: "anger",
    2: "love",
    3: "surprise",
    4: "fear",
    5: "joy"
}

emotion_emoji = {
    "sadness": "😢",
    "anger": "😠",
    "love": "❤️",
    "surprise": "😲",
    "fear": "😨",
    "joy": "😊"
}


emotion_description = {
    "sadness": "The text expresses sadness, disappointment, loneliness, or emotional pain.",
    "anger": "The text expresses frustration, irritation, or anger.",
    "love": "The text expresses affection, care, attachment, or love.",
    "surprise": "The text expresses shock, amazement, or an unexpected feeling.",
    "fear": "The text expresses worry, anxiety, or fear.",
    "joy": "The text expresses happiness, excitement, or a positive emotion."
}
if st.button("🔍 Predict Emotion"):

    if text.strip() != "":

        text = text.lower()

        text_bow = bow_vectorizer.transform([text])

        prediction = nb_model.predict(text_bow)[0]

        predicted_emotion = emotion_map[prediction]

        probabilities = nb_model.predict_proba(text_bow)

        confidence = max(probabilities[0]) * 100


        st.success(
            f"{emotion_emoji[predicted_emotion]} Emotion: {predicted_emotion.upper()}"
        )

        st.write(f"📊 Confidence: {confidence:.2f}%")

        st.write(
            f"📖 Description: {emotion_description[predicted_emotion]}"
        )


        st.subheader("📊 All Emotion Scores")

        for i, prob in enumerate(probabilities[0]):
            emotion = emotion_map[i]
            st.write(
                f"{emotion_emoji[emotion]} {emotion.capitalize()}: {prob*100:.2f}%"
            )

    else:
        st.warning("Please enter a sentence.")