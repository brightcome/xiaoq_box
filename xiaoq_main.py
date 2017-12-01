#!usr/bin/env python  #coding=utf-8        from aip import AipSpeechimport numpy as np  from pyaudio import PyAudio,paInt16  from datetime import datetime  import wave  from tkinter import *  import urllib.requestimport urllibimport jsonimport pygameimport time
#define of params  NUM_SAMPLES = 2000  framerate = 8000  channels = 1  sampwidth = 2  #record time  TIME = 10
def get_file_content(filePath):    with open(filePath, 'rb') as fp:        return fp.read()
def save_wave_file(filename, data):      '''''save the date to the wav file'''      wf = wave.open(filename, 'wb')      wf.setnchannels(channels)      wf.setsampwidth(sampwidth)      wf.setframerate(framerate)      wf.writeframes(b"".join(data))      wf.close()        def my_button(root,label_text,button_text,button_func):        '''''''function of creat label and button'''        #label details        label = Label(root)        label['text'] = label_text        label.pack()        #label details        button = Button(root)        button['text'] = button_text        button['command'] = button_func        button.pack()            def record_wave():      #open the input of wave      pa = PyAudio()      stream = pa.open(format = paInt16, channels = 1,                     rate = framerate, input = True,                     frames_per_buffer = NUM_SAMPLES)      save_buffer = []      count = 0      while count < TIME:      #read NUM_SAMPLES sampling data          string_audio_data = stream.read(NUM_SAMPLES)          save_buffer.append(string_audio_data)          count += 1          print ('.')            #filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"      filename = "test.wav"      save_wave_file(filename, save_buffer)      save_buffer = []      print (filename, "saved")        def record_wav_first():      record_wave()   
def convert_wav_get_text():      """ 你的 APPID AK SK """    APP_ID = '10367256'    API_KEY = 'A5VkLmBPtidpfn5YlDqGGyQu'    SECRET_KEY = '5b79320aa2c5de933d4ebd7dcc6be721'    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)    # 识别本地文件    fanhui = aipSpeech.asr(get_file_content('test.wav'), 'pcm', 8000, {'lan': 'zh',})    #print (type(fanhui))    #print (fanhui)    jieguo = fanhui['result'][0]    print (jieguo)    return jieguo
if __name__ == "__main__":              key = '150553285b3d4d358f1ebc074a2073f2'    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='        APP_ID = '10367256'    API_KEY = 'A5VkLmBPtidpfn5YlDqGGyQu'    SECRET_KEY = '5b79320aa2c5de933d4ebd7dcc6be721'              record_wav_first()        info = convert_wav_get_text()    info_convert = urllib.parse.quote(info.encode('utf8'))    request = api + info_convert    page = urllib.request.urlopen(request)    response = page.read()    dic_json = json.loads(response)    print (dic_json['text'])    strings_txt = dic_json['text']        #图灵机器人 回答转换成 百度语音合成    aipSpeech = AipSpeech(APP_ID,API_KEY,SECRET_KEY)    result = aipSpeech.synthesis(strings_txt,'zh','1',\                                {'vol':8,                                'per':0,                                'spd':5})    if not isinstance(result,dict):        with open('tuling_duihua.mp3','wb') as f:            f.write(result)                #use pygame to play the synced souce file    file=r'tuling_duihua.mp3'    pygame.mixer.init()    print("播放图灵机器人回答")    track = pygame.mixer.music.load(file)        pygame.mixer.music.play()    while pygame.mixer.music.get_busy():        time.sleep(2)    pygame.mixer.music.stop()
