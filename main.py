from Yt import YouTubeDL, os
import shutil

if __name__ == "__main__":
    ytdl = YouTubeDL(input_file = "./jobs/videoinlist.txt", options = {"vlist": True})
    ytdl.download_video_list()
    shutil.make_archive("renmindeminyi", 'zip', f"{os.getcwd()}")