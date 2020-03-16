# This is a script to compile a latex document and clean up afterwards
# Originally written by Nick Wheeler
import os

################################################################################
# Clean out the repo, and recompile the tex
################################################################################

# Options

# What is the file name?
texfile = "cwru-cse-thesis"

# Also run bibtex to compile references?
bibtex=True

# Call up the resulting pdf with mupdf when finished?
view=True

################################################################################
# Code
################################################################################

os.system("python 1501wheeler-pytexrepoclean.py")
os.system("pdflatex " + texfile + ".tex")
os.system("pdflatex " + texfile + ".tex")
if bibtex:
  os.system("bibtex " + texfile + ".aux")
  os.system("pdflatex " + texfile + ".tex")
  os.system("pdflatex " + texfile + ".tex")
os.system("python 1501wheeler-pytexrepoclean.py")
if view:
  os.system("mupdf " + texfile + ".pdf")
