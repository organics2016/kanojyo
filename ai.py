import config
from abc import abstractmethod, ABCMeta
import logging
import openai


class AI(metaclass=ABCMeta):

    @abstractmethod
    def completion(self, prompt: str) -> str:
        pass


class OpenAI(AI):
    openai.api_key = config.conf['OPENAI_API_KEY']
    user_id = config.conf['USER_ID']

    def completion(self, prompt: str) -> str:

        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=prompt,
                                            temperature=1,
                                            max_tokens=2048,
                                            user=self.user_id)

        result_str = response['choices'][0]['text']

        logging.info("AI Completion {}".format(result_str))

        if isinstance(result_str, str):
            return result_str.strip()

        return ''