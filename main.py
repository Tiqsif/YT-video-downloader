from pytube import YouTube
from pytube import Playlist

def Download(url):
	yt = YouTube(url)
	title = yt.title
	stream = yt.streams.filter(progressive=True).get_highest_resolution()
	print(f"Video [{title}] is saved to: " + stream.download(output_path=output_file))

#########################################################################################
fromPlaylist = False # if true downloads whole playlist from YT
fromFile = False # if true reads every line of the file as YT links
inputPath = "input.txt"
output_file = "./output"

link = "" # write a link if both fromFile and fromPlaylist are False
playlistLink = ""

if fromPlaylist:
	p = Playlist(playlistLink)
	for url in p.video_urls:
		Download(url)


elif fromFile:
	with open(inputPath, "r") as f:
		for line in f.readlines():
			Download(line)

else:	

	Download(link)


