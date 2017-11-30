from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators, StringField, SubmitField
import collections
from string import punctuation

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    text_block = TextAreaField('Text Block:', validators=[validators.required(), validators.DataRequired()])

@app.route("/", methods=['GET', 'POST'])
def word_count():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        text_block = form.text_block.data

        if form.validate():
            # generate word counts
            all_words = generate_word_count(text_block)
            all_unique_words = generate_unique_word_count(text_block)

            # return string with the word counts
            flash('Word Count: ' + all_words + ' | ' + 'Unique Words: ' + all_unique_words)
        else:
            # send error on invalid input
            flash('Error! Text input is required.')

    return render_template('index.html', form=form)

def generate_word_count(text_block):
    '''
    :type text_block: String
    :rtype: String

    Splits text block by whitesace and returns the count of tokens.

    Returns the sum of the Counter values to get the number of words.
    '''
    word_counter = collections.Counter(text_block.split())
    return str(sum(word_counter.values()))

def generate_unique_word_count(text_block):
    '''
    :type text_block: String
    :rtype: String

    Removes all punctuation in string, lowers individual string, inserts uniquely into Counter.

    Returns the length of the Counter to get the number of unique words.
    '''
    punctuation_replaced = text_block.translate(str.maketrans({a:None for a in punctuation})).lower()
    word_counter = collections.Counter(punctuation_replaced.split())
    return str(len((word_counter.keys())))

if __name__ == "__main__":
    app.run()
