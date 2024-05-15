import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
import time

project = "woven-bonbon-422619-f6"
vertexai.init(project = project)

config = generative_models.GenerationConfig(
    temperature = 0.4
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)

chat = model.start_chat()

# helper function to display and send messages in streamlit
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text
    # st.write("🤖 ReX:", output)
    
    with st.chat_message("model"):
        st.markdown(output)
        
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )     

st.title("Gemini Explorer")

# Init chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    user_name = ""
    user_age = ""
    user_race = ""
    user_pronouns = ""

# Capture User Information
user_name = st.text_input("Please enter your name")
# time.sleep(2.0)
user_age = st.text_input("Please enter your age")
# time.sleep(2.0)
user_race = st.text_input("Please enter your race")
# time.sleep(2.0)
user_pronouns = st.text_input("Please enter your pronouns")
time.sleep(5.0)

# Display and load to chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
            role = message["role"],
            parts = [ Part.from_text(message["content"]) ]
        )
    
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        
    chat.history.append(content)

# Implement Personalized Greetings
if len(st.session_state.messages) == 0:
    if user_name and user_age and user_race and user_pronouns:
        initial_prompt = f"Hey {user_name}! I'm ReX, an assistant powered by Google Gemini. Let's chat using emojis to be interactive 😊. I see that you are {user_age}, {user_race}, and identify as {user_pronouns}. How can I help you today?"
    else:
        initial_prompt = "Hey there! I'm ReX, an assistant powered by Google Gemini. Let's chat using emojis to be interactive 😊. How can I help you today?"
    llm_function(chat, initial_prompt)

query = st.chat_input("Gemini Flights")   

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)