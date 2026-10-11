from flask import Flask, abort, redirect, render_template, request, url_for

from i18n import DEFAULT_LANG, LANGS, UI, get_methods

app = Flask(__name__)


@app.route('/')
def index():
    # Wybór języka na podstawie nagłówka Accept-Language przeglądarki
    lang = request.accept_languages.best_match(list(LANGS)) or DEFAULT_LANG
    return redirect(url_for('guide', lang=lang))


@app.route('/<lang>/')
def guide(lang):
    if lang not in LANGS:
        abort(404)
    return render_template('index.html', lang=lang, langs=LANGS, t=UI[lang], methods=get_methods(lang))


if __name__ == '__main__':
    app.run(debug=True)
