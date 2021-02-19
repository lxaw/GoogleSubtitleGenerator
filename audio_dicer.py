import os
import pydub
from pydub import AudioSegment
import math

##Created by Lex Whalen 2/19/21
class AudioDicer():
    """Google Translate can only handle so much file size, so we need to slice up our audio into bite-sized pieces."""

    def __init__(self):
        self.CWD = os.getcwd()
        self.TEMP_SPLIT_AUD = os.path.join(self.CWD,"temp_split_aud")

    def get_aud(self, raw_file):
        #returns an AudioSegment representation of your audio


        #You could also change the rate of the audio as you read the file. I have included the code for that below.
        
        #RATE is the rate of the audio. For instance, 0.5 is half the speed. 
        #Play around with this to see if it helps GT recognize the audio.
        #RATE = 0.9

        sound =  AudioSegment.from_file(raw_file)
        #sound.set_frame_rate(int(sound.frame_rate * RATE))

        return sound

    def get_duration(self,aud_segment):
        
        #returns the time of the audio file. This is used to split the audio evenly.
        return aud_segment.duration_seconds

    def speed_change(self,sound, speed=1.0):
        ####Credit to StackOverflow####


        # Manually override the frame_rate. This tells the computer how many
        # samples to play per second
        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * speed)
        })

        # convert the sound with altered frame rate to a standard frame rate
        # so that regular playback programs will work right. They often only
        # know how to play audio at standard frame rate (like 44.1k)
        return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


    def single_split(self,aud_segment,from_sec,to_sec,split_fn):

        #aud_segment does stuff in milliseconds, so multiply to get to seconds.
        t1 = from_sec * 1000 
        t2 = to_sec * 1000

        #split the audio from t1 to t2
        split_aud = aud_segment[t1:t2]
        
        #slow the audio down 
        slowed = self.speed_change(split_aud,0.9)

        slowed.export(split_fn,format="wav")

    def multiple_split(self,raw_file,sec_per_split):
        #creates multiple splits of the audio file


        aud_seg = self.get_aud(raw_file)

        #get the total seconds as an upper bound
        total_secs = math.ceil(self.get_duration(aud_seg))

        cut_iter = 0

        for i in range(0,total_secs,sec_per_split):

            #left pad zeros to loop through file names correctly
            split_fn = "{}-{}.wav".format(raw_file.split(".wav")[0],str(cut_iter).zfill(5)) #create file name for the split up aud

            self.single_split(aud_seg,i,i+sec_per_split,split_fn)
            cut_iter +=1

