# srt_sub_extract

Extract srt subtitles from mkv videos with mkvextract, and name srts with mkv filenames.

No need for other python packages.

## - mkvextract command in python style:
**mkvextract** src_video_path **tracks** track_id:dst_srt_path [track_id_1:dst_srt_path_1 ...]

## - raw mkvextract command:
**mkvextract** source-filename **tracks** [options] TID1:dest-filename1 [TID2:dest-filename2 ...]

## - about mkvextract:
Currently supported is the extraction of tracks, tags, attachments, chapters, CUE sheets, timestamps and cues.

PS: mkxextract.exe is for windows system.

Download other system version or see more about mkvextarct at https://mkvtoolnix.download/doc/mkvextract.html
