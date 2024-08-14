import yt_dlp
import ffmpeg
import os

URL = 'https://youtu.be/2b1IexhKPz4?si=HEBpVuiqsK9CP6ZJ'
DIR = 'C:\\Youtube'


ydl_opt_video = {
    'format':'bestvideo[ext=mp4][height<=1080]',
    'outtmpl': f'{DIR}/video.mp4', 
}
ydl_opt_audio = {
    'format':'bestaudio[ext=mp4][height<=1080]',
    'outtmpl': f'{DIR}/video.mp4', 
}

try:
    with yt_dlp.YoutubeDL(ydl_opt_video) as ydl:
        info_dict_video = ydl.extract_info(URL, download=True)
        video_itag = info_dict_video.get("format_id", None)
        print(f"Video downloaded: {DIR}\\video.mp4")
        print(f"Video itag: {video_itag}")

    with yt_dlp.YoutubeDL(ydl_opt_audio) as ydl:
        info_dict_audio = ydl.extract_info(URL, download=True)
        audio_itag = info_dict_audio.get("format_id", None)
        print(f"Audio downloaded: {DIR}\\audio.mp4")
        print(f"Audio itag: {audio_itag}")  

    video_input = ffmpeg.input(os.path.join (DIR,'video.mp4'))
    audio_input = ffmpeg.input(os.path.join (DIR,'audio.mp4'))
    output_path = os.path.join(DIR, 'output.mp4')

    ffmpeg.output(video_input, audio_input, output_path, vcodec='copy', acodec='aac', strict='experimental').run()
    print(f"Video and audio merged: {output_path} " )

    os.remove(os.path.join(DIR, 'video.mp4'))
    os.remove(os.path.join(DIR, 'audio.mp4'))




except Exception as e:
    print(f"An unexpected error occured while downloading video:{e}")

