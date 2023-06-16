import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get user input
text = input("Enter the text you want to speak: ")

# Set the speed (rate) of speech
engine.setProperty('rate', 150)

# Set the volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# Speak the text
engine.say(text)

# Wait until speech is complete
engine.runAndWait()
