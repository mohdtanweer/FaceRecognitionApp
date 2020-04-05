from flask import Flask

UPLOAD_FOLDER = '/face_match/file_upload'

app = Flask(__name__)
app.secret_key = "Revo-Ex"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['S_UPLOAD_FOLDER'] = UPLOAD_FOLDER + "/selfie"
app.config['I_UPLOAD_FOLDER'] = UPLOAD_FOLDER + "/id"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024