# YouTube Video Downloader and Merger

This project allows you to download YouTube videos and audio, then merge them into a single file with your desired output format.

## Prerequisites

- Python 3.x installed on your system
- `pytube` and `moviepy` Python libraries

## Setting Up the Project

### Windows

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the batch file to create a virtual environment, install dependencies, and execute the script:

    ```batch
    run_yt_window.bat
    ```

    ```batch
    @echo off
    cd /d "%~dp0" 

    IF NOT EXIST env (
        echo Creating virtual environment...
        python -m venv env
    )

    call env\Scripts\activate.bat

    pip install -r requirements.txt

    python python.py

    pause
    ```

### Mac and Linux

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Make sure the `setup.sh` file has execute permissions. You can set the execute permissions using the following command:

    ```sh
    chmod +x run_yt_mac_or_linux.sh
    ```

4. Run the shell script to create a virtual environment, install dependencies, and execute the script:

    ```sh
    ./run_yt_mac_or_linux.sh
    ```

    ```sh
    #!/bin/bash

    cd "$(dirname "$0")"

    if [ ! -d "env" ]; then
        echo "Creating virtual environment..."
        python3 -m venv env
    fi

    source env/bin/activate

    pip install -r requirements.txt

    python3 python.py
    ```

## Usage

1. Once the script is running, you will be prompted to enter the YouTube video URL.
2. The script will display available video and audio streams. Choose the desired streams by entering the corresponding numbers.
3. After downloading, you will be prompted to choose the output format (`mp4` or `webm`).
4. The script will merge the downloaded video and audio files and save the output file in the chosen format.
5. You can choose to download more videos or exit the script.

## Example

```sh
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

Available streams for Rick Astley - Never Gonna Give You Up (Official Music Video):
...
Enter the number corresponding to the desired video stream: 1
Enter the number corresponding to the desired audio stream: 1

Downloading...
...

Enter which extension output you need '1: mp4' or '2: webM': 1
Merging complete!

Enter 1 to continue or 2 to exit: 2
