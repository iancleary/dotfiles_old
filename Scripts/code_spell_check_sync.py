#!python3

import json
from pathlib import Path
from typing import List

home = Path.home()

MACOS_CODE_SETTINGS_FILE = home / 'Library/Application Support/Code/User/settings.json'
LINUX_CODE_SETTINGS_FILE = home / '.config/Code/User/settings.json'

CSPELL_KEY = 'cSpell.userWords'

def get_cspell_words(settings_file:Path) -> List[str]:
    with open(settings_file) as file:
        settings = json.load(file)
        if CSPELL_KEY in settings.keys():
            words = settings[CSPELL_KEY]
            return words
        else:
            return []

def merge_lists(cspell_word_list_one:List[str], cspell_word_list_two:List[str]) -> List[str]:
    list_one_set = set(cspell_word_list_one)
    list_two_set = set(cspell_word_list_two)
    union = list_one_set.union(list_two_set)
    return sorted(list(union))

def update_cspell_words(settings_file:Path, cspell_words:List[str]) -> None:
    with open(settings_file, "r") as file:
        settings = json.load(file)
        settings[CSPELL_KEY] = cspell_words
        
    with open(settings_file, "w") as file:
        json_object = json.dumps(settings, indent = 4)
        file.write(json_object)

macos_code_settings_cspell_words = get_cspell_words(MACOS_CODE_SETTINGS_FILE)
linux_code_settings_cspell_words = get_cspell_words(LINUX_CODE_SETTINGS_FILE)

combined_cspell_words = merge_lists(macos_code_settings_cspell_words, linux_code_settings_cspell_words)

update_cspell_words(settings_file=MACOS_CODE_SETTINGS_FILE, cspell_words=combined_cspell_words)
update_cspell_words(settings_file=LINUX_CODE_SETTINGS_FILE, cspell_words=combined_cspell_words)
