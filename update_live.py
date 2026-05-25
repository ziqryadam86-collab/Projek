import urllib.request
import re

video_id = "HgWz05AsLxw"
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

try:
    req = urllib.request.Request(youtube_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.search(r'"hlsManifestUrl":"([^"]+)"', html)

    if matches:
        m3u8_url = matches.group(1).replace(r'\/', '/')
        
        # Di sini kita simpan pautan index.m3u8 YouTube tadi ke fail live.m3u kita sendiri
        m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-name=\"Alan_Becker\", Alan Becker TV Live\n{m3u8_url}\n"
        
        with open("live.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
            
        print("✅ BERJAYA! Fail live.m3u telah dicipta dengan pautan segar!")
    else:
        print("❌ Gagal: Kod hlsManifestUrl tidak ditemui dalam HTML.")
except Exception as e:
    print(f"❌ Ralat berlaku: {e}")
            
