from google_trans_new import google_translator


##Created by Lex Whalen 2/19/21
class Translator:

    def __init__(self):
        self.TRANSLATOR = google_translator()

    def translateText(self,text,lang_src,lang_tgt):
        translate_text = self.TRANSLATOR.translate(text,lang_src=lang_src,lang_tgt=lang_tgt)
        
        return translate_text

    def detectLang(self,text):
        detect_result = self.TRANSLATOR.detect(text)

        return detect_result
###THIS IS BONUS CONTENT. Try to apply it to the regular sub generator to convert English! 