# ApiSamples
A playground for playing with APIs, particularly OpenAI.

## Current caveats
* There is no build - the code assumes you have installed the openai and dotenv libraries.
* A .env file must be created in the project root containing the openai api key as follows
    OPEN_AI_KEY=_[your key goes here]_

## Environment Setup
Tool versions managed by [ASDF](www.asdf-vm.com)
### MacOS (Apple Silicon)
1. Install homebrew
2. brew install coreutils curl git
3. brew install asdf  (node 12 error?)
4. echo -e "\n. \"$(brew --prefix asdf)/libexec/asdf.sh\"" >> ~/.bash_profile
5. echo -e "\n. \"$(brew --prefix asdf)/etc/bash_completion.d/asdf.bash\"" >> ~/.bash_profile
6. Restart your terminal
7. pip install openai
8. pip install python-dotenv (consider using a python virtual env to manage libraries)

