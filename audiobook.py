pip -q install gTTS  # Install the gTTS library
from gtts import gTTS  # Now this line should work

def text_to_speech_save(text, output_path):
    # Convert text to speech using Google Text-to-Speech (gTTS)
    tts = gTTS(text=text, lang='en')
    
    # Save the converted speech to an MP3 file
    tts.save(output_path)
    print(f"Audiobook saved as {output_path}")

if __name__ == "__main__":
    # Ask the user how they want to provide the text
    print("How would you like to provide the text for the audiobook?")
    print("1. Input the text manually")
    print("2. Provide a text file")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Option to input text manually
        print("Enter the text you want to convert to an audiobook:")
        text_content = input("> ").strip()
    elif choice == "2":
        # Option to read text from a file
        file_path = input("Enter the path to the text file: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            text_content = None
    else:
        print("Invalid choice. Exiting.")
        text_content = None
    
    # If text content is available, proceed with conversion
    if text_content:
        print("Starting the audiobook creation...")
        output_file = input("Enter the output path for the audiobook (including filename and extension): ").strip()
        text_to_speech_save(text_content, output_file)
        print("Audiobook creation completed!")
