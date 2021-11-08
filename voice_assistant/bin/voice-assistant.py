import speech_recognition as sr
from handle_reply.phrase_handler import handle_phrase
from service.voice_recognize_service import recognize_voice
from initialize.initializer import app_initialize
from dict.auto_response_dictionary import DONT_HEAR, YOU_SILENT
from service.auto_commands_resolver import print_command


def main():
    app_initialize()

    while True:
        try:
            user_text = recognize_voice()
            handle_phrase(user_text)
        except sr.UnknownValueError:
            print_command(DONT_HEAR)
        except sr.RequestError:
            # TODO: log at least something here
            pass
        except sr.WaitTimeoutError:
            print_command(YOU_SILENT)
        except NotImplementedError as err:
            print(str(err))


if __name__ == '__main__':
    main()
