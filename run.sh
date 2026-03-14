#!/bin/bash

MAIN_FILE="main.py"
VENV_DIR=".venv"
REQUIREMENTS="aiogram python-dotenv"
SUBCOMMAND=${1}

case "$SUBCOMMAND" in
  "init-venv")
    python3 -m venv $VENV_DIR
    source "$VENV_DIR/bin/activate"
    python3 -m pip install $REQUIREMENTS
    ;;
  "init")
    python3 -m pip install $REQUIREMENTS
    ;;
  "")
    ;;
  *)
    echo "Неверный первый аргумент: должен быть init, init-venv или отсутствовать (> <)\"."
    return 1
esac

if [[ -d "$VENV_DIR" ]]; then
  source "$VENV_DIR/bin/activate"
fi
python3 $MAIN_FILE