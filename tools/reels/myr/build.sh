#!/bin/bash
set -e
cd /tmp/claude-0/newreels/myr
RAW=/tmp/claude-0/newreels/my_raw.mp4
seg(){ # $1 caption png, $2 start, $3 dur, $4 out
  ffmpeg -v error -y -loop 1 -framerate 30 -t $3 -i $1 -ss $2 -t $3 -i $RAW -i mask.png -filter_complex "[1]scale=776:1380,setsar=1[v];[2]format=gray[m];[v][m]alphamerge[vm];[0][vm]overlay=152:500,format=yuv420p" -t $3 -r 30 -c:v libx264 -crf 18 $4
}
seg png/c0.png 0.3 3.4 s_c0.mp4
seg png/c1.png 4.6 6.2 s_c1.mp4
seg png/c2.png 15.9 3.7 s_c2.mp4
seg png/c3.png 20.5 8.0 s_c3.mp4
seg png/c4.png 35.4 6.3 s_c4.mp4
seg png/c5.png 42.5 5.0 s_c5.mp4
seg png/c6.png 47.5 3.5 s_c6.mp4
seg png/c7.png 51.0 4.0 s_c7.mp4
ffmpeg -v error -y -loop 1 -framerate 30 -t 2.4 -i /tmp/claude-0/hl/end-miss-you-new.png -vf "scale=1080:1920,format=yuv420p" -r 30 -c:v libx264 -crf 18 s_end.mp4
printf "file 'seg_hook.mp4'\n" > list.txt; for i in 0 1 2 3 4 5 6 7; do echo "file 's_c$i.mp4'" >> list.txt; done; echo "file 's_end.mp4'" >> list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -c copy video.mp4
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 video.mp4)
ffmpeg -v error -y -i video.mp4 -i /tmp/claude-0/reels/miss-you-synth.wav -filter_complex "[1]atrim=0:$D,afade=t=in:d=0.4,afade=t=out:st=$(python3 -c "print($D-1.6)"):d=1.6,volume=0.9[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart ../littlegasp-miss-you-story-reel.mp4
echo done $D
