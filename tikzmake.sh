#!/bin/bash

python network_diagram.py
pdflatex network_diagram.tex

rm *.aux *.log *.vscodeLog
rm *.tex
