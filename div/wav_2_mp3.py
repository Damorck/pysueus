import os
import pydub
import glob
import datetime
import shutil
from pydub.utils import which
from PIL import Image


which("ffmpeg")
dato = datetime.date.today()

print("Opretter mp3-mappe...")
os.mkdir(str(dato) + "_MP3")

wav_files = glob.glob('./*.wav')
for wav_format in wav_files:
    mp3_file = os.path.splitext(wav_format)[0] + '.mp3'
    sound = pydub.AudioSegment.from_wav(wav_format)
    sound.export((str('./') + str(dato) + "_MP3/" + mp3_file[2:]), format="mp3")
    print(str(mp3_file[2:][:-4]), "succesfuldt konverteret til mp3")
im = Image.open("abby.png")
im.show()