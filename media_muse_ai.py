from transformers import pipeline
from PIL import Image
import numpy as np
import requests
from bs4 import BeautifulSoup
from gtts import gTTS

def generate_article(prompt, max_length=500):
    generator = pipeline('text-generation', model='gpt2', tokenizer='gpt2')
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text']

def generate_image(prompt):
    image_array = np.random.rand(256, 256, 3) * 255
    image = Image.fromarray(image_array.astype('uint8')).convert('RGB')
    return image

def get_trending_topics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    topics = []
    for topic in soup.find_all('a', class_='trending_topic_link'):
        topics.append(topic.get_text())
    return topics

def generate_audio(text):
    tts = gTTS(text, lang='en')
    tts.save('output.mp3')
    return 'output.mp3'

if __name__ == "__main__":
    prompt = "The impact of AI on modern media"
    article = generate_article(prompt)
    print("Generated Article: ", article)

    image = generate_image(prompt)
    image.show()

    url = "https://example.com/trending"
    trending_topics = get_trending_topics(url)
    print("Trending Topics: ", trending_topics)

    audio_file = generate_audio(article)
    print(f"Generated audio saved as {audio_file}")
