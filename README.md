# LinguaLoop

# **LinguaLoop**

LinguaLoop is a real-time speech translation and response recommendation system. 
It translates spoken input from one language to the user's native language, offers suggested responses, and then translates the chosen response back to the input language. This project leverages Google’s Speech Recognition and Translation APIs, enabling smooth multilingual conversations.

## **Overview**

LinguaLoop facilitates multilingual communication by:
- Translating real-time speech input into the user's preferred language.
- Recommending three or more contextually appropriate responses.
- Translating the chosen response back into the original language.
- Converting the translated response into speech for playback.

Ideal for language learners or those needing quick communication in a foreign language, LinguaLoop enables seamless dialogue across language barriers.

## **Features**
- Real-time speech-to-text conversion.
- Accurate translations using Google Translate API.
- Response recommendation based on context.
- Text-to-speech output in multiple languages.

## **Technologies Used**
- **Python**: Main programming language.
- **SpeechRecognition**: For converting speech to text.
- **Googletrans**: For translation between languages.
- **gTTS (Google Text-to-Speech)**: For converting text to speech.
- **Playsound**: For playing the audio output.

## **Installation**

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LinguaLoop.git
    ```
2. Navigate to the project directory:
    ```bash
    cd LinguaLoop
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   Required libraries include:
   - `SpeechRecognition`
   - `googletrans==4.0.0-rc1`
   - `gtts`
   - `playsound`

4. Ensure you have a working microphone and speakers for real-time input and output.

## **Usage**

1. Run the main script:
    ```bash
    python main.py
    ```
2. Speak into the microphone when prompted. LinguaLoop will recognize the speech and translate it into the target language.
3. Select from the suggested responses, and LinguaLoop will translate the chosen response back into the original language and read it aloud.

## **Example Workflow**

- **Input**: User speaks, "Can you help me with this?" in English.
- **Translation**: The system translates it into the user's native language, e.g., Korean: "이것에 대해 도와주실 수 있나요?"
- **Response Suggestion**: LinguaLoop provides three suggested replies, such as:
  1. "Yes, I can help with that."
  2. "Please provide more details."
  3. "Sorry, I can't help with that right now."
- **Response Selection**: User selects option 1.
- **Final Translation**: The system translates "Yes, I can help with that." back to English and reads it aloud.
