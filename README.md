# Vid2pdf
A app tthat uses estimation to convert videos to pdf , it can also add subtitles if srt/vrt file is provided.

# How to use:
   CLone this repository then add your video in the videos folder inside tests folder,
   then run coomand:
  <br> <br>
   python3 -m src.main tests/videos/<vid_name> -s tests/subtitles/<srt filename> -o output.pdf
   <br>
   If you dont want subtitles:<br>
   python3 -m src.main tests/videos/input_4.mp4 -o output.pdf
