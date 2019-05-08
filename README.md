# Crap v 0.0.1
A command-line tool (bash) to help users find a right command after mistake. Works under `python 2.7.x`
# Example of usage:
```bash
$ gut
bash: gut: command not found
$ crap
Did you mean:
git ?
``` 
# Installation
* clone repo into any dir you like and navigate to repo dir
* change permissions and user groups for `bin/crap.sh` to make it avaiable and executable (just example):
```bash
$ chmod a+x bin/crap.sh
```
* create `crap` alias for .sh file, for example open `.bashrc` or `.bash_profile` (or any shell you like) and type
```bash
alias crap='/path/to/crap/bin/crap.sh'
```
to make this tool permanently accessible
* reload your shell