import config
from abc import abstractmethod, ABCMeta
import logging
import xml.dom.minidom
import azure.cognitiveservices.speech as speechsdk


class Speech(metaclass=ABCMeta):

    @abstractmethod
    def speechToText(self) -> str:
        pass

    @abstractmethod
    def textToSpeech(self, text: str):
        pass


class AzureSpeech(Speech):

    speech_config = speechsdk.SpeechConfig(
        subscription=config.conf['SPEECH_KEY'],
        region=config.conf['SPEECH_REGION'])

    speech_config.speech_recognition_language = config.conf[
        'SPEECH_RECOGNITION_LANGUAGE']

    audio_input_config = speechsdk.audio.AudioConfig(
        use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input_config)

    def speechToText(self) -> str:

        print("Speak into your microphone.")
        speech_recognition_result = self.speech_recognizer.recognize_once_async(
        ).get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            logging.info("Recognized: {}".format(
                speech_recognition_result.text))
            return speech_recognition_result.text

        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            logging.info("No speech could be recognized: {}".format(
                speech_recognition_result.no_match_details))

        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            logging.info("Speech Recognition canceled: {}".format(
                cancellation_details.reason))

            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                logging.error("Error details: {}".format(
                    cancellation_details.error_details))
                logging.info(
                    "Did you set the speech resource key and region values?")

        return ''

    audio_output_config = speechsdk.audio.AudioOutputConfig(
        use_default_speaker=True)
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_output_config)

    def textToSpeech(self, text: str):

        speech_synthesis_result = self.speech_synthesizer.speak_ssml_async(
            self.textToSSML(text)).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            logging.info("Speech synthesized finish")

        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            logging.info("Speech synthesis canceled: {}".format(
                cancellation_details.reason))

            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    logging.error("Error details: {}".format(
                        cancellation_details.error_details))
                    logging.info(
                        "Did you set the speech resource key and region values?"
                    )

    ssml_template = xml.dom.minidom.parse('ssml.xml').documentElement

    def textToSSML(self, text: str) -> str:
        voice = self.ssml_template.getElementsByTagName('voice')[0]
        mstts = voice.getElementsByTagName('mstts:express-as')[0]
        mstts.childNodes[0].data = text
        return str(self.ssml_template.toxml('utf-8'), 'utf-8')
