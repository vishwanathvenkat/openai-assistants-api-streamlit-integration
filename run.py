"""
Main code for the front-end of the bot. Can be used universally for any Assistant assistant backend.
NOTE: FOr assistants, they can be initialized either in the UI or via code once. Since they maintain the context
internally, we don't have to do it every-time. Unlike chat completion end-point where we need to supply the context
every time.
If you don't have to create new assistant via your front-end .i.e if you are not a chatbot creation product,
then its better you create the assistant via UI
"""
import streamlit as st
from streamlit_chat import message

from assistant import initialize_assistant


# we are creating a front-end that connects to an assistant that takes in  a text file and answers questions in the file
def initialize_st_object():
    st.session_state['user_input_list'] = []
    st.session_state['Assistant_response_list'] = []
    st.session_state.user_input = ''
    return


def main(assistant):

    # Title details
    st.set_page_config(page_title="Assistant", page_icon=":smiley:")

    # Initialize the list of user and bot responses so that it can be displayed
    if "current_thread" not in st.session_state:
        initialize_st_object()
        thread = assistant.initialize_thread()
        st.session_state["current_thread"] = thread
    else:
        thread = st.session_state["current_thread"]

    # Define text box for user input and a button for reset conversation
    # if 'user_input' not in st.session_state:

    st.text_input("Type your question here. Assistant is ready:", key='widget', on_change=clear_text)
    user_input = st.session_state.user_input
    button_clicked = st.button("Reset conversation")

    if button_clicked:
        reset_conversation()
        # Reload the page so that all the historical conversations displayed is erased
        st.rerun()

    # Enter this loop only of the user has typed in something it the textbox
    if user_input:
        # Generate the response by talking to Assistant
        response = respond(thread, user_input)

        # Append to lists so that we can display them at each run
        st.session_state.Assistant_response_list.append(response)
        st.session_state.user_input_list.append(user_input)

        # Display the user and bot responses
        for i in range(len(st.session_state['user_input_list']) - 1, -1, -1):
            # This function displays user input
            # This function displays Assistant response
            message(st.session_state['Assistant_response_list'][i],
                    avatar_style="icons",
                    key=str(i) + 'data_by_user')
            message(st.session_state["user_input_list"][i],
                    key=str(i), avatar_style="miniavs", is_user=True)


def respond(thread, user_input):
    run = assistant.submit_message(thread, user_input)
    run = assistant.wait_for_run_completion(run, thread)
    response_messages = assistant.get_response(thread)
    response = pretty_print(response_messages)
    return response


def pretty_print(messages):
    for m in messages:
        if m.role == "assistant":
            return m.content[0].text.value


def reset_conversation():
    # Clear all the values that were assigned in the current run
    st.session_state.pop('current_thread')
    st.session_state.pop('user_input_list')
    st.session_state.pop('Assistant_response_list')
    return


def clear_text():
    st.session_state.user_input = st.session_state.widget
    st.session_state.widget = ''


if __name__ == '__main__':
    assistant = initialize_assistant()
    main(assistant)