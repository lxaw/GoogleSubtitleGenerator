import os
from aud_vid_recog import AudioVideoRecognizer

##Created by Lex Whalen 2/19/21
class EpisodeScraper():
    """Scrapes a single Episode"""

    def __init__(self):
        self.AudVidRecog = AudioVideoRecognizer()

    def write_to_file(self,text_list,file_path):

        with open(file_path,'w',encoding="utf-8") as f:
            for num, word in enumerate(text_list):
                f.write("{}\t{}\n".format(num,word))

    def scrape_episode(self,src_lang,ep_path,out_path):

        ###just scrape the original audio
        text = self.AudVidRecog.from_file(ep_path,src_lang,isVideo=True)

        self.write_to_file(text,out_path)


            
