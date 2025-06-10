import subprocess
import sys
import os
from pathlib import Path


def run_ytdlp(url, ytdlp_path="yt-dlp.exe"):
    """
    Run yt-dlp for a single URL
    
    subprocess.run -> takes in path of yt-dlp, url of video
    capture_output = True  (captures error message by initialising
    subprocess.CalledProcessError)

    tries to download, if you get non-zero exit path(check=True)
    then we return false, print failed

    **subprocess.run([ytdlp_path, url]) just runs this on the command line:
    yt-dlp.exe url
    """
    try:
        print(f"Downloading: {url}")
        result = subprocess.run([ytdlp_path, url],


                                text=True,
                                check=True)
        print(f"Successfully Downloaded {url}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to Download {url}: {e}")
        return False
    except FileNotFoundError:
        print(f"yt-dlp not found at: {ytdlp_path}")
        return False


def download_from_lists(urls, ytdlp_path = "yt-dlp.exe"):
    """Download multiple URLs"""
    successful = 0
    failed = 0

    print(f"Starting download of {len(urls)} URLs...\n")
    #All the below code is just aesthetics, the main job has been done in run_ytdlp
    for i, url in enumerate(urls, 1): # (iterable, start_count)
        #print progress:
        print(f"[{i}/{len(urls)}] ", end="")
        if run_ytdlp(url.strip(), ytdlp_path):
            successful+= 1
        else:
            failed += 1

    print("Download Summary:")
    print(f"Successful: {successful}")
    print(f"failed: {failed}")


def main():
    #Option1: Hardcoded URLs:
    urls = [
        "https://www.youtube.com/watch?v=e44hXvuy3OA&pp=ygUac3RhbmR1cCBjb21lZHkgb3ZlciAxIGhvdXI%3D=VIDEO_ID_1",
        "https://www.youtube.com/watch?v=GXYprZmOu9A&pp=ygUac3RhbmR1cCBjb21lZHkgb3ZlciAxIGhvdXLSBwkJsgkBhyohjO8%3D=VIDEO_ID_2",
        "https://www.youtube.com/watch?v=PPjYWaqCffQ&pp=ygUac3RhbmR1cCBjb21lZHkgb3ZlciAxIGhvdXI%3D=VIDEO_ID_3"
    ]

    #Option2: Read URL form file(text file)

    urls_file = "urls.txt"
    if os.path.exists(urls_file):
        print(f"Found{urls_file}, reading URLs from file...")
        with open(urls_file, 'r') as file:
            #basically iterative over lines, making sure line not empty string check: if line.strip()
            file_urls = [line.strip() for line in file if line.strip()]
        if file_urls:
            urls = file_urls
    #Option3: Interactive Input:

    #the bottom if statement takes in input, checks if input taken
    if not urls or input("Enter URLs interactively? (y/n): ").lower() == 'y':
        urls = []
        print("Enter URLs (press Enter twice to finish)")
        #keep asking for urls:
        while True:
            url = input("URL: ").strip()  #removes white spaces before and after
            if not url:
                break
            urls.append(url)
    if not urls:
        print("No URLs provided")
        return

    #check if yt-dlp exists in current directory
    ytdlp_path = "yt-dlp.exe"
    if not os.path.exists(ytdlp_path):
        """
        # Try without .exe extension (for non-Windows or pip installed)
        ytdlp_path = "yt-dlp"
        if not os.path.exists(ytdlp_path):
        """
        pass

    download_from_lists(urls, ytdlp_path)

    input("Press Enter to Exit...")

if __name__ == "__main__":
    main()
