# GitRecovery
Yesterday I accidentally ran `git . rm -r -f` with no prior commit. Which is the reason why I wrote the script to help
recover lost data from my stupid act.

Right now it is basically unusable. You have to bring the script into the git repo in order for it to work...
It searches in all files deleted by git through searching and displaying files that contains given keyword.
Much improvements are expected to happen within few weeks...

# TODO
- Write Makefile for make install, which install into the system path as a command line tool.
- Make the script have command line tool, rather than having to manually bringing the script into the git repo...
