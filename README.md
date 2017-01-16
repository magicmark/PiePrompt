# PiePrompt
PiePrompt is a custom PS1 written in Python. It is modular and responsive.

To use: install in a venv, and use this custom zsh theme:

```
function precmd() {
    path/to/venv/bin/pieprompt top "$(tput cols)"
}

PROMPT='%5{$(path/to/venv/bin/pieprompt bottom "$(tput cols)")%}'
RPROMPT='%{$fg[green]%}[%*]%{$reset_color%}'
```
