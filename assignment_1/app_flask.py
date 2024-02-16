"""Simple Web interface to spaCy entity recognition

To see the pages point your browser at http://127.0.0.1:5000.

"""


from flask import Flask, request, render_template

import ner

app = Flask(__name__)


# For the website we use the regular Flask functionality and serve up HTML pages.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        text = request.form['text']
        doc = ner.SpacyDocument(text)
        markup = doc.get_markup_html()
        # markup_paragraphed = ''
        # for line in markup.split('\n'):
        #     if line.strip() == '':
        #         markup_paragraphed += '<p/>\n'
        #     else:
        #         markup_paragraphed += line
        return render_template('result.html', markup=markup)



if __name__ == '__main__':

    app.run(debug=True)