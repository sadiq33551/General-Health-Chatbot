# ==========================================
# General Health Query Chatbot
# Author: Syed Muhammad Sadiq
# ==========================================

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "sore throat" in user_input:
        return "A sore throat is usually caused by a viral infection, cold, or allergies."

    elif "paracetamol" in user_input:
        return "Paracetamol is generally safe for children in proper dosage. Always consult a doctor."

    elif "fever" in user_input:
        return "Fever is often a sign that your body is fighting infection."

    elif "bye" in user_input:
        return "Goodbye! Take care of your health."

    else:
        return "I'm not sure. Please consult a medical professional for proper advice."


print("Health Chatbot (Type 'bye' to exit)")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye! Stay healthy.")
        break
    response = chatbot_response(user)
    print("Bot:", response)