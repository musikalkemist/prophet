# prophet

*prophet* is a command-line application that allows you to have a conversation 
with ChatGPT - the newly released GPT-3 model from OpenAI - with your voice.

## Installation
To install *prophet*, you can use the following command:

```bash
poetry install
```

After installing *poetry*, run the following command:

```bash
python -m playwright install
```

This will install the required browser plugins that enable *prophet* to
connect to ChatGPT via the *revChatGPT* library.


## Dependencies

### Python version
*prophet* requires Python 3.8.

### revChatGPT
*prophet* uses the *revChatGPT* library to interact with the ChatGPT model.

### Setting up Google Cloud Text-To-Speech

*poetry* uses Google Cloud Text-To-Speech to synthesise speech.

In order to be able to use this service, you should:

- create an account on Google Cloud, 
- create a Cloud Platform project, 
- enable the Text-To-Speech API in the project 
- setup authentication 
- download a Json private key

### pydub
*prophet* uses *pydub* to play back MP3 files. You need to install *ffmpeg* to
be able to use MP3s with *pydub*.

On Debian-like machines, you can install *ffmpeg* with the following command:

```bash
$ sudo apt install ffmpeg
```

### SpeechRecognition
*prophet* uses the *SpeechRecognition* library to convert your speech input to 
text. You need to install *portaudio* and its Python bindings (*pyaudio*)
to be able to use *SpeechRecognition*.


## Environment variables
The app uses an environment variable called GOOGLE_APPLICATION_CREDENTIALS to 
connect to Google Cloud Text-To-Speech safely.

In *config.env*, set GOOGLE_APPLICATION_CREDENTIALS to the path of the Json 
private key you previously downloaded while setting up the Google service.

Without this step, you won't be able to connect to Google Cloud Text-To-Speech, 
and the app will throw an error.


## Usage
To run *prophet*, you can use the following command from the terminal:

```bash
$ prophet
```

Once you run this script, you'll be asked to log in to your OpenAI account. 
After logging in, you're good to go. Enjoy your convo with ChatGPT!