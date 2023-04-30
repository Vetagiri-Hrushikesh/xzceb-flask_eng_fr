from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    ''' Translate English to French '''
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.translate_english_to_french(textToTranslate)   
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    ''' Translate French to Enflish '''
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.translate_french_to_english(textToTranslate)  
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(debug = True, port = 5000)
    app.run(host = "0.0.0.0", port = 8080)