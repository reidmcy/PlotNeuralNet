from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


images = convert_from_path('network_diagram_maia.pdf')
images[0].save("network_diagram_maia.jpg") 
