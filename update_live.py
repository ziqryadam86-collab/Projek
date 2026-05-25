
    
from flask import Flask, redirect
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server IPTV Maharaja Adam sedang aktif!"

@app.route('/live')
def play_live():
    # ID video YouTube Live Alan Becker
    video_id = "HgWz05AsLxw"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    try:
        # Ekstrak pautan segar secara masa nyata di pelayan Render
        live_url = subprocess.check_output(["yt-dlp", "-g", "-f", "best", youtube_url]).decode("utf-8").strip()
        return redirect(live_url, code=302)
    except Exception as e:
        return f"Ralat: {e}", 500

if __name__ == '__main__':
    # Mengikut port yang ditetapkan oleh Render secara automatik
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
