import openai

openai.api_key = "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"

chat_history = ""

chat_history = "I will call you NAO and respond following question casually \n "
chat_history = [{"role": "system", "content": 'User will call you NAO and respond following question casually'}]

while True:
    text = input("User say:")
    # chat_history = "if I ask you "what is your name?" please answer "my name is NAO", otherwise please responds the followings casually \n "
    # chat_history = "I will call you NAO and respond following question casually \n "
    chat_history.append({"role": "user", "content": text})
    
    # chat_history = {"role": "user", "content": chat_history}
    # print(chat_history)
    # .gpt_prompt += "\n"+text

    # GPT-3
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt= chat_history,
    #     temperature=0.9,
    #     max_tokens=1000, #4 character is 1 token
    #     top_p=1,
    #     frequency_penalty=0.3,
    #     presence_penalty=0.6,
    #     stop=["Human:","NAO:"]
    # )
    print(chat_history)
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=chat_history
    )
    # messages=[{"role": "user", "content": chat_history}]

    # print(type(messages[0]))
    # print(response["choices"][0]["text"][:])
    # chat_history+=response["choices"][0]["text"][:]+"\n"

    print(response["choices"][0]["message"]["content"])
    chat_history.append({"role": "assistant","content":response["choices"][0]["message"]["content"]})
