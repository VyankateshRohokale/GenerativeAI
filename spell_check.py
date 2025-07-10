from textblob import TextBlob


text = 'I love progamming and machine learnig.'

textblob_obj = TextBlob(text)

correct_text = textblob_obj.correct()

print("Wrong Text : ",text)
print("Corrected Text : ",correct_text)