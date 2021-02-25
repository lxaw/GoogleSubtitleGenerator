# GoogleSubtitleGenerater

# GoogleTranslate Sub Generator

## Automate the generation of subtitles for other languages.

## :cinema: Video:
* https://youtu.be/xnNB2NdUYUk

## :grey_question: What is it?
* Uses GoogleTranslate to create subtitle files for imported audio. If video, converts the video to .wav and does the same thing. Has potential to translate between languages.
###### Limitations:
* Because I do not have a "premium" Google account (or whatever it is called for the paid API), I do not have access to all of the features. The biggest of these is timestamps. 
Besides the payment, there are some barriers implicit to using automated translation. The biggest one is that translation engines as of now are not the best when it comes to more muddied audio. 
For instance, this translation works very well with crisp clips of one or two people speaking at turns, but loses power as background voices / noises come into play. This would best be used 
for something like getting translations of audiobooks, or podcasts (anything with very clear audio).

## :zap: Features:
* Translates audio clips!
* Translates video clips!
* Creates subtitle files for each clip!
* Allows for translation from a source lang to a target lang! (Look at the files w/in here)

## :package: Modules / Packages:
* speech_recognition: https://pypi.org/project/SpeechRecognition/
* moviepy: https://pypi.org/project/moviepy/
* send2trash: https://pypi.org/project/Send2Trash/
* os: https://docs.python.org/3/library/os.html
* time: https://docs.python.org/3/library/time.html
* pydub: https://pypi.org/project/pydub/
* math: https://docs.python.org/3/library/math.html


###### :hammer: To do:
* See if there is anyway to get the timestamps. Try to play around with slowing down the audio / changing pitch to improve translation quality.

