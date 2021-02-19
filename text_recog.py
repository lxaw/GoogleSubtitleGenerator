from google_trans_new import google_translator
translator = google_translator()  

##Created by Lex Whalen 2/19/21
class TextRecognizer():
    ###for text only

    def __init__(self):
        self.TRANSLATOR = google_translator()

    def translate_text(self,text,src_lang,out_lang):
        translate_text = self.TRANSLATOR.translate(text,lang_src=src_lang,lang_tgt=out_lang)

        return translate_text

    def detect_lang(self, text):
        ##returns the detected language
        detect_res = self.TRANSLATOR.detect(text)
        
        return detect_res


###THIS IS BONUS CONTENT. Try to apply it to the regular sub generator to convert English! 


#translate_text = translator.translate('Hello!',lang_src='en', lang_tgt='ja')  

#rint(translate_text)