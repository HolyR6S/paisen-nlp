import spacy

while True:
    model = input("Which model to use? (sm / md / LG): ").strip().lower()
    if model == '':
        model = 'lg'
        break
    if model in {"sm", "md", "lg"}:
        break
    print("Invalid input. Please enter 'sm', 'md', or 'lg'.")
model_name = f"de_core_news_{model}"
print(f"Model: {model_name}")

while True:
    file_name = input("Name of file that contains the text (default: 'input.txt'): ")
    if file_name.endswith('.txt'):
        break
    if file_name == '':
        file_name = 'input.txt'
        break
    print("Invalid input. File must be of type *.txt.")

# Load the selected German model
try:
    nlp = spacy.load(model_name)
except OSError:
    print(f"Model '{model_name}' not found. Did you run: `python -m spacy download {model_name}`?")
    exit(1)

# Read text from file
try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{file_name}' not found. Make sure it's in the same folder as this script.")

# Process text using spaCy
doc = nlp(text)

# print("Token | POS | Entity")
# print("-" * 30)
# for token in doc:
#     print(f"{token.text:15} | {token.pos_:5} | {token.ent_type_ or '-'}")

print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text:20} ({ent.label_})")