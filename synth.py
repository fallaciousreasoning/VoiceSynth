import boto3

client = boto3.client('polly')

response = client.describe_voices()
voices = response['Voices']
english_voices = [x for x in voices if x.]
for voice in voices:
    print(voice)