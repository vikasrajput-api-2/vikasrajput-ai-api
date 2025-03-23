from Gemini import get_shagun_reply

ai_active = False

def start_chat():
    global ai_active
    print("Shagun AI Bot Ready! Type 'ai on' to start, 'ai off' to stop, 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Shagun: Bye bye! Masti khatam.")
            break

        elif user_input.lower() == "ai on":
            ai_active = True
            print("Shagun: Hehe! Chalu ho gayi Shagun AI!")

        elif user_input.lower() == "ai off":
            ai_active = False
            print("Shagun: AI band ho gayi. Ab main chup hoon.")

        elif not ai_active:
            print('Shagun: Mujhe chalu karne ke liye "ai on" likho.')

        else:
            reply = get_shagun_reply(user_input)
            print(f"Shagun: {reply}")

if __name__ == "__main__":
    start_chat()
