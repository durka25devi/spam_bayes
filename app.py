import streamlit as st
import pickle as pkl

# 📦 Load the combined pickle file (model + vectorizer)
with open('spam_model.pkl', 'rb') as f:
    nb, vectorizer = pkl.load(f)

# 🧠 Streamlit App Interface
st.set_page_config(page_title="Spam Message Detector", page_icon="📩")
st.title("📩 Spam Message Detector")
st.write("Enter a message below to check if it’s **Spam** or **Ham (Not Spam)**.")

# 📝 Input from user
user_input = st.text_area("Type your message here:")

# 🔍 Predict button
if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        # Transform and predict
        input_vec = vectorizer.transform([user_input])
        prediction = nb.predict(input_vec)[0]

        # 🎯 Display Result
        if prediction == 1:
            st.error("🚨 This message is **Spam!**")
        else:
            st.success("✅ This message is **Ham (Not Spam)**.")

# Optional: Add some styling or info
st.markdown("---")
st.caption("Built using Naive Bayes and CountVectorizer.")
