#!/bin/bash

rm network_diagram_maia.tex
python network_diagram_maia.py
pdflatex network_diagram_maia.tex
# python pdf2jpg.py

rm *.aux *.log
