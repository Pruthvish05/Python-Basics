import yt_dlp
def download_video(url,name):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/' + name + '.%(ext)s',
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
url = input("Enter the YouTube video URL: ")
name = input("Enter the desired name for the downloaded video (without extension): ")
download_video(url,name)


