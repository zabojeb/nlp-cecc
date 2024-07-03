from googletrans import Translator

def translate(text):
  trans = Translator()
  return trans.translate(text, src='ru', dest='en').text