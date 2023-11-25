from google.cloud import texttospeech
import os
import PyPDF2


def get_text_string_from_pdf(pdf_path, start_page=0, end_page=None):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        end_page = end_page or len(pdf_reader.pages)
        for page_num in range(start_page, end_page):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def get_pdf_path():
    pdf_path = input(
        r"Iveskite failo lokacija (Pvz.: C:\Users\Vardenis\Atsisiuntimai\Knyga.pdf):  "
    )
    pdf_path = r"{}".format(pdf_path.replace('"', "").strip())
    return pdf_path


def main():
    if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
        print("GOOGLE_APPLICATION_CREDENTIALS nera nustatytas.")
        raise SystemExit(1)

    client = texttospeech.TextToSpeechClient()
    pdf_path = get_pdf_path()
    input_text = r"{}".format(get_text_string_from_pdf(pdf_path))

    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="lt-LT",
        name="lt-LT-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    output_file = "output.mp3"
    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    print(f"Garsas yra irasytas i {output_file}")


if __name__ == "__main__":
    main()
