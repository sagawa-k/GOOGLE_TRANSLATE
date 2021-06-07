from googletrans import Translator
import sys
import eel

def text_translate(base_text, base_country, result_country):
  translator = Translator()
  country_list = {"日本語":"ja", "英語":"en", "フランス語":"fr", "ドイツ語": "de"}
  print(translator.translate(base_text, src=country_list[base_country] ,dest=country_list[result_country]).text)
  eel.view_result(translator.translate(base_text, src=country_list[base_country] ,dest=country_list[result_country]).text)
