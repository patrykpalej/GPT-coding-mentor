from openai import OpenAI


def create_assistant(api_key, model, assistant_name="Coding mentor by Patryk Palej"):
    client = OpenAI(api_key=api_key)
    my_assistants = [assistant.name for assistant in client.beta.assistants.list().data]

    if assistant_name not in my_assistants:
        assistant = client.beta.assistants.create(
            name=assistant_name,
            instructions="Help to solve programming tasks, but never provide the solution"
                         " and never write any code for the user. Just guide the user in the "
                         "right direction. The default programming language is Python. You can"
                         " ask questions to get information about what exatcly should be done.",
            model=model
        )
    else:
        assistant_id = [assistant.id
                        for assistant in client.beta.assistants.list().data
                        if assistant.name == assistant_name][0]
        assistant = client.beta.assistants.retrieve(assistant_id)

    thread = client.beta.threads.create()
    return client, assistant, thread
