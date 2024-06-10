from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import sys, os
import time

def print_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    total_size_mb = total_size / (1024 * 1024)
    downloaded_mb = bytes_downloaded / (1024 * 1024)
    sys.stdout.write("\rDownloading... {:.2f}% ({:.2f} MB / {:.2f} MB)".format(progress, downloaded_mb, total_size_mb))
    sys.stdout.flush()

def download_video(url):
    try:
        yt = YouTube(url, on_progress_callback=print_progress)
        streams = yt.streams.all()
        video_streams = []
        audio_streams = []
        
        for stream in streams:
            if stream.type == "video":
                video_streams.append(stream)
            elif stream.type == "audio":
                audio_streams.append(stream)

        print(f"\nAvailable streams for {yt.title}:")
        print("\nType : Video →")
        for i, stream in enumerate(video_streams, start=1):
            total_size_mb = stream.filesize / (1024 * 1024)
            format_ = stream.mime_type.split("/")[-1]
            print(f"{i}. Resolution: {stream.resolution}, Type: {format_}, MB: {total_size_mb:.2f}")

        print("\nType : Audio →")
        for i, stream in enumerate(audio_streams, start=1):
            total_size_mb = stream.filesize / (1024 * 1024)
            format_ = stream.mime_type.split("/")[-1]
            print(f"{i}. Type: {format_}, MB: {total_size_mb:.2f}")

        while True:
            try:
                
                video_choice = int(input("\nEnter the number corresponding to the desired video stream: "))  
                if video_choice <= 0 or video_choice > len(video_streams) :
                    print("\nInvalid choice. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                
        while True:
            try:
                audio_choice = int(input("Enter the number corresponding to the desired audio stream: "))
                if audio_choice <= 0 or audio_choice > len(audio_streams):
                    print("\nInvalid choice. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("\nInvalid input. Please enter a number.")
            

        print("\nDownloading...")
        time.sleep(1)  # Add a short delay for a smoother experience
        video_stream = video_streams[video_choice - 1]
        audio_stream = audio_streams[audio_choice - 1]
        video_filename = 'video.mp4'
        audio_filename = 'audio.mp4'
        video_stream.download(filename=video_filename)
        audio_stream.download(filename=audio_filename)
        print("\nDownload complete!")
        
        # Merge video and audio files
        userLoop = True
        while userLoop:
            user_out = input("\nEnter which extension output you need '1: mp4' or '2: webM': ")
            dic = {"1": "mp4", "2": "webm"}

            if user_out in dic:
                userLoop = False
                output_format = dic[user_out]
                if output_format == 'mp4':
                    codec = 'libx264'
                elif output_format == 'webm':
                    codec = 'libvpx' if sys.platform != 'win32' else 'libvpx-vp9'  # Use different codec for Windows
                merge_video_audio(video_filename, audio_filename, f'{yt.title}.{output_format}', codec)
            else:
                print("Invalid choice. Please enter either '1' or '2' for the desired output format.")
                
        
        # Clean up downloaded files
        os.remove(video_filename)
        os.remove(audio_filename)

    except Exception as e:
        print(f"\nError downloading video: {e}")
        return False
    
    return True

def merge_video_audio(video_filename, audio_filename, output_filename, codec):
    try:
        video_clip = VideoFileClip(video_filename)
        audio_clip = AudioFileClip(audio_filename)

        # Ensure the audio duration matches the video duration
        audio_clip = audio_clip.set_duration(float(video_clip.duration))

        # Combine video and audio
        final_clip = video_clip.set_audio(audio_clip)

        # Write the result to a new file
        final_clip.write_videofile(output_filename, codec=codec)

        print("Merging complete!")
    except Exception as e:
        print(f"\nError merging video and audio: {e}")

if __name__ == "__main__":
    mainDfLoop = True
    while mainDfLoop:
        print("\n«««««««««««   YouTube Video Downloader and Merger  »»»»»»»»»»»»»»\n")
        video_url = input("Enter the YouTube video URL: ")
        completed = download_video(video_url)
        
        while True:
            if completed:
                choice = input("Enter 1 to continue or 2 to exit: ")
            else:
                print("Enter a Valid Link........\nExample like this 'https://www.youtube.com/watch?v=m7-rtybEtrt'")
                break
                
            if choice == '1':
                break  # Continue downloading more videos
            elif choice == '2':
                mainDfLoop = False  # Exit the main loop
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

