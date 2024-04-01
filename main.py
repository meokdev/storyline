import anthropic
import os
from globalvar import detail, outline, chapterdesc, fulltext
from fpdf import FPDF

client = anthropic.Anthropic()

system_filepath = os.path.join("prompts", "system.txt")
with open(system_filepath, 'r', encoding='utf-8') as file:
        system_context = file.read()

system_filepath = os.path.join("prompts", "detailiser.txt")
with open(system_filepath, 'r', encoding='utf-8') as file:
        detail_prompt = file.read()

content=input("What do you want the novel to be about?: ")

#add detail to user prompt
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=4096,
    temperature=1,
    system=system_context,
    messages=[
        {"role": "user", "content": detail_prompt+content}
    ]
)
detail=message.content[0].text

system_filepath = os.path.join("prompts", "outline.txt")
with open(system_filepath, 'r', encoding='utf-8') as file:
        outline_prompt = file.read()
#outline
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=4096,
    temperature=1,
    system=system_context,
    messages=[
        {"role": "user", "content": outline_prompt+"Description:"+detail}
    ]
)
outline=message.content[0].text
print(outline)


system_filepath = os.path.join("prompts", "chaptercount.txt")
with open(system_filepath, 'r', encoding='utf-8') as file:
        chaptercount_prompt = file.read()
#chaptercount
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=4096,
    temperature=1,
    system=system_context,
    messages=[
        {"role": "user", "content": chaptercount_prompt+outline}
    ]
)
count=int(message.content[0].text)
print(count)

#Generating chapter descriptions
for i in range(count):
    system_filepath = os.path.join("prompts", "chapter_outline.txt")
    with open(system_filepath, 'r', encoding='utf-8') as file:
            chapter_outline_prompt = file.read()
    #chaptercount
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4096,
        temperature=1,
        system=system_context,
        messages=[
            {"role": "user", "content": "For chapter number "+str(i+1)+"from the outline"+outline+chapter_outline_prompt}
        ]
    )
    chapter_outline=message.content[0].text
    chapterdesc.append(chapter_outline)


print(chapterdesc)

for i in range(count):
    system_filepath = os.path.join("prompts", "chapter.txt")
    with open(system_filepath, 'r', encoding='utf-8') as file:
            chapter_prompt = file.read()
    #chaptercount
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4096,
        temperature=1,
        system=system_context,
        messages=[
            {"role": "user", "content": chapter_prompt+str(chapterdesc[i])}
        ]
    )
    chapter_text=message.content[0].text
    fulltext.append(chapter_text)


def sanitize_text(input_text):
    """
    Sanitizes input text for FPDF compatibility by removing or replacing unsupported Unicode characters.
    """
    # Replace specific unsupported characters with similar ones or remove them
    # This is a basic example; you might need to expand it based on your text content
    replacements = {
        '“': '"',  # Replace curly double quotes
        '”': '"',
        '‘': "'",  # Replace curly single quotes
        '’': "'",
        '—': '-',  # Replace em dashes
        '…': '...',  # Replace ellipses
    }
    for original, replacement in replacements.items():
        input_text = input_text.replace(original, replacement)
    
    # Remove any remaining characters outside the Latin-1 range
    sanitized_text = ''.join(char if ord(char) < 256 else '' for char in input_text)
    return sanitized_text
# Sanitize and update each item in the 'fulltext' list
fulltext = [sanitize_text(chapter) for chapter in fulltext]



class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'My Novel Title', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')



pdf = PDF()

# Add a page
pdf.add_page()

# Set the font
pdf.set_font("Arial", size=12)

# Add the full text to the PDF
for line in fulltext:
    pdf.multi_cell(0, 10, line)

# Save the PDF to a file
pdf_file_path = "output/my_novel.pdf"
pdf.output(pdf_file_path)

print(f"PDF created successfully: {pdf_file_path}")