# Download
- youtube-dl: Downloader for various videos. Installed e.g. as python application via pip.
- yt-dlp: Fork from youtube-dl. Installed best via the binary, placed inside .local/bin
```bash
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o ~/.local/bin/yt-dlp
chmod a+rx ~/.local/bin/yt-dlp  # Make executable
```
Download Audio only:
```bash
yt-dlp -x url #paste url without any surrounding hyphens
```