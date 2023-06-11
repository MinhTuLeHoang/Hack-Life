from moviepy.editor import VideoFileClip


VID_PATH = "~/Desktop/demo/part1.mov"

videoClip = VideoFileClip(VID_PATH)
videoClip.write_gif("~/Desktop/demo/part1.gif")