
import openai

openai.api_key = "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"

messages = []                                                               #defining the list to store the conversartion
greeting = "I'm your friendly assistant chef. How can I help you today?"    #initial message from Chatgpt which is not shown in the output as it is asking gpt to act as a cheff assistant         
messages.append({"role": "assistant", "content": greeting})

print("Your chef assistant is ready")
while True:                                                                 #defininfg a loop which continusly append message from user and gpt and printing the same for a seamless chat flow
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(                                #calling openai api to generate the response
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")                                              #printing the reply and iterate again and again to maintain the chat
