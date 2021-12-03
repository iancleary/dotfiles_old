# dotfiles

I manage my dotfiles wtih managed with the [yadm](https://yadm.io/docs/getting_started) dotfile manager.

My dotfiles are used and tested on MacOS, Ubuntu 20.04, ElementaryOS 6.  
I primarily use MacOS at home, Ubuntu at work or for anything with servers, and am a fan of Elementary.

If you use a Mac, I recommend you checkout [geerlingguy/mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook)!
If you use Ubuntu or Elementary OS, I recommend you checkout [icancclearynow/ubuntu-dev-playbook](https://github.com/icancclearynow/ubuntu-dev-playbook)!

Cheers!

## yadm

> Check out their [Getting Started Documentation](https://yadm.io/docs/getting_started)

### Install

```zsh
# MacOS
brew install yadm
```

```bash
# Ubuntu and Elementary
sudo apt install yadm
# Alternatively you can download the latest binary directly (say to avoid older ubuntu archive versions)
```

### Clone and Bootstrap

```bash
yadm clone -b main https://github.com/icancclearynow/dotfiles --bootstrap
```

This clones my dotfiles repo via HTTPS using yadm's [bootstrap](https://yadm.io/docs/bootstrap) standard command.

My Bootstrap script is [icancclearynow/dotfiles/blob/main/.config/yadm/bootstrap](https://github.com/icancclearynow/dotfiles/blob/main/.config/yadm/bootstrap). It's purpose is to:

* loads my dotfiles (including SSH keys)
* decrypt the private key (prompts for password),
* add the key to ssh-agent,
* tests the connection,
* and exit.

## Host Specific things

A few things are done selectively for MacOS and Ubuntu-based distributions.

* ssh-add has an extra `--use-apple-keychain` parameter to persist key addition to the next terminal session
* VS Code's settings.json file is in a different folder on Ubuntu and MacOS.  

> I use [Scripts/code_spell_check_sync.py](Scripts/code_spell_check_sync.py) to sync spell check words. 
> I manually edit the other settings.  I avoid VS Code built in sync as I prefer to have a git history of extensions, and other settings for later reference.
