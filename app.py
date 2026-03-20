from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yoga', methods=['POST'])
def yoga():
    problem = request.form['problem'].lower()
    
    with open('data/yoga.json') as f:
        data = json.load(f)

    result = data.get(problem, [])

    return render_template('yoga_result.html', result=result, problem=problem)

@app.route('/medicine', methods=['POST'])
def medicine():
    import json
    import easyocr

    text = ""

    # 🥇 OPTION 1: TEXT INPUT
    medicine_name = request.form.get("medicine_name")

    if medicine_name:
        text = medicine_name.lower()

    # 📂 Load JSON
    with open('data/medicine.json') as f:
        data = json.load(f)

    # 🔍 MATCH
    for key in data:
        if key in text:
            info = data[key]

            return render_template(
                'medicine_result.html',
                name=info['name'],
                use=info['use'],
                precaution=info['precaution']
            )

    return render_template(
        'medicine_result.html',
        name="Not Found",
        use="Could not detect medicine",
        precaution="Try different input"
    )
if __name__ == '__main__':
    app.run(debug=True)
