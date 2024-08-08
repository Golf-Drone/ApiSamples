# ApiSamples
A playground for playing with APIs, particularly OpenAI.

## Current caveats
* There is no build - the code assumes you have installed the openai, dotenv and duckduckgo_search libraries.
* A .env file must be created in the project root containing the openai api key as follows
    OPEN_AI_KEY=_[your key goes here]_

## Environment Setup
Tool versions managed by [ASDF](www.asdf-vm.com)
### MacOS (Apple Silicon)
1. Install homebrew
2. `brew install coreutils curl git`
3. `brew install asdf`
4. Add `. /opt/homebrew/opt/asdf/libexec/asdf.sh` to your home folder .zprofile file
5. Restart your terminal
6. `asdf plugin add python`
7. `pip install openai`
8. `pip install python-dotenv` (consider using a python virtual env to manage libraries)
9. `pip install duckduckgo_search`
