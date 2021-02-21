
for /r ./ %%i in ("*.avi") do (
	"ffmpeg.exe" -i %%~fi -c:v h264 -crf 20 -preset veryslow -movflags +faststart -pix_fmt yuv420p -an %%~ni.mp4
)
