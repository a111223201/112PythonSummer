import yt_dlp

URLs= ['https://youtu.be/EhS9lPrrLK8?si=eflbZYivB87cuezl',
       'https://youtu.be/rK2kXg9tpdQ?si=5ChUyQWew_mTq3GR',
       'https://youtu.be/_UD4zyHx0cw?si=6zwhOnzyrhY5NicY',
       'https://youtu.be/0JLS35L6hwM?si=5gTZDQ--gycp5Po7'      
]
DIR = 'C:\\Youtube'


for URL in URLs:
    ydl_opts = {
        'format': 'worst',
        'outtmpl': f'{DIR}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(URL,download=True)
            video_id = info_dict.get("id",None)
            video_title = info_dict.get("title", None)
            downloaded_format_id = info_dict.get('format_id', None)

        if video_id and downloaded_format_id:
            print(f"Video '{video_title}' 成功下載最低解析度影片")
            print(f"Video ID:{video_id}")
            print(f"Downloaded format itag:{downloaded_format_id}")

    except Exception as e:
        print(f"An unexpected error occured:{e}")


