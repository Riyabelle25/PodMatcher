from distutils.log import debug
import os
from site import abs_paths
from urllib import response
from flask import Flask, flash, request, send_from_directory, redirect, render_template,url_for, jsonify, make_response
from flask_cors import CORS, cross_origin
import json
from preprocessing import docx_processing  as doc, textract_processing as txt
from text_processing import tf_idf_cosine_similarity as tf_idf,doc2vec_comparison as d2v
from text_processing import cv_cosine_similarity as cv
import os
import logging

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # this connects to our Firestore database 
candidates = []

def fetch_resumes():
    docs = db.collection(u'Resumes').stream() # opens 'resumes' collection
    resumes = {}
    for doc in docs:
        # print(f'{doc.id} => {doc.to_dict()}')
        resumes[doc.id] = doc.to_dict()['resume']
        candidates.append(doc.id)
    print(resumes)
    return resumes
resumes = fetch_resumes()

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')


def process_files(req_document,resume_docs):
    
    print(req_document)
    req_doc_text = txt.get_content_as_string(req_document)
    # print('The start' * 5)
    # resume_doc_text = []
    # for doct in resume_docs:
    #     resume_doc_text.append(txt.get_content_as_string(doct))
    print(34,resume_docs)
    cos_sim_list = tf_idf.get_tf_idf_cosine_similarity(req_doc_text,resume_docs)
    final_doc_rating_list = []
    zipped_docs = zip(cos_sim_list,candidates)
    sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0], reverse=True)
    for element in sorted_doc_list:
        doc_rating_list = []
        doc_rating_list.append(os.path.basename(element[1]))
        doc_rating_list.append("{:.0%}".format(element[0]))
        final_doc_rating_list.append(doc_rating_list)
    return final_doc_rating_list
 

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','docx'])
UPLOAD_FOLDER = 'C:/Users/Priya/Documents/mlhfellowship/PodMatcher/uploads'

app = Flask(__name__, static_folder = 'react-client/build', static_url_path='')
cors = CORS(app)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/api')
@cross_origin()
def Welcome():
    return "Hello world!!!"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/failure')
def failure():
   return 'No files were selected'

@app.route('/success/<name>')
def success(name):
   return 'Files %s has been selected' %name

@app.route('/api/upload', methods=['POST', 'GET'])
def check_for_file():
    if request.method == 'GET':
        print("hey")
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if 'file' not in request.files:
           print('Requirements document can not be empty')
           return json.dumps({'message': 'Requirements document can not be empty'})
        # if 'resume_files' not in request.files:
        #    flash('Select at least one resume File to proceed further')
        #    return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
           print('Requirement document has not been selected')
           return json.dumps({'message': 'Requirement document has not been selected'})

           return redirect(request.url)

        # resume_files = request.files.getlist("resume_files")
        # if len(resume_files) == 0:
        #     flash('Select atleast one resume file to proceed further')
        #     return redirect(request.url)
        if ((file and allowed_file(file.filename))): # and (len(resume_files) > 0)
           #filename = secure_filename(file.filename)
           abs_paths = []
           filename = file.filename
           req_document = UPLOAD_FOLDER+'/'+filename
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #    for resumefile in resume_files:
        #        filename = resumefile.filename
        #        abs_paths.append(UPLOAD_FOLDER + '/' + filename)
        #        resumefile.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
  
           for key in resumes:
               abs_paths.append(resumes[key])

           result = process_files(req_document,abs_paths)
           print(result)
           response = json.dumps(result)
           os.remove(req_document)
        #    for file_path in abs_paths:
        #        os.remove(file_path)
                       
           return "response"
        #    return render_template("resume_results.html", result=result)
                  
        else:
           print('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
           return json.dumps({'message': 'notvalid'})

           return redirect(request.url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444, debug=True)

# flask_cors.CORS(app, expose_headers='Authorization')