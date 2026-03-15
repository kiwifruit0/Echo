# Echo: The Voice-First Social Network

## Inspiration
Social media glues us to screens. We wanted the community depth of Reddit and the raw authenticity of BeReal, but completely hands-free. Echo is designed to help you stay connected while walking, cooking, or driving; without ever looking at a phone.

## What it does
Echo is a voice-only social platform that turns your social feed into a personalized daily podcast.
-   Daily Briefing: Instead of doom-scrolling, an AI host narrates your friends' updates and interesting forum discussions.
-   Voice Forum: Ask questions and answer others using just your voice.
-   Interactive 3D: A "living" interface featuring a reactive Audio Ring and Friends Graph that react to your speech in real-time.

## How we built it
We combined a visually interesting 3d frontend with a Python FastAPI backend:
-   Frontend: Built with React and Tailwind css. We used custom shaders to create the audio-reactive visualizers.
-   Backend: FastAPI (Python) and MongoDB manage the data flow.
-   AI Engine:
    -   Google Gemini: The "brain" that categorizes voice queries, summarizes daily activities, and determines user intent.
    -   ElevenLabs: The "voice" that provides ultra-low latency Speech-to-Text and natural Text-to-Speech.

## Challenges we faced
*   Latency: Making the voice interaction feel instant and conversational required optimizing the pipeline between ElevenLabs and our backend.
*   3D Integration: Seamlessly blending the HTML UI with the 3D canvas so users could interact with the "Friends Graph" naturally.

## Accomplishments that we're proud of
*   The "Daily Summary": It genuinely feels like listening to a radio station dedicated to your friend group.
*   Reactive Visuals: The way the interface breathes and distorts with the user's volume creates a deeply immersive experience.
