import datetime

# ========= BUSINESS INFO =========
BUSINESS = {
    "owner": "Haji Zafar Iqbal",
    "location": "District Kot Addu, Division D.G. Khan",
    "contact": "03007339740"
}

# ========= KNOWLEDGE BASE =========
fish_data = {
    "rohu": {
        "price": "500 PKR/kg",
        "feed": "Rice polish + Soybean meal"
    },
    "tilapia": {
        "price": "450 PKR/kg",
        "feed": "Commercial pellets"
    },
    "catla": {
        "price": "550 PKR/kg",
        "feed": "Wheat bran + Fish meal"
    }
}

# ========= INTENT DETECTION =========
def detect_intent(user_input):
    text = user_input.lower()

    intents = {
        "owner": ["owner", "malik"],
        "location": ["location", "kahan", "address"],
        "contact": ["contact", "number", "phone"],
        "fish_info": ["fish", "types", "varieties"],
        "price": ["price", "rate"],
        "feed": ["feed", "khurak"],
        "farming": ["farming", "start"],
        "profit": ["profit", "increase"],
        "time": ["time"]
    }

    for intent, keywords in intents.items():
        if any(word in text for word in keywords):
            return intent

    # fish name detection
    for fish in fish_data:
        if fish in text:
            return f"fish_{fish}"

    return "unknown"

# ========= RESPONSE HANDLERS =========
def handle_intent(intent):

    if intent == "owner":
        return f"👤 Owner: {BUSINESS['owner']}"

    elif intent == "location":
        return f"📍 Location: {BUSINESS['location']}"

    elif intent == "contact":
        return f"📞 Contact: {BUSINESS['contact']}"

    elif intent == "fish_info":
        return "🐟 Available Fish: " + ", ".join(fish_data.keys())

    elif intent.startswith("fish_"):
        fish = intent.split("_")[1]
        data = fish_data[fish]
        return f"""
🐟 {fish.upper()}
💰 Price: {data['price']}
🌾 Feed: {data['feed']}
"""

    elif intent == "farming":
        return """
📘 Fish Farming Guide:
1. Pond Preparation
2. Water Quality (pH 6.5–8)
3. Stocking Fish
4. Feeding Schedule
5. Disease Control
"""

    elif intent == "profit":
        return """
📈 Profit Tips:
✔️ High quality feed
✔️ Proper oxygen level
✔️ Avoid overcrowding
✔️ Regular monitoring
"""

    elif intent == "feed":
        return """
🌾 General Feed:
- Rice polish
- Wheat bran
- Soybean meal
- Fish meal
"""

    elif intent == "time":
        return str(datetime.datetime.now())

    else:
        return "❗ Sorry, I didn't understand. Ask about fish, price, farming, contact, etc."

# ========= MAIN CHATBOT =========
def chatbot():
    print("🐟 Fish Farming PRO Chatbot")
    print(f"Owner: {BUSINESS['owner']}")
    print("Type 'exit' to quit\n")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("Bot: Allah Hafiz! 🐟")
            break

        intent = detect_intent(user)
        response = handle_intent(intent)

        print("Bot:", response)

# ========= RUN =========
chatbot()
