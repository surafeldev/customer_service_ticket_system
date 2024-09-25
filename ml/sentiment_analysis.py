# ml/sentiment_analysis.py

from ibm_watson_machine_learning import APIClient
from config import WML_API_KEY, WML_URL, SENTIMENT_MODEL_ID

wml_credentials = {
    "apikey": WML_API_KEY,
    "url": WML_URL
}

client = APIClient(wml_credentials)

def analyze_sentiment(ticket_text):
    deployment = client.deployments.get_details(SENTIMENT_MODEL_ID)
    payload = {"input_data": [{"values": [[ticket_text]]}]}

    result = client.deployments.score(deployment['entity']['deployment_id'], payload)
    
    return result['predictions'][0]['values'][0][0]  # Return sentiment score
