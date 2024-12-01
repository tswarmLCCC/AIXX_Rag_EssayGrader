from ollama import chat
from ollama import ChatResponse
from utilities.promptUtils import promptStringFromFiles, promptStringFromStrings, getStringFromFile
import logging

logging.basicConfig(level=logging.INFO)


quizPrompt = 'prompts/quizPrompt.txt'
basePrompt = getStringFromFile(quizPrompt)
testPrompt = promptStringFromStrings(basePrompt, "python if statement", "")



logging.info("BASE_PROMPT: %s" % testPrompt)

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': testPrompt,
  },
])
print(response['message']['content'])
# or access fields directly from the response object
#print(response.message.content)