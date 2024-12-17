from gtts import gTTS
import os

def read_text_file(file_path):
    try:
        # Open the text file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def text_to_speech_save(text, output_path):
    # Convert text to speech using Google Text-to-Speech (gTTS)
    tts = gTTS(text=text, lang='en')
    
    # Save the converted speech to an MP3 file
    tts.save(output_path)
    print(f"Audiobook saved as {output_path}")

if __name__ == "__main__":
    # Provide the path to the text file you want to convert to an audiobook
    file_path = "E:\Python\Audio Book\sample.txt"  # Replace this with the actual path to your text file
    
    # Read the text from the file
    text_content = read_text_file(file_path)
    
    # If file reading is successful, convert text to speech and save it
    if text_content:
        print("Starting the audiobook creation...")
        output_file = "E:\Python\Audio Book\Quaid_Easy.mp3"  # Output MP3 file path
        text_to_speech_save(text_content, output_file)
        print("Audiobook creation completed!")
