# to get the audio from some sources :)

import os
import yt_dlp

def download_universal_audio(video_url, output_dir="downloads"):
    """
    downloads a low quality audio to pass it to the ai
    """

    # make a folder (dir) for it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"\n[+] Analyzing link: {video_url}")
    print("[+] Fetching audio streams...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s', 
        
        'quiet': False,
        'no_warnings': True,
        'ignoreerrors': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            if info is None:
                return None
            filename = ydl.prepare_filename(info)
            return filename
            
    except Exception as e:
        print(f"[X] Downloading error: {e}")
        return None

if __name__ == "__main__":
    print("🎵 TalkToVidBrain - Core Component: Universal Audio Downloader")
    
    test_url = "https://youtu.be/xXgtokSlIgM"
    
    audio_path = download_universal_audio(test_url)
    
    if audio_path and os.path.exists(audio_path):
        print(f"\nSuccess! Audio saved at: {audio_path}")
    else:
        print("\nFailed to download audio from this platform.")
