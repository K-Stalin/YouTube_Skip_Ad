import speech_recognition as sr
import pyautogui
import time

# Time to wait before skipping the ad
SKIP_AD_WAIT_TIME = 0.5


# Function to skip the ad
def skip_ad():
    x, y = 1212, 830  
    pyautogui.moveTo(x, y)  # to locate the cursor in x and y axis
    time.sleep(SKIP_AD_WAIT_TIME)
    pyautogui.click()
    print("Skip Ad")


def listen_for_hotword():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Hey YouTube' to skip ads...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        if "alexa" in command:
            print("Hotword detected! Skipping ad...")
            skip_ad()
    except sr.UnknownValueError:
        print("Didn't catch that. Try again.")
    except sr.RequestError:
        print("Error connecting to speech service.")



while True:
    listen_for_hotword()