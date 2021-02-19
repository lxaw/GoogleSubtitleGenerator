import os
from episode_scraper import EpisodeScraper
from aud_vid_recog import AudioVideoRecognizer
from text_recog import TextRecognizer

##Created by Lex Whalen 2/19/21
class MasterTranslate():
    ###manages both text and speech recog
    def __init__(self):
        ###standard paths
        self.CWD = os.getcwd()
        self.SUB_FOLDER = os.path.join(self.CWD,"generated_subs")

        ###for voice / text recog
        self.AudVidRecog = AudioVideoRecognizer()
        self.EpScraper = EpisodeScraper()

    
    def show_lang_options(self):
        print("See the following link for all language codes:")
        print("https://cloud.google.com/speech-to-text/docs/languages")

    def scrape_show(self,src_lang,folder_path):

        for num, f_name in enumerate(os.listdir(folder_path)):
            f_path = os.path.join(folder_path,f_name)
            text_path = os.path.join(self.SUB_FOLDER,"{}_sub{}".format(f_name.split(".")[0],num))

            self.EpScraper.scrape_episode(src_lang,f_path,out_path = text_path)

if __name__ == "__main__":

    MT = MasterTranslate()

    YOUR_LANG = "ja-JP"
    YOUR_FLDR = "YOUR_SHOW_FLDR"

    MT.scrape_show(YOUR_LANG,YOUR_FLDR)
    print("Done")

    
