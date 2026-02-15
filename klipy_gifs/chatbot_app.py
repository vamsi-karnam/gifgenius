import streamlit as st
from gifresponse import getgif, getresponse
# Function that processes user queries
# def respond(userquery):
#     """
#     This function processes the user's query and returns a response.
#     You can customize this function to integrate with your AI model or logic.
#     """
#     # Placeholder response - customize this with your actual bot logic
#     response = f"You said: '{userquery}'. This is where the bot's response will go!"
#     return response
sys_prompt='''you are a chatbot that replies to the user in the form of GIFS, you need to understand the tone, language, intent and other patterns based on the user query and conversation history provided to you to come up with smart reply to the converstaion that the user is trying to have with you in the form of GIF titles that will later be used for searching in a gif database called klipy and then this gif would be passed to the user.
    so the user talks to you and you need to proactively have a conversation with the user but in the form of gifs, so your task is to understand the user's query based on the conversation history and the contextual reference of the query provided to you and then come up with a reply and then convert your reply into a witty gif title.
    Keep your response crisp with just the GIF title, make sure you dont add any symbols or dash "-" in your title and keep it short with only keywords so that the most relavant gif would come up that will be used for querying klipy, do not send any other content in your response.
    make sure the response should be free of symbols.
    '''

# Set up the Streamlit page
st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")
st.title("🤖 Simple Chatbot")
st.caption("A chatbot interface powered by Streamlit")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messagesimg = []
    st.session_state.messages.append({"role": "system", "content": sys_prompt})

# Display chat messages from history
for message in st.session_state.messagesimg:
    with st.chat_message(message["role"]):
        if message["role"]=="user":
            st.markdown(message["content"])
        if message["role"]=="assistant":
            st.image(message["content"])
                

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messagesimg.append({"role": "user", "content": prompt})
    
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    res=getresponse(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": res})
    
    # Get bot response by calling the respond function
    bot_response = getgif(res)
    st.session_state.messagesimg.append({"role": "assistant", "content": bot_response})
    
    # Display bot response
    with st.chat_message("assistant"):
        # st.markdown(bot_response)
        st.image(bot_response)
    
    # Add bot response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": bot_response})
