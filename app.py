from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
    'id': 0,
    'contact': '0123456789',
    'name': 'Sid',
    'is_done': False,
}, {
    'id': 1,
    'contact': '9876543210',
    'name': 'John',
    'is_done': False,
}]

@app.route('/')
def get_data():
    return jsonify({
        'data': contacts
    })

@app.route('/addData', methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            'status': 'Error',
            'message': 'No Request Found To Post Data'
        }, 400)
  
    contact = {
        'id': contacts[-1]['id'] + 1,
        'contact': request.json['contact'],
        'name': request.json['name'],
        'is_done':  request.json['is_done']
    }
    contacts.append(contact)
    return jsonify({
            'status': 'Success',
            'message': 'Task Successfully Posted'
    })

if __name__ == '__main__':
    app.run(debug=True)