#!/usr/bin/env python
#####################################
# Installation module for PowerSploit
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nathan Underwood (sainate)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Powershell Empire"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/adaptivethreat/Empire.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="PowershellEmpire"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./setup/install.sh,./setup/setup_database.py"
