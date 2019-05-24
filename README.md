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

## Install with pipenv
Install pipenv: https://pipenv.readthedocs.io/en/latest/
```bash
git clone git@github.com:FundacionParaguaya/send-lifemap.git
cd send-lifemap
pipenv install
pipenv shell
```

## Other requirements
* Create a `secrets.py` file (follow the example in `secrets.py.example`).
  * The credentials can be found at https://www.twilio.com/console.

* wkhtmltopdf:
  * Ubuntu: `sudo apt install wkhtmltopdf`
  * Win/Mac: https://wkhtmltopdf.org/downloads.html

## PDF creation 
```python
import pdfkit

pdfkit.from_url("https://www.povertystoplight.org/en/faq", "faq.pdf")

pdfkit.from_file("algo.html", "algo.pdf")
```