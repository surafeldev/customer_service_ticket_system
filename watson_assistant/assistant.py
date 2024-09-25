# watson_assistant/assistant.py

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import ASSISTANT_API_KEY, ASSISTANT_URL, ASSISTANT_ID

# Set up Watson Assistant
authenticator = IAMAuthenticator(ASSISTANT_API_KEY)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(ASSISTANT_URL)

# Function to get a response from Watson Assistant
def get_response(ticket_text):
    session = assistant.create_session(ASSISTANT_ID).get_result()['session_id']
    response = assistant.message(
        ASSISTANT_ID,
        session,
        input={'text': ticket_text}
    ).get_result()

    # Extract the assistant's response
    return response['output']['generic'][0]['text']
