import dialogflow_v2 as dialogflow


def get_answer(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code
    )
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input)

    if response.query_result.intent.is_fallback:
    	return
    return response.query_result.fulfillment_text
