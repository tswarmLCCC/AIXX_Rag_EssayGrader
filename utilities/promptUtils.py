def promptStringFromFiles(base_string_file_path, file1_path , file2_path  ):
    with  open(base_string_file_path, 'r') as base_string_file, open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        base_string = base_string_file.read().strip()
        string1 = file1.read().strip()
        string2 = file2.read().strip()
    
    result = base_string.format(string1, string2)
    return result
# Example usage:
#result = promptStringFromFiles('prompts/prompt1.txt', 'prompts/essay.txt', "prompts/rubric.txt")