'''Extract srt subtitles from mkv videos with mkvextract, and name srts with mkv names.
cmd: mkvextract source-filename tracks [options] TID1:dest-filename1 [TID2:dest-filename2 ...]
see more about mkvextarct at https://mkvtoolnix.download/doc/mkvextract.html
'''

import os


# setting
video_dir = '.\Modern.Family'  # replace with your video dir pls


# collact all mkv video paths
video_paths = []
for root, dirs, files in os.walk(video_dir):
    for file in files:
        if file.endswith('mkv'):
            video_paths.append(os.path.join(root, file))


# extract srt subtitles via mkvextract
for video_path in video_paths:
    track_id = 2  # replace with your specific tracj_id, default: video=0, audio=1, text(subtitle)=2.
    os.system('mkvextract {} tracks {}:{}\n'.format(video_path, track_id, video_path.replace('.mkv', '.srt')))