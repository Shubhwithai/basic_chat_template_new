# 🗣️ Conversational Chatbot

A modern conversational chatbot built with Streamlit and LangChain, powered by Together AI's LLM models.

## Features

- 💬 Interactive chat interface with message history
- 🧠 Powered by Meta's Llama 4 Maverick model via Together AI
- 🔄 Conversation memory using LangChain's latest patterns
- 🎨 Clean and intuitive UI built with Streamlit
- 🔒 Secure API key management with Streamlit secrets

## Tech Stack

- **Frontend**: Streamlit
- **LLM Framework**: LangChain (latest version)
- **LLM Provider**: Together AI
- **Model**: meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
- **Python**: 3.8+

## Prerequisites

- Python 3.8 or higher
- Together AI API key ([Get one here](https://api.together.xyz/))

## Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd chatbot_Course
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   - Open `.streamlit/secrets.toml`
   - Replace `your-together-api-key-here` with your actual Together AI API key:
     ```toml
     TOGETHER_API_KEY = "your-actual-api-key-here"
     ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the chatbot**:
   - The app will automatically open in your browser
   - Default URL: `http://localhost:8501`

3. **Start chatting**:
   - Type your message in the chat input at the bottom
   - Press Enter to send
   - The AI will respond with context from your conversation history

## Project Structure

```
chatbot_Course/
├── app.py                      # Main application file
├── requirements.txt            # Python dependencies
├── .streamlit/
│   └── secrets.toml           # API keys (not committed to git)
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## Configuration

### Changing the LLM Model

To use a different model, modify the `llm` initialization in `app.py`:

```python
llm = ChatOpenAI(
    model="your-model-name",  # Change this
    api_key=st.secrets["TOGETHER_API_KEY"],
    base_url="https://api.together.xyz/v1",
    temperature=0.7  # Adjust temperature (0.0 - 1.0)
)
```

### Using OpenAI Instead

1. Update `requirements.txt` to include OpenAI support
2. Add your OpenAI API key to `.streamlit/secrets.toml`:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   ```
3. Update the LLM initialization:
   ```python
   llm = ChatOpenAI(
       model="gpt-4o-mini",
       api_key=st.secrets["OPENAI_API_KEY"]
   )
   ```

### Adjusting Conversation Memory

The chatbot uses `InMemoryChatMessageHistory` to maintain conversation context. To limit the number of messages remembered, you can implement a custom message history with a window size.

## Key Features Explained

### Modern LangChain Implementation

This project uses the latest LangChain patterns:
- ✅ `RunnableWithMessageHistory` for conversation management
- ✅ `ChatPromptTemplate` with `MessagesPlaceholder` for structured prompts
- ✅ LCEL (LangChain Expression Language) with the `|` operator
- ✅ Proper session management with configurable session IDs

### No Deprecated Code

All deprecated imports and patterns have been removed:
- ❌ No `ConversationChain`
- ❌ No `ConversationBufferWindowMemory`
- ✅ Uses modern `langchain_core` components

## Security

⚠️ **Important**: Never commit your `.streamlit/secrets.toml` file to version control. It's already included in `.gitignore` to prevent accidental exposure of API keys.

## Troubleshooting

### Model Not Available Error

If you see an error about the model not being available:
1. Check that your Together AI API key is valid
2. Verify the model name is correct and available
3. Some models require a dedicated endpoint - check the Together AI dashboard

### Import Errors

If you encounter import errors:
```bash
pip install --upgrade langchain langchain-openai streamlit
```

## Dependencies

- `langchain` - LLM framework
- `langchain-openai` - OpenAI-compatible LLM integration
- `streamlit` - Web interface
- `streamlit-chat` - Chat UI components

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://www.langchain.com/)
- LLM by [Together AI](https://www.together.ai/)
- Tutorial by Build Fast with AI

## Support

For questions or issues:
1. Check the [LangChain documentation](https://python.langchain.com/)
2. Review [Streamlit documentation](https://docs.streamlit.io/)
3. Visit [Together AI documentation](https://docs.together.ai/)

---

**Happy Chatting! 🚀**
