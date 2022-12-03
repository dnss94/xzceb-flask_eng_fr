''' Coursera translator '''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

authentiacator = IAMAuthenticator("XYjTX72BwgbkjafLKZAncBxqvC6NeNOe4v_0GA18EvaU")
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authentiacator
)
language_translator.set_service_url("https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/c5c3b358-3f13-43b0-b3df-071363c33dac")


def english_to_french(englishtext):
    """ Section e2f"""
    french_text = language_translator.translate(text=englishtext,model_id="en-fr").get_result()
    return french_text.get("translations")[0].get("translate")

def french_to_english(frenchtext):
    """Section f2e"""
    english_text = language_translator.translate(text=frenchtext,model_id="fr-en").get_result()
    return english_text.get("translations")[0].get("translate")
