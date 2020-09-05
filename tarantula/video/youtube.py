from pytube import Playlist, YouTube, Stream
from typing import Dict, List, Optional
from datetime import datetime
import logging
import os

class YouTube(object):  
    
    # Scrap video or by videolist
    def __init__(self, input_file: str, options: Optional[Dict[str, bool]] = {"vinlist": True}):
        super().__init__()
        self.vinlist = []
        self.vin = []
        if "vlist" in options:
            self.vinlist = self.load_video_list(input_file)
        else:
            self.vin = self.load_video_list(input_file)
    
    def load_video_list(self, input_file: str) -> List[str]:
        v_list = list()
        with open(input_file) as video_list:
            for i in video_list.readlines():
                v_list.append(i)

        video_list.close()
        return v_list

    def download_video_list(self, out_dir="./out/"):
        for v in self.vinlist:
            playlist = Playlist(url=v)
            dir_name = playlist.playlist_id
            try: 
                os.mkdir(f'{os.getcwd()}/logs/{dir_name}')
                logging.basicConfig(filename=f'{os.getcwd()}/logs/{dir_name}/downloadlist-{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.log', \
                                    level=logging.DEBUG)
            except FileNotFoundError as fe:
                print(fe)
            
            for i, video in enumerate(playlist.videos):
                logging.info(f"{i}th video on {video.title}: {video.description}")
                print(f"{i}th video on {video.title}")
                video.register_on_progress_callback(self.show_progress_bar)
                video.streams.get_highest_resolution().download(f"{os.getcwd()}/out/{dir_name}")


    def show_progress_bar(self, stream: Stream, chunk: bytes, bytes_remaining: int):
        return
