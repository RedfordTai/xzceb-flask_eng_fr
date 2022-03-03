import os
import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-07-22',
    authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(englishText):
    """to translator word to french"""
    try:
        transcation = language_translator.translate(text=englishText,model_id='en-fr').get_result()
        respo_french_d = json.dumps(transcation,indent=0,ensure_ascii=False)
        respo_french = json.loads(respo_french_d)
        french_text = respo_french['translations'][0]['translation']
        return french_text
    except ApiException as ex:
        return str(ex.code)

def french_to_english(frenchText):
    """to translator word to english"""
    try:
        transcation = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
        respo_eng_d = json.dumps(transcation,indent=0,ensure_ascii=False)
        respo_eng = json.loads(respo_eng_d)
        eng_text = respo_eng['translations'][0]['translation']
        return eng_text
    except ApiException as ex:
        return str(ex.code)
