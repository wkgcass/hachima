from hachima import HACHIMA

import os #to read audioClips folder
from pathlib import Path
from random import randint #randomchoice
from pydub import AudioSegment #to cimbine audioclips

# 获取当前文件所在目录的绝对路径
filePath = Path(__file__).parent.absolute()
# 移除 os.chdir(filePath)，不应该改变工作目录

# 定义音频剪辑目录和缓存目录的绝对路径
AUDIO_CLIPS_DIR = filePath / 'audioClips'
CACHE_DIR = filePath / 'cache'
CACHE_FILE = CACHE_DIR / 'audio.wav'



def makeAudio(words):
    #del words that not in HACHIMA
    words = [word for word in words if word in HACHIMA]
    #print(words)
    audio=AudioSegment.empty()
    for word in words:
        # 使用绝对路径访问音频剪辑文件夹
        whichAuClipFileFolder = AUDIO_CLIPS_DIR / word
        clips = os.listdir(whichAuClipFileFolder)
        clips = [clip for clip in clips if clip.endswith('.wav')]#only keep wav
        #if not empty
        if len(clips) == 0:
            continue
        clip = clips[randint(0,len(clips)-1)]
        #print(clip)
        audio += AudioSegment.from_file(whichAuClipFileFolder/clip)
        audio += AudioSegment.silent(duration=50)
    return audio

import pygame #to play audio
def playSound(audio,cleanUp=True):
    #ensure cache folder exists
    os.makedirs(CACHE_DIR, exist_ok=True)
    # 使用绝对路径导出音频文件
    audio.export(CACHE_FILE,format='wav')
    pygame.mixer.init()
    pygame.mixer.music.load(str(CACHE_FILE))
    pygame.mixer.music.play()
    #wait for audio to finish
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    #delete audio file
    if cleanUp:
        os.remove(CACHE_FILE)

def makeNoice(words):
    playSound(makeAudio(words))

#test 
if __name__ == '__main__':
    audio = makeAudio("""
        哈、基、米、南、北、绿、豆、#ok
        阿、西、噶、压、库、那、鲁、#ok
        曼、波、欧、马、自、立、悠、嗒、步、诺、斯、 #ok
        哇、嗷、冰、踩、背、        #ok
        叮、咚、鸡、大、狗、叫、    #ok
        袋、鼠、兴、奋、剂、出、示、健、康、码、#ok
        楼、上、下、来、带、一、段、 #ok
        小、白、手、套、胖、宝、    #ok
        牛、魔、呵、嘿、喔 #ok
    """)
    playSound(audio)

