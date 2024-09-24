def insert_strings(base_string, file1_path , file2_path  ):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        string1 = file1.read().strip()
        string2 = file2.read().strip()
    
    result = base_string.format(string1, string2)
    return result

# Example usage:
base_string = '''

Prompt:

Evaluate the following student essay against the provided rubric.

Inputs:

Student Essay: {}
Rubric: {}

Task:

Grade: Determine a suggested grade for the essay based on the rubric.
Key Points: Identify the key points or arguments presented in the essay.
Strengths: Highlight the strengths of the essay, such as clear organization, strong evidence, or effective writing style.
Weaknesses: Identify areas where the essay could be improved, such as lack of clarity, insufficient evidence, or grammatical errors.
Specific Feedback: Provide specific feedback on the essay, addressing both the strengths and weaknesses identified.

Example Feedback:

Overall Grade: B+ Key Points: The essay effectively argues for [main argument]. The author provides strong evidence from [source 1] and [source 2] to support their claims. Strengths: The essay is well-organized and easy to follow. The writing is clear and concise.
Weaknesses: The essay could be strengthened by providing more in-depth analysis of the evidence. Additionally, there are a few grammatical errors that should be corrected. Specific Feedback: The introduction could be more engaging. Consider adding a strong hook to capture the reader's attention. The conclusion could be expanded to provide a more satisfying ending.


Note: To ensure accurate and helpful feedback, it is important to provide a comprehensive rubric that clearly outlines the expectations for the essay. The LLM can then use the rubric as a guide to evaluate the student's work.
 
'''

result = insert_strings(base_string, 'prompts/essay.txt', "prompts/rubric.txt")
print(result)