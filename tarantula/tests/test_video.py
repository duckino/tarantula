from tarantula.video.youtube import YouTube
import os
import shutil

if __name__ == "__main__":
    yt = YouTube(input_file = "./jobs/videoinlist.txt", options = {"vlist": True})
    yt.download_video_list()
    shutil.make_archive("test_video", 'zip', f"{os.getcwd()}")