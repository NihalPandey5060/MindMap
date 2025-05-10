import streamlit as st
from transformers import pipeline
from data_utils import InteractionLogger

# Initialize session state
if 'classifier' not in st.session_state:
    st.session_state.classifier = pipeline("text-classification", model="parka735/mbti-classifier")
if 'logger' not in st.session_state:
    st.session_state.logger = InteractionLogger()

def main():
    st.title("🧠 Personality Predictor (MBTI)")
    st.write("Enter a paragraph about yourself, and get your MBTI personality type predicted!")

    # Text input for personality prediction
    user_input = st.text_area("Describe yourself in a few sentences")

    if st.button("Predict Personality"):
        if user_input.strip():
            try:
                prediction = st.session_state.classifier(user_input)[0]
                predicted_type = prediction['label']
                score = round(prediction['score'] * 100, 2)

                # Log interaction
                st.session_state.logger.log_interaction(user_input, {"MBTI Type": predicted_type, "Confidence": f"{score}%"})

                st.success(f"Predicted MBTI Type: **{predicted_type}** with {score}% confidence")

            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
        else:
            st.warning("Please enter some text for prediction.")

    # Show past interactions
    st.header("📝 Prediction History")
    interactions = st.session_state.logger.get_recent_interactions()
    if interactions:
        for interaction in reversed(interactions):
            with st.expander(f"Interaction at {interaction['timestamp']}"):
                st.write("Text:", interaction['input'])
                st.write("Prediction:", interaction['prediction'])
    else:
        st.info("No predictions made yet.")

if __name__ == "__main__":
    main()