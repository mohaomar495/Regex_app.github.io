from flask import Flask, request, render_template
import re

app = Flask(__name__)

def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

@app.route('/', methods=['GET', 'POST'])
def index():
    email_valid = None
    result = None
    if request.method == 'POST':
        regex = request.form.get('regex')
        test_string = request.form.get('test_string')
        
        if regex and test_string:
            try:
                pattern = re.compile(regex)
                match = pattern.search(test_string)
                if match:
                    result = f"Match found: {match.group()}"
                else:
                    result = "No match found"
            except re.error:
                result = "Invalid regular expression"

        email = request.form.get('email')
        if email:
            email_valid = "Valid email" if is_valid_email(email) else "Invalid email"
        
        return render_template('result.html', result=result, email_valid=email_valid)
    
    return render_template('index.html', email_valid=email_valid)

if __name__ == '__main__':
    app.run(debug=True)
