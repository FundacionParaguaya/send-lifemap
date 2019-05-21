# send-lifemap
Build a prototype that sends families and mentors their lifemaps.

## Install
```bash
git clone git@github.com:FundacionParaguaya/send-lifemap.git
cd send-lifemap
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Other requirements

* wkhtmltopdf:
  * Ubuntu: `sudo apt install wkhtmltopdf`
  * Win/Mac: https://wkhtmltopdf.org/downloads.html

## PDF creation 

```python
import pdfkit

pdfkit.from_url("https://www.povertystoplight.org/en/faq", "faq.pdf")

pdfkit.from_file("algo.html", "algo.pdf")
```