# cjk

Python tool for learning new vocabulary in Chinese, Japanese, and Korean.

## Story

I made this CLI tool since I haven't used Python in a hot minute and I wanted a refresher. This tool uses GPT4All
to translate words to Chinese, Japanese, and Korean with example sentences. While the program is set to translate
English to these three languages, it is extensible to whatever languages are understood by the model, and can be
configured in `src/config.py`.

While the program seems to work okay most of the time for simple words, it definitely spews out incorrect translations
from time to time. This is probably because at the time of writing, I am not super familiar with the best LLMs to use
for this use-case that are available to run locally for free, nor am I a prompt engineer.

In the future, I might revisit this idea and make it a native desktop application written in Rust. For now, I got what
I needed and got a simple refresher on Python. :)

## Usage

Once you run the app locally (instructions below) you will be prompted to enter a word to translate to the languages
of interest. From there, a prompt will run for each against the selected model, and you will see the translation as
well as an example sentence directly in your terminal.

## Development

### Prerequisites

- PyEnv (`brew install pyenv`)
- PipEnv (`brew install pipenv`)

### Running the Program Locally

```bash
# install packages
pipenv install

# start pipenv shell
pipenv shell

# run main.py
python src/main.py
```
