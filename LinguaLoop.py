pip install SpeechRecognition googletrans==4.0.0-rc1 gtts playsound

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound

# 음성 인식을 위한 함수
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("음성을 입력하세요:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"입력된 음성: {text}")
            return text
        except sr.UnknownValueError:
            print("음성을 인식하지 못했습니다.")
            return None
        except sr.RequestError as e:
            print(f"Google API 요청 오류: {e}")
            return None

# 번역을 위한 함수
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# 답안 추천을 위한 함수
def suggest_responses(original_text):
    # 간단한 답변 예시
    responses = [
        "감사합니다, 도움이 되셨기를 바랍니다.",
        "추가 질문이 있으시면 언제든지 알려주세요.",
        "네, 그렇게 진행하시면 됩니다."
    ]
    print("\n추천 답안:")
    for i, response in enumerate(responses, 1):
        print(f"{i}. {response}")
    
    selected = int(input("\n원하는 답안을 선택하세요 (숫자로 입력): "))
    return responses[selected - 1]

# 텍스트를 음성으로 변환하여 재생하는 함수
def speak_text(text, language_code):
    tts = gTTS(text=text, lang=language_code)
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

# 메인 실행 함수
def main():
    # 1. 음성 인식 (외국어로 입력)
    foreign_text = recognize_speech()
    if not foreign_text:
        return

    # 2. 음성을 모국어로 번역 (예: 한국어)
    translated_text = translate_text(foreign_text, 'ko')
    print(f"\n번역된 텍스트 (한국어): {translated_text}")

    # 3. 답변 추천
    response = suggest_responses(translated_text)

    # 4. 선택된 답안을 외국어로 번역 (예: 영어로 다시 번역)
    translated_response = translate_text(response, 'en')
    print(f"\n번역된 답변 (영어): {translated_response}")

    # 5. 외국어로 된 답변을 음성으로 출력
    speak_text(translated_response, 'en')

if __name__ == "__main__":
    main()
