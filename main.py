import openai
import os
import sqlite3

openai.api_key = os.environ["OPENAI_API_KEY"]

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
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

output = response.choices[0].text
print(output)

output_file_path = "output.txt"
write_file(output_file_path, output)

conn = sqlite3.connect('memory.db')
cursor = conn.cursor()

# Create a table to store the memory
cursor.execute('''
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY,
        input_file_path TEXT,
        output_file_path TEXT,
        prompt TEXT,
        engine TEXT,
        response TEXT
    );
''')

# Insert the relevant information into the memory table
cursor.execute('''
    INSERT INTO memory (input_file_path, output_file_path, prompt, engine, response)
    VALUES (?, ?, ?, ?, ?);
''', (file_path, output_file_path, prompt, 'text-davinci-002', output))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
