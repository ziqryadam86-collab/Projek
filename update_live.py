import subprocess
import urllib.request

# Masukkan URL YouTube Live yang anda mahukan
youtube_url = "https://www.youtube.com/watch?v=HgWz05AsLxw"

try:
    # 1. Guna yt-dlp untuk dapatkan pautan m3u8 yang sebenar dari YouTube
    print("Sedang mengambil pautan m3u8 dari YouTube...")
    m3u8_link = subprocess.check_output(["yt-dlp", "-g", youtube_url]).decode("utf-8").strip()
    
    # 2. Muat turun isi kandungan (content) daripada pautan m3u8 tersebut
    print("Sedang menyalin kandungan m3u8...")
    req = urllib.request.Request(
        m3u8_link, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        m3u8_content = response.read().decode('utf-8')
    
    # 3. Simpan kandungan tersebut ke dalam fail 'stream.m3u8'
    with open("stream.m3u8", "w", encoding="utf-8") as f:
        f.write(m3u8_content)
        
    print("Fail stream.m3u8 berjaya dikemaskini!")

except Exception as e:
    print(f"Ralat berlaku: {e}")
      
