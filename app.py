from flask import Flask, request, jsonify, render_template
from openai import OpenAI, OpenAIError

app = Flask(__name__)

client = OpenAI(
    api_key="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"
)

@app.route('/')
def home():
    return render_template('ai.html')

@app.route('/get_ai_response', methods=['POST'])
def get_ai_response():
    data = request.json
    prompt = data.get('prompt')
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        response = completion.choices[0].message['content']
        return jsonify({'response': response})
    except OpenAIError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
