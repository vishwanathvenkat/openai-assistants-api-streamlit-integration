from openai import OpenAI
from dotenv import load_dotenv
import os
import time


class OpenAIAssistant:
    def __init__(self, api_key, assistant_id):
        self.client = OpenAI(api_key=api_key)
        self.assistant_id = assistant_id
    
    def initialize_thread(self):
        thread = self.client.beta.threads.create()
        return thread

    def submit_message(self, thread, user_input):
        self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant_id,
        )
        return run

    def get_response(self, thread):
        messages = self.client.beta.threads.messages.list(thread_id=thread.id, order="desc")
        return messages

    def wait_for_run_completion(self, run, thread):
        while run.status in {"queued", "in_progress"}:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run


def initialize_assistant():
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    assistant_id = os.environ.get("ASSISTANT_ID")

    if not api_key or not assistant_id:
        raise EnvironmentError("API keys are not set in the environment.")

    assistant = OpenAIAssistant(api_key, assistant_id)

    return assistant


def main():
    
    assistant = initialize_assistant()
    # Example usage:
    thread = assistant.initialize_thread()
    user_input = "Hello, assistant!"
    run = assistant.submit_message(thread, user_input)
    run = assistant.wait_for_run_completion(run, thread)
    response = assistant.get_response(thread)
    print(response)


if __name__ == "__main__":
    main()