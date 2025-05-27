import random
from ai import call_gpt

def indonesia_culinary():
    """
    Suggests an Indonesian culinary dish based on the user's mood.
    This version includes a loop for continuous suggestions and improved mood matching.
    """
    culinary_dictionary = {
        'happy': ['Nasi Goreng', 'Sate Ayam', 'Bakso', 'Es Campur'],
        'sad': ['Soto Ayam hangat', 'Indomie Goreng (comfort food!)', 'Bubur Ayam'],
        'hungry': ['Rendang', 'Gudeg', 'Mie Ayam', 'Nasi Padang'],
        'adventurous': ['Pempek', 'Rawon', 'Gado-Gado', 'Martabak Manis'],
        'spicy': ['Ayam Geprek', 'Seblak', 'Sambal Matah (with anything!)'],
        'light': ['Sayur Asem', 'Pecel', 'Asinan Buah'],
        'sweet': ['Klepon', 'Dadar Gulung', 'Serabi'],
        'refreshing': ['Es Teh Manis', 'Es Dawet', 'Cendol'],
        'tired': ['Sop Buntut', 'Nasi Uduk', 'Lontong Sayur'],
        'curious': ['Nasi Liwet', 'Karedok', 'Otak-Otak'],
        'default': ['Nasi Goreng', 'Sate Ayam', 'Bakso', 'Rendang', 'Gado-Gado'] # Fallback if mood not matched
    }

    print("--- What to Eat? - Indonesian Culinary! ---")

    while True: # Loop to allow multiple suggestions
        user_input_action = input("\nInput mood? Or exit? Just type 'mood' or 'exit': ").strip().lower()

        if user_input_action == 'exit':
            print("\nThank you for using the Indonesian Culinary Suggester. Enjoy your meal!")
            break # Exit the loop
        
        elif user_input_action == 'mood':
            print("-" * 50)
            mood_keys = [key for key in culinary_dictionary if key != 'default']
            # Determine maximum mood key length for formatting
            max_len = max(len(key) for key in mood_keys) if mood_keys else 0

            # Print moods in a structured way
            num_columns = 3 # You can adjust the number of columns
            for i in range(0, len(mood_keys), num_columns):
                row_moods = mood_keys[i:i + num_columns]
                formatted_row = " | ".join(f"{mood:<{max_len}}" for mood in row_moods)
                print(f"| {formatted_row} |")
            print("-" * 50)

            user_mood = input("\nHow is your mood today? ").strip().lower()

            suggested_dishes = []
            found_specific_mood = False

            # Iterate through the keys in culinary_dictionary to find a match
            # We check if the mood key is present in the user's input string
            for mood_key, dishes in culinary_dictionary.items():
                if mood_key != 'default' and mood_key in user_mood:
                    suggested_dishes = dishes
                    found_specific_mood = True
                    break # Stop after finding the first relevant mood

            # Handle cases where no specific mood is found or input is empty
            if not found_specific_mood:
                suggested_dishes = culinary_dictionary['default'] # Use default suggestions
                if user_mood == '':
                    print("\nPlease enter your mood to get a more specific suggestion!")
                else:
                    print(f"\nI don't have a specific suggestion for '{user_mood}'. Here's a general Indonesian culinary suggestion:")
            else:
                print(f"\nBased on your mood '{user_mood}', here's a suggestion:")

            # Get a random dish from the selected list and print it
            suggestion = random.choice(suggested_dishes)
            print(f"\n-> You might enjoy: {suggestion}!\n")
            print("-" * 40) # Separator for better readability
            
            gpt_activation = input(f"\nDo you want to know more about {suggestion}? Type 'yes' or 'no': ").strip().lower()
            if gpt_activation == 'yes':
                response = call_gpt(f"Please tell me more about Indonesian dish called {suggestion}")
                print("-" * 40)
                print(f"\n{response}")
            else:
                print("\nThank you for using the Indonesian Culinary Suggester. Enjoy your meal!")
                break

        else:
            print("\nInvalid input. Please type 'mood' to get a suggestion or 'exit' to quit.")
            print("-" * 40)

if __name__ == "__main__":
    indonesia_culinary()