import speech
import ai


def main():
    azure_speech = speech.AzureSpeech()
    open_ai = ai.OpenAI()

    while True:
        print("Enter some text that you want to speak >")
        input()

        text = azure_speech.speechToText()
        if text:
            result = open_ai.completion(text)
            if result:
                azure_speech.textToSpeech(result)


if __name__ == "__main__":
    main()