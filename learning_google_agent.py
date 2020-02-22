import dialogflow_v2 as dialogflow
from dotenv import load_dotenv

import file


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)
    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)


def main():
    answers_and_questions = file.get_phrases('questions.json')
    for answer_and_question in answers_and_questions.items():
        display_name = answer_and_question[0]
        training_phrases_parts = answer_and_question[1]['questions']
        message_texts = [answer_and_question[1]['answer']]
        create_intent(file.get_project_id(), display_name,
                      training_phrases_parts, message_texts)


if __name__ == '__main__':
    load_dotenv()
    main()
