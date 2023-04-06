import openai
import os

openai.api_key = os.environ["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"]

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

file_path = "example.txt"
file_content = read_file(file_path)

prompt = "The following is a text completion task:\n\n" + file_content

response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

output = response.choices[0].text
print(output)

output_file_path = "output.txt"
write_file(output_file_path, f"Input file path: {file_path}\nOutput file path: {output_file_path}\nPrompt: {prompt}\nEngine: gpt-3.5-turbo\nResponse: {output}")