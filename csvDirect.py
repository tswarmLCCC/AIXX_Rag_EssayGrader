from ollama import chat
from ollama import ChatResponse
from utilities.promptUtils import promptStringFromFiles, promptStringFromStrings, getStringFromFile
import logging
import csv

logging.basicConfig(level=logging.INFO)

quizPrompt = 'prompts/quizPrompt.txt'
basePrompt = getStringFromFile(quizPrompt)
# Update the prompt to ask for CSV formatted output without additional text
testPrompt = promptStringFromStrings(basePrompt, "python if statement", "Please format the output as CSV data only, without any additional text.")

logging.info("BASE_PROMPT: %s" % testPrompt)

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': testPrompt,
  },
])

csv_content = response['message']['content']

# Clean up the response to ensure it only contains CSV data
csv_lines = csv_content.splitlines()
csv_data = [line for line in csv_lines if line.startswith('"')]

# Save the cleaned CSV content to a file
with open('output.csv', 'w', newline='') as csvfile:
    csvfile.write("\n".join(csv_data))

print("CSV content saved to output.csv")