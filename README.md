# AI Voice Assistant 🤖🎤

A smart voice assistant built with LiveKit Agents that can control temperature in different rooms through natural voice commands.

## Features ✨

- **Voice Interaction**: Natural speech-to-text and text-to-speech using OpenAI
- **Temperature Control**: Get and set temperature for different rooms
- **Multi-room Support**: Control temperature in living room, bedroom, kitchen, bathroom, and office
- **Real-time Communication**: Uses LiveKit for real-time voice interaction

## Supported Commands 🗣️

### Get Temperature
- "What's the temperature in the bedroom?"
- "Check the living room temperature"
- "How warm is the kitchen?"

### Set Temperature
- "Set the bedroom temperature to 25 degrees"
- "Change the kitchen temperature to 18"
- "Make the living room 23 degrees"

## Setup Instructions 🛠️

### Prerequisites
- Python 3.11+
- LiveKit Cloud account
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-Voice-Assistant.git
   cd AI-Voice-Assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv ai
   .\ai\Scripts\activate  # Windows
   # or
   source ai/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file with your credentials:
   ```
   LIVEKIT_URL=wss://your-livekit-url.livekit.cloud
   LIVEKIT_API_KEY=your-livekit-api-key
   LIVEKIT_API_SECRET=your-livekit-api-secret
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Run the application**
   ```bash
   python main.py start
   ```

## Project Structure 📁

```
AI-Voice-Assistant/
├── main.py              # Main application entry point
├── api.py               # Temperature control API functions
├── .env                 # Environment variables (not tracked)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## How It Works 🔧

1. **Voice Input**: Uses OpenAI's Speech-to-Text (STT) to convert voice to text
2. **AI Processing**: OpenAI's LLM processes the command and determines the action
3. **Function Execution**: Executes temperature control functions based on the command
4. **Voice Output**: Uses OpenAI's Text-to-Speech (TTS) to respond with voice

## Room Zones 🏠

The assistant supports temperature control for:
- Living Room
- Bedroom
- Kitchen
- Bathroom
- Office

## Technologies Used 🚀

- **LiveKit Agents**: Real-time voice interaction framework
- **OpenAI API**: Speech-to-text, language model, and text-to-speech
- **Silero VAD**: Voice activity detection
- **Python 3.11**: Core programming language

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Support 💬

If you encounter any issues or have questions, please create an issue in this repository.

---

**Built with ❤️ using LiveKit Agents and OpenAI**