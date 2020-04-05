import os
# import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
from face_matching import FaceMatching

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/match', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'selfie' not in request.files:
            flash('No file part')
            return jsonify(status=205, reason="Selfie image missing")
        file_s = request.files['selfie']
        if file_s.filename == '':
            flash('No file selected for uploading')
            return jsonify(status=205, reason="No file selected for uploading")
        if file_s and allowed_file(file_s.filename):
            if not os.path.isdir(app.config['UPLOAD_FOLDER']):
                os.mkdir(app.config['UPLOAD_FOLDER'])
                print("Upload folder created")
            if not os.path.isdir(app.config['S_UPLOAD_FOLDER']):
                os.mkdir(app.config['S_UPLOAD_FOLDER'])
            selfie_filename = secure_filename(file_s.filename)
            file_s.save(os.path.join(app.config['S_UPLOAD_FOLDER'], selfie_filename))
            if 'id' not in request.files:
                flash('No file part')
                return jsonify(status=205, reason="Id image missing")
            file_id = request.files['id']
            if file_id.filename == '':
                flash('No file selected for uploading')
                return jsonify(status=205, reason="No file selected for uploading")
            if file_id and allowed_file(file_id.filename):
                if not os.path.isdir(app.config['I_UPLOAD_FOLDER']):
                    os.mkdir(app.config['I_UPLOAD_FOLDER'])
                id_filename = secure_filename(file_id.filename)
                file_id.save(os.path.join(app.config['I_UPLOAD_FOLDER'], id_filename))
                match = FaceMatching(selfie_filename, id_filename)
                similarity = match.match_selfie_id()
                return jsonify(status=0, reason="Selfie and ID Image uploaded successfully!", selfie_filename=selfie_filename, id_filename=id_filename, score=similarity)
        else:
            flash('Allowed file types are png, jpg, jpeg')
            return jsonify(status=200, reason="Allowed file types are png, jpg, jpeg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)