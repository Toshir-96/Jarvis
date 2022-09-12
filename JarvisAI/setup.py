import setuptools
from setuptools import find_namespace_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="JarvisAI",
    version="4.0",
    author="Dipesh",
    author_email="dipeshpal17@gmail.com",
    description="JarvisAI is python library to build your own AI virtual assistant with natural language processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dipeshpal/Jarvis_AI",
    include_package_data=True,
    packages=find_namespace_packages(include=['JarvisAI.*', 'JarvisAI']),
    install_requires=['numpy', 'gtts', 'playsound', 'pyscreenshot', "opencv-python",
                      'SpeechRecognition', 'pipwin', 'lxml', 'pyjokes',
                      'beautifulsoup4', 'wikipedia', 'scipy', 'download',
                      "torch", 'lazyme', "requests", "pyttsx3", "googlesearch-python",
                      "spacy", 'textdistance', 'pywhatkit', "googlesearch-python",
                      "youtube-search-python", "shutup", 'Flask', 'speedtest-cli',
                      'pytube', 'pycountry', 'phonetics', 'fuzzywuzzy', 'googletrans', 'wave',
                      'deepspeech', 'webrtcvad', 'halo', 'playsound==1.2.2', 'pyaudio'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/Dipeshpal/Jarvis_AI',
        'Donate': 'https://www.buymeacoffee.com/dipeshpal',
        'Say Thanks!': 'https://youtube.com/techportofficial',
        'Source': 'https://github.com/Dipeshpal/Jarvis_AI',
    },
)
