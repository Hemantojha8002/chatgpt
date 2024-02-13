API_Key='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'
import openai
import os
os.environ['OPENAI_Key']=API_Key
openai.api_key=os.environ['OPENAI_Key']

keep_prompting=True
while keep_prompting:
    prompt=input('Hey , whats your question? Type exit if done!!')
    if prompt=='exit':
        keep_prompting=False
    else:
        response=openai.Completion.create(engine='text-davinci-003',prompt=prompt,max_tokens=200)
        print(response)
 


