Adapted from: https://github.com/maratona-linux/maratona-animeitor
Author: Marcio Oshiro


Use with Python 3, Pygame 1.9.6; e.g. on Ubuntu run

    sudo apt install python3 python-pip
    python3 -m pip install -r requirements.txt

How to use:

1º) change the logo event in "images" folder
2º) Put into the "images/team_photos" folder the teams photos, renamed with the user of boca and in .JPG (extension must be capitalized)
3º) After contest, put the "webcast files" from Boca, to the "sample" folder.
5º) Run Animeitor 

Full Screen
python3 ./main.py sample/

Window mode
python3 ./main.py -w sample/

Set FPS (-f : framerate for the animator. Defaults to 30 fps) 
python3 ./main.py -f 24 -w sample/


Keyboard control: 
 P - while time is running Tap "P" to pause song or "R" to resume.
 PageDown --- Tap PageDown once to fast-forward to the end of the contest, then tap the PageDown to advance through the contest teams.
 PageUP   --- Tap PageUP when show the "team photo" to set the song. The "Volume" word will show in the left top, then Tap PageUP to up the volume. The volume is configured to stop in "0.8", Tap PageUP to back scoreboard.
 Q - Tap "Q" to quit

- Change the songs
   Put in "music" folder the background songs. (mp3, ogg, etc files) - The animeitor will play just the first song of the folder (in alphabetic order) 
   Put in "musicas" folder the team's songs. (mp3, ogg, etc files) - To organize the sequece of songs, rename the songs (in alphabetic order) - The lasts songs will be played for 1º,2º, 3º and 4º placed of contest 


WARNING: We are not the authors of the base code, so we do not guarantee it will work properly!
