import speech_recognition as sr
from audio_dicer import AudioDicer
import os
import time
import moviepy.editor as mp
import send2trash

##Created by Lex Whalen 2/19/21
class AudioVideoRecognizer():
    """Deals with audio recognition. Uses Google Translate for .wav files. If a video, converts to .wav then uses Google Translate."""

    def __init__(self):
        self.RECOG = sr.Recognizer()
        self.DICER = AudioDicer()

        self.CWD = os.getcwd()
        self.TEMP_AUD = os.path.join(self.CWD,"temp_aud")

    def trash_file(self,file_path):
        #sends file to trash
        send2trash.send2trash(file_path)

    def slice_aud(self,file_path):
        """Dices audio into SECONDS seconds. I did 30 in the video, but 45 works better."""
        SECONDS = 30
        self.DICER.multiple_split(file_path,SECONDS)

    def transcribe(self,file_name,lang):
        """Transcribes the audio. Returns a list of the words found in that audio segment."""

        with sr.WavFile(file_name) as source: #use f.wav as aud source
            audio = self.RECOG.record(source) #get aud data
            try:
                #first try is to see if google recognizes that it is speech
                try:
                    #second try is to see if it can make the speech out
                    words = [i for i in (self.RECOG.recognize_google(audio,language = lang)).split()]
                    
                    #return the list of words found from GT
                    return words

                except Exception as e:
                    #found no words in the audio
                    #return an empty list

                    return []

            except LookupError: #unintelligible
                print("Could not understand audio")

    def from_file(self,f,lang, isVideo = False):

        if not isVideo:
            #already working with only an audio file
            words = transcribe(f,lang)

            return words

        elif isVideo:
            #convert to wav and read
            
            aud_path_name = "temp{}.wav".format(len(os.listdir(self.TEMP_AUD)))
            aud_path_abs = os.path.join(self.TEMP_AUD,aud_path_name)

            clip = mp.VideoFileClip(f)
            clip.audio.write_audiofile(aud_path_abs)

            #cut the clip into 30 second pieces so google can work with them

            self.slice_aud(aud_path_abs)
            
            #throw away the base audio
            self.trash_file(aud_path_abs)

            #loop through the split audio, append to a list
            master_words = []

            for f in os.listdir(self.TEMP_AUD):
                f_path = os.path.join(self.TEMP_AUD,f)

                words = self.transcribe(f_path,lang)

                #to prevent google from shutting us down
                time.sleep(2)

                #append the words we found in that audio clip to the master_words for use in creating .txt file
                master_words += words
            


            #throw away the temps 
            for f in os.listdir(self.TEMP_AUD):
                f_path = os.path.join(self.TEMP_AUD,f)

                self.trash_file(f_path)

            


            #finally return words
            return master_words






