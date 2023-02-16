from pytube import YouTube


def downloader (url):

    my_video = YouTube(url)

    print(" -- the title of the video is -- " + my_video.title)

    my_video = my_video.streams.get_highest_resolution()

    print("your video is being downlaoded ...")

    my_video.download()


