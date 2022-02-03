import os
from urllib import response
from flask import Flask, flash, request, redirect, render_template,url_for
import json
from preprocessing import docx_processing  as doc, textract_processing as txt
from text_processing import tf_idf_cosine_similarity as tf_idf,doc2vec_comparison as d2v
from text_processing import cv_cosine_similarity as cv
import os


def process_files(req_document,resume_docs):
    
    req_doc_text = txt.get_content_as_string(req_document)
    # print('The start' * 5)
    resume_doc_text = []
    for doct in resume_docs:
        resume_doc_text.append(txt.get_content_as_string(doct))

    print(resume_doc_text)
    cos_sim_list = tf_idf.get_tf_idf_cosine_similarity(req_doc_text,resume_doc_text)
    final_doc_rating_list = []
    zipped_docs = zip(cos_sim_list,resume_docs)
    sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0], reverse=True)
    for element in sorted_doc_list:
        doc_rating_list = []
        doc_rating_list.append(os.path.basename(element[1]))
        doc_rating_list.append("{:.0%}".format(element[0]))
        final_doc_rating_list.append(doc_rating_list)
    return final_doc_rating_list
 

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','docx'])
UPLOAD_FOLDER = '/Users/riya'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('resume_loader.html')

@app.route('/failure')
def failure():
   return 'No files were selected'

@app.route('/success/<name>')
def success(name):
   return 'Files %s has been selected' %name

@app.route('/', methods=['POST', 'GET'])
def check_for_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'reqFile' not in request.files:
           flash('Requirements document can not be empty')
           return redirect(request.url)
        if 'resume_files' not in request.files:
           flash('Select at least one resume File to proceed further')
           return redirect(request.url)
        file = request.files['reqFile']
        if file.filename == '':
           flash('Requirement document has not been selected')
           return redirect(request.url)
        resume_files = request.files.getlist("resume_files")
        if len(resume_files) == 0:
            flash('Select atleast one resume file to proceed further')
            return redirect(request.url)
        if ((file and allowed_file(file.filename)) and (len(resume_files) > 0)):
           #filename = secure_filename(file.filename)
           abs_paths = []
           filename = file.filename
           req_document = UPLOAD_FOLDER+'/'+filename
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           for resumefile in resume_files:
               filename = resumefile.filename
               abs_paths.append(UPLOAD_FOLDER + '/' + filename)
               resumefile.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
           result = process_files(req_document,abs_paths)
           print(result)
           response = json.dumps(result)
           return response
        #    for file_path in abs_paths:
        #        file_utils.delete_file(file_path)
                  
        else:
           flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
           return redirect(request.url)

if __name__ == "__main__":
    app.run(debug = True)