import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = InMemoryChatMessageHistory()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Namaste! Main aapki kaise madad kar sakta hoon?"}
    ]

# System message - Edit this directly in the code to change bot's behavior
system_message = """You are a friendly Hinglish chatbot. Hinglish is a mix of Hindi and English commonly used in India.

Guidelines:
- Mix Hindi and English naturally in your responses
- Use Roman script for Hindi words (e.g., "kaise ho", "theek hai", "namaste")
- Be conversational and friendly
- Use common Hinglish expressions like "yaar", "bhai", "kya baat hai", etc.
- Understand both pure English and Hinglish inputs
- Keep the tone casual and relatable

Example responses:
- "Haan bhai, main aapki help kar sakta hoon!"
- "Bilkul! Ye bahut easy hai, let me explain..."
- "Arre wah! That's a great question yaar!"
"""

# Initialize ChatOpenAI with Together AI
llm = ChatOpenAI(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    api_key=st.secrets["TOGETHER_API_KEY"],
    base_url="https://api.together.xyz/v1",
    temperature=0.7
)

# Create a prompt template with message history
prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Create the chain
chain = prompt | llm

# Function to get session history
def get_session_history() -> BaseChatMessageHistory:
    return st.session_state.chat_history

# Create runnable with message history
conversation = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Create user interface
st.title("🇮🇳 Hinglish Chatbot")
st.subheader("Aapka apna desi AI assistant!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Apna message yahan type karein..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            # Invoke the conversation chain
            response = conversation.invoke(
                {"input": prompt},
                config={"configurable": {"session_id": "hinglish_session"}}
            )
            
            # Extract content from AIMessage
            response_content = response.content if hasattr(response, 'content') else str(response)
            
            st.write(response_content)
            
            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_content})
