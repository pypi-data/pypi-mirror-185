# bluewave

This is a Python script to analyze the similarity of two PDFs.

## Usage

To run this, an example would be:

```python
from bluewave.compare_pdfs import compare_pdf_files

filenames = ["file1.pdf", "file2.pdf"]
result = compare_pdf_files(filenames,
                           methods=False,
                           pretty_print=False,
                           verbose=True,
                           regen_cache=True,
                           sidecar_only=False,
                           no_importance=False
                           )
```