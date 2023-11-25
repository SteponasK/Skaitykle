from google.cloud import texttospeech
import os

if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
    print(f"Credentials file path: {os.environ['GOOGLE_APPLICATION_CREDENTIALS']}")
else:
    print("GOOGLE_APPLICATION_CREDENTIALS is not set.")

client = texttospeech.TextToSpeechClient()

input_text = "Ką daryt kai taves nemyli niekas, o tu taip visus myli"

synthesis_input = texttospeech.SynthesisInput(text=input_text)

voice = texttospeech.VoiceSelectionParams(
    language_code="lt-LT",
    name = "lt-LT-Standard-A",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

output_file = "output.wav"
with open(output_file, "wb") as out:
    out.write(response.audio_content)


print(f"Audio content written to {output_file}")