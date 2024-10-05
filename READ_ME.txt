##Created by Lex Whalen 2/19/21
##Edited by Eric Chen 10/1/24

To user, run "py master_translate.py" to run the function. 
Please note that this requires a linux plugin currently (ffmpeg, avconv) to run

YOUR_LANG is the language the show is IN. For instance, with ジョジョの奇妙な冒険,
I had "ja-JP". Look at the link under "show_lang_options" to see all of the potential languages.
You could translate to a different language as well, but first you would need the subtitle files, so
you MUST use the SOURCE LANGUAGE OF THE CONTENT as the argument for MasterTranslate's "YOUR_LANG".

To translate into a different language, play around with text_translator. I did not finish the setup for it,
but it should not be too difficult.

FOLDERS OF IMPORTANCE:

"generated_subs" is where the subtitle files are generated. Do not delete this folder, or if you do recreate it.
Or of course, you could decide what folder you want to use by playing around with the code.

Similarly, "temp_aud" is where the temporary audio clips are stored. Same thing applies as the above folder.+
SOME OTHER NOTES:
I have included both a .wav and .mkv for you to try out. Furthermore, I included the sub that was generated from the video.

Please improve this if you can! I think it has potential, but I am limited because I do not know much!