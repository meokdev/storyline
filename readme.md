# STORYLINE V1
Storyline is an AI powered novel generator. It transforms brief user input into an entire novel.

### Functions
- Interprets user prompt
- Generates story plan
- Generates chapters
- Chapters are assembled 
- Generator returns a PDF

Storyline is able to maintain contextual clarity and relevance across the whole novel. Characters, plot, settings stay constant throughout the whole novel. 

The style and formatting of the generated PDF can be customised. 

### Cost
Storyline is powered by the Anthropic API. By default, the model used is claude haiku ```claude-3-haiku-20240307```. Each novel with this model costs around 0.05USD in credits. Using a better model, such as ```claude-3-sonnet-20240229``` or even ```claude-3-opus-20240229``` may return slightly better results with higher quality writing, but cost much more. 

Regardless of the model used, the writing is able to maintain high contextual relevance. 

## Setup
Python version ```3.11``` or above is required to run this program. Older versions may work, but are untested, and may be incompatible with anthropic.

*It is recommended to set up a virtual environment using ```venv```"

Install all of the requirements using ```pip install -r requirements.txt```

Set the ANTHROPIC_API_KEY environment variable using ```export ANTHROPIC_API_KEY='your-api-key-here'``` on MacOS/Linux or ```setx ANTHROPIC_API_KEY "your-api-key-here"``` on Windows. 

**Run the program** using ```python main.py```
You will then be required to enter a prompt for the novel you want. The prompt can be anything from a 1 sentence idea, to a multi paragraph outline.

Usually, the generator takes around 5 minutes to generate the entire novel, and the length of the text may vary based on the prompt. 

Once writing finishes, a ```pdf``` with the complete novel will be created in the ```output``` folder.

## To-Dos

-[ ] Better PDF formatting
-[ ] Table of contents
-[ ] AI Generated Title page (DallE)
-[ ] UI