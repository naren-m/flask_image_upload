from flask import Flask, render_template, Response, jsonify, request
from flask.ext.api import status
from werkzeug import secure_filename
import os
from flask_restful import reqparse, abort, Api, Resource


from flask import jsonify
app = Flask(__name__)
# parser.add_argument('task', type=str)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = 'uploads/'

resp = {'response': None, "imagePath": None}

@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    content = {'filename': None}
    if request.method == 'POST' and 'image' in request.files:
        # Get the name of the uploaded file
        f = request.files['image']
        print("file obj", f)
        # Check if the file is one of the allowed types/extensions
        if f and allowed_file(f.filename):
            print("in if", "filename")
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(f.filename)
            print("in if", filename)
            # Move the file form the temporal folder to
            # the upload folder we setup
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print("path", path)
            f.save(path)
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            resp['response'] = status.HTTP_200_OK
            resp['imagePath'] = filename
            return jsonify(resp) 
    else:
        resp['response'] = status.HTTP_405_METHOD_NOT_ALLOWED
        resp['imagePath'] = None
        return resp 

if __name__ == '__main__':
    app.run(debug=True)




