# Youtube Skip Ad ✨ 



A Python script that listens for a voice command (hotword) and automatically clicks the "Skip Ad" button on YouTube using Speech Recognition and PyAutoGUI.

## Features  
- 🎙 Uses speech recognition to detect a hotword (**"Alexa"**).  
- 🖱 Moves the cursor to the **"Skip Ad"** button location and clicks it.  
- 🔄 Continuously listens for the hotword and **skips ads automatically**.  

## Requirements
- Ensure you have Python installed (Python 3 recommended). Install the required dependencies:
- pip install speechrecognition pyautogui pyaudio

## Usage
- Run the script:
    ```python youtube_ad_skipper.py ```
- The script will listen for the hotword "Alexa".
- When the hotword is detected, it will click the "Skip Ad" button on YouTube.

## Code Explanation
- skip_ad(): Moves the cursor to a predefined location and clicks to skip the ad.
- listen_for_hotword(): Listens for the hotword using speech recognition.
- The script runs in an infinite loop to continuously listen for the hotword and perform the action.

Notes
- Ensure your microphone is working.
- You may need to adjust the x, y coordinates in skip_ad() to match your screen resolution.
- Modify the hotword detection to recognize other phrases if needed.

License
  This project is open-source and available under the MIT License.

🌟Contributing
  Feel free to submit pull requests or report issues to improve the project!

## Connect with Me  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Stalin%20K-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/k-stalin/)
