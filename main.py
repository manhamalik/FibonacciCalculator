from flask import Flask, render_template, request

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form.get('number')
        if not number:
            return render_template('index.html', error_message='You must enter a number before continuing')
        try:
            number = int(number)
            if number > 150:
                return render_template('index.html', error_message='The maximum number allowed is 150')
            
            fibonacci_sequence = fibonacci(number + 1)

            # Determine the number suffix
            if number % 10 == 1 and number % 100 != 11:
                number_suffix = "st"
            elif number % 10 == 2 and number % 100 != 12:
                number_suffix = "nd"
            elif number % 10 == 3 and number % 100 != 13:
                number_suffix = "rd"
            else:
                number_suffix = "th"

            return render_template('index.html', number=number, number_suffix=number_suffix, sequence=fibonacci_sequence)
        except ValueError:
            return render_template('index.html', error_message='Invalid number. Please enter a valid integer.')
    else:
        return render_template('index.html')

app.run(host='0.0.0.0', port=81, debug=True)
