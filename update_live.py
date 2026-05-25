import subprocess
import os

# Sini tempat letak nama dan ID Live YouTube anda
streams = {
    "Alan_Becker_TV": "HgWz05AsLxw"
}

try:
    m3u_content = "#EXTM3U\n"
    
    for name, video_id in streams.items():
        # Menggunakan format URL YouTube rasmi yang betul
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"Mengambil pautan m3u8 untuk {name}...")
        
        # Jalankan yt-dlp untuk dapatkan URL m3u8 segar
        live_url = subprocess.check_output(["yt-dlp", "-g", "-f", "best", youtube_url]).decode("utf-8").strip()
        
        # Menyusun format senarai main IPTV (.m3u)
        m3u_content += f'#EXTINF:-1 tvg-name="{name}" logo="", {name}\n{live_url}\n'
    
    # Menyimpan senarai main ke dalam fail live.m3u secara lokal
    with open("live.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print("Fail live.m3u berjaya dicipta!")

    # Memulakan proses automatik Git Push ke GitHub
    repo = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GITHUB_TOKEN')
    remote_url = f"https://x-access-token:{token}@github.com/{repo}.git"

    os.system('git config --global user.name "github-actions[bot]"')
    os.system('git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"')
    os.system(f'git remote set-url origin {remote_url}')
    os.system('git add live.m3u')
    os.system('git commit -m "Auto-update IPTV live.m3u" && git push origin main')
    print("Tahniah! Fail live.m3u berjaya dihantar ke GitHub!")

except Exception as e:
    print(f"Ralat berlaku: {e}")
    
