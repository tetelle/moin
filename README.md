This project integrates wiki pages and converts these pages using the markdown language.
It uses Moinmoin and Pandoc.

Moin_convert giving a page and a location, it looks up for the most recent page of a wiki page
Results are saved into wiki/data/output

Convert_markdown converts all wiki files in wiki/data/output into markdown files

# Install

virtualenv .
. ./bin/activate
pip install -r requirements.txt


