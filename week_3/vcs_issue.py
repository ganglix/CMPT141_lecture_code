# error: cannot spawn C:\Users\gal894\AppData\Local\JetBrains\PyCharmCE2022.3\tmp\intellij-git-askpass-local.sh: Function not implemented
# error: cannot spawn bash: Function not implemented
# fatal: could not read Username for 'https://github.com': No such file or directory
#
#
# I have solved the problem , able to do Git Pull/Push successfully from Intellij:
#
# No need to re-install Git/Intellij. Just go to IntelliJ-> project Settings->Git-> uncheck "Path to Git Executable" ( This will automatically pop-up with C:/Users/<UserName>\AppData\....\Git.exe
#
# Restart Intellij and try to do Git-> pull .
#
# Note: Keeping credential-manager will help to avoid entering password again.

