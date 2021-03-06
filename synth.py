import boto3
from extracttext import get_chapters
import random

client = boto3.client('polly')

def get_voice():
    """Gets the voice we want from Amazon"""

    # TODO: not even this...
    english_regions = ['en-AU', 'en-GB', 'en-US']
    voices = []
    for region in english_regions:
        response = client.describe_voices(LanguageCode=region)
        for voice in response['Voices']
            voices.append(voice['Id'])

    return random.choice(voices)

def synth_book(text, voice, output_file):

    response = client.synthesize_speech(OutputFormat='mp3', 
    Text=text, VoiceId=voice, TextType='text')
    
    content_stream = response['AudioStream']

    # Write the generated text to the disk
    with open(output_file, 'wb') as f:
        # This is probably not my best moment
        f.write(content_stream.read())

if __name__ == '__main__':
    output_file = "output.mp3"
    book = get_chapters('The Autumn Republic.epub')
    chapter = book[4] # First actual text chapter, not contents/acknowledgments
    text = '\n'.join(chapter[2:10]) # Don't send too much text to Amazon, they don't like it

    voice = get_voice() # Get our Australian voice from Amazon

    synth_book(text, voice, output_file) # Generate our voice and save it to disk
    print('Synthesized', output_file)

