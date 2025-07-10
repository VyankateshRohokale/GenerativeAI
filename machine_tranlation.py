from translate import Translator


translate_obj = Translator(to_lang='es')

text = "Hey, this is piyush!"


print("English : ",text)

translated_text = translate_obj.translate(text)

print("Spanish : ",translated_text)