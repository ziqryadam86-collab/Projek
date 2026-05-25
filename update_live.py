import subprocess
import urllib.request
import time
import os

# Masukkan pautan siaran langsung YouTube anda di sini
youtube_url = "https://www.youtube.com/watch?v=HgWz05AsLxw"

def kemaskini_dan_push():
    try:
        print("Mengambil pautan m3u8 menggunakan yt-dlp...")
        m3u8_link = subprocess.check_output(["yt-dlp", "-g", "-f", "best", youtube_url]).decode("utf-8").strip()
        
        print("Muat turun isi kandungan m3u8...")
        req = urllib.request.Request(
            m3u8_link, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            m3u8_content = response.read().decode('utf-8')
        
        with open("stream.m3u8", "w", encoding="utf-8") as f:
            f.write(m3u8_content)
        print("Fail stream.m3u8 berjaya dikemaskini lokal.")

        # Konfigurasi Git menggunakan token keselamatan repo
        repo = os.environ.get('GITHUB_REPOSITORY')
        token = os.environ.get('GITHUB_TOKEN')
        remote_url = f"https://x-access-token:{token}@github.com/{repo}.git"

        os.system('git config --global user.name "github-actions[bot]"')
        os.system('git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"')
        os.system(f'git remote set-url origin {remote_url}')
        os.system('git add stream.m3u8')
        
        # Sila commit dan push terus tanpa semakan quiet
        status = os.system('git commit -m "Auto-update stream.m3u8" && git push origin main')
        
        if status == 0:
            print("Berjaya tolak fail ke GitHub!")
        else:
            print("Gagal melakukan push atau tiada perubahan.")

    except Exception as e:
        print(f"Ralat berlaku dalam fungsi: {e}")

# Memulakan pusingan
for i in range(28):
    print(f"\n--- Pusingan ke-{i+1} ---")
    kemaskini_dan_push()
    print("Menunggu 2 minit...")
    time.sleep(120)
            
