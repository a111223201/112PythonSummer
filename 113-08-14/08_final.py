import yt_dlp

URL = 'https://youtu.be/EhS9lPrrLK8?si=eflbZYivB87cuezl'
DIR = 'C:\\Youtube'



ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]',
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(URL,download=True)
        video_id = info_dict.get("id",None)
        video_title = info_dict.get("title", None)
        downloaded_format_id = info_dict.get('format_id', None)

    if video_id and downloaded_format_id:
        print(f"Video '{video_title}' 成功下載最高解析度影片")
        print(f"Video ID:{video_id}")
        print(f"Downloaded format itag:{downloaded_format_id}")

except Exception as e:
    print(f"An unexpected error occured:{e}")


