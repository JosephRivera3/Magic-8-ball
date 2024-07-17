from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/input', methods=['GET','POST'])
def question():
    answer = [
        'Yes', 'No', 'Maybe'
    ]
    if request.method == 'POST':
        query = request.form['query']
        if query not in answer:
                return "You're answer is" + answer
        return render_template('gifs.html', answer=answer[query])

    return render_template('input.html',url=url_for('input'))

if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)
