import os
import subprocess

# Check if mode is ON
shagun_mode = os.getenv("SHAGUN_MODE", "off").lower()

if shagun_mode == "off":
    print("Shagun ka mood abhi off hai baby... ON karo tabhi baat karungi!")
else:
    try:
        user_input = input("Bolo jaan, kya baat karni hai mujhse? > ")
        result = subprocess.run(['python', 'Gemini.py', user_input], capture_output=True, text=True)
        if result.stdout.strip():
            print("\nShagun says:\n" + result.stdout.strip())
        else:
            print("Uff... lagta hai main thoda confuse ho gayi, phir se poochho na!")
    except Exception as e:
        print(f"Aiyo! Kuch toh gadbad ho gayi... Error: {e}")
        
