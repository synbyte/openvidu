import asyncio

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import deepgram, silero, openai

import requests
#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
#https://api.groq.com/openai/v1
# Define a class for Groq LLM
class GroqLLM:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def chat(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'mixtral-8x7b-32768',
            'prompt': prompt
        }
        response = requests.post(self.api_url + 'completions', headers=headers, json=data)
        return response.json()['choices'][0]['text']

# Define a class for Groq TTS
class GroqTTS:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def synthesize_speech(self, text):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'text': text
        }
        response = requests.post(self.api_url + 'synthesize', headers=headers, json=data)
        return response.content

# This function is the entrypoint for the agent.
async def entrypoint(ctx: JobContext):
    # Create an initial chat context with a system prompt
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
        ),
    )

    # Connect to the LiveKit room
    # indicating that the agent will only subscribe to audio tracks
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Initialize Groq LLM and TTS
    groq_llm = GroqLLM(api_key='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', api_url='https://api.groq.com/v1/')
    groq_tts = GroqTTS(api_key='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', api_url='https://api.groq.com/v1/')

    # VoiceAssistant is a class that creates a full conversational AI agent.
    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=deepgram.STT(),
        llm=groq_llm,
        tts=groq_tts,
        chat_ctx=initial_ctx,
    )

    # Start the voice assistant with the LiveKit room
    assistant.start(ctx.room)

    await asyncio.sleep(1)

    # Greets the user with an initial message
    await assistant.say("Hey, how can I help you today?", allow_interruptions=True)


if __name__ == "__main__":
    # Initialize the worker with the entrypoint
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
