from flask import Flask, request, jsonify,send_file,render_template
from flask_cors import CORS
from pymongo import MongoClient
from gridfs import GridFS
from bson import ObjectId
from pdf2image import convert_from_bytes,convert_from_path
import os

app = Flask(__name__)
app.config.from_object(__name__)

# Connect to MongoDB
db_client = MongoClient(host='attackflow6-mongodb',
                        port=27017, 
                        username='root', 
                        password='pass',
                        authSource="admin")

# Print text to server console
def print_to_console(text):
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    """
    print(f"\033[96m{text}", flush=True)

# Display available databases on server startup
print_to_console("backend: " + str(db_client.list_database_names()))

# Access the "attackflowdb" database
database = db_client["attackflowdb"]

# added to retrieve files
collection = database['files']

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app, resources={r'/*': {'origins': '*'}})

###### new modification to fix doc_upload 
fs = GridFS(database)

# Route: Home
@app.route('/')
def home():
    return "Hi from Backend Server"

# Route: Ping-Pong for server status check
@app.route('/ping', methods=['GET'])
def ping_pong():
    print_to_console("Server is ONLINE")
    return jsonify('pong!')

# Route: User Sign In
@app.route('/signin', methods=['POST'])
def signin():
    # TODO: Implement user sign in logic
    return jsonify('User sign in logic to be implemented')

# Route: User Sign Up
@app.route('/signup', methods=['POST'])
def signup():
    # TODO: Implement user sign up logic
    return jsonify('User sign up logic to be implemented')

# Route: User Sign Out
@app.route('/signout', methods=['GET'])
def signout():
    # TODO: Implement user sign out logic
    return jsonify('User sign out logic to be implemented')

# Route: Upload Document
@app.route('/upload_document', methods=['POST'])
# def upload_document():
#     file = request.files['file']
#     if file:
#         database.admin.insert_one({'i': file.read()})
#         print("successful msg from python")
#         return jsonify({'message': 'Upload successful'})
#     return jsonify({'message': 'No file uploaded'})
def upload_document():
    file = request.files['file']
    print_to_console (file.content_type)
    if file:
        if file.content_type == "application/pdf":
            file_id = fs.put(file, filename=file.filename, content_type=file.content_type)
            response = {
                'status': 'success',
                'msg': f'Upload successful, stored under id: {file_id}'
            }
            return response, 200
        else:
            response = {
                'status': 'failed',
                'error': "Invalid File Type! Only PDF file is accepted."
            }
            return response, 422

    response = {
                'status': 'failed',
                'error': 'No file uploaded.'
            }
    return response, 422

# Route: List all stored documents
@app.route('/list_documents', methods=['GET'])
def list_document():
    text=""
    for line in list(database['fs.files'].find()):
        text += str(line)
        text += "<br>"
    return text
"""
Example output
[{'_id': ObjectId('650bc2d81ae68c03f1b85143'), 'filename': 'A Truly Graceful Wipe Out - The DFIR Report.pdf', 'contentType': 'application/pdf', 'md5': '2bb14531032c089c5aebdd23627430dc', 'chunkSize': 261120, 'length': 957342, 'uploadDate': datetime.datetime(2023, 9, 21, 4, 13, 13, 588000)},
 {'_id': ObjectId('650bc64ba634981e024a159c'), 'filename': 'snapshot_week08_AttackFlow6.pdf', 'contentType': 'application/pdf', 'md5': '6ece469559cb4db0263401976e5a0c3b', 'chunkSize': 261120, 'length': 503611, 'uploadDate': datetime.datetime(2023, 9, 21, 4, 27, 55, 663000)}]
'650bc2d81ae68c03f1b85143' can be passed as file_id to retrieve the file
 """


# Route: Get Document
@app.route('/get_document/<file_id>', methods=['GET'])
def get_document(file_id):
    image_html = ""
    dir_path = f'tmp/{file_id}'

    # Check if a directory with the given file_id exists
    if os.path.isdir(dir_path):
        # Iterate through files in the directory
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if file_path[-3:]=="jpg" and os.path.isfile(file_path):
                # Generate HTML for displaying images
                image_html += f'<li><img src="/{file_id}/{filename}"></li>'
    else:
        # Create a directory with the given file_id if it doesn't exist
        os.mkdir(f"tmp/{file_id}")
        obj_id = ObjectId(file_id)
        res_file = fs.get(obj_id).read()

        # Save the PDF file in the directory
        with open(f"tmp/{file_id}/{file_id}.pdf", "wb") as f:
            f.write(res_file)

        # Convert PDF to images and save them
        images = convert_from_path(f'tmp/{file_id}/{file_id}.pdf')
        for i, image in enumerate(images):
            image.save(f'tmp/{file_id}/page{file_id}-{i}.jpg', 'JPEG')
            # Generate HTML for displaying images
            image_html += f'<li><img src="/{file_id}/page{file_id}-{i}.jpg"></li>'

    # Render the HTML template with the image HTML content
    return render_template('view_image.html', data=image_html)

# Route: Edit Document
@app.route('/edit_document', methods=['POST'])
def edit_document():
    # TODO: Implement document editing logic
    return jsonify('Document editing logic to be implemented')

# Route: Get Annotations for Document
# Parameters:
#   - documentID: ID of the document that the user wants annotations for
@app.route('/get_annotations_for_document', methods=['GET'])
def get_annotations_for_document():
    # TODO: Implement logic to retrieve annotations for a document
    return jsonify('Annotation retrieval logic to be implemented')

# Route: Add Document Annotation
# Parameters:
#   - documentID: ID of the document the annotation is being added to
# The JSON for the annotation data should be supplied in the body of the request
@app.route('/add_document_annotation', methods=['POST'])
def add_document_annotation():
    # TODO: Implement logic to add an annotation to a document
    return jsonify('Annotation addition logic to be implemented')

# Route: Edit Document Annotation
# Parameters:
#   - documentID: ID of the document the annotation belongs to (REQUIRED)
#   - annotationID: ID of the annotation to be edited (REQUIRED)
# The JSON for the edited annotation data should be supplied in the body of the request
@app.route('/edit_document_annotation', methods=['POST'])
def edit_document_annotation():
    # TODO: Implement logic to edit an existing annotation for a document
    return jsonify('Annotation editing logic to be implemented')

# Route: Delete Document Annotation
# Parameters:
#   - documentID: ID of the document the annotation belongs to (REQUIRED)
#   - annotationID: ID of the annotation to be deleted (REQUIRED)
@app.route('/delete_document_annotation', methods=['POST'])
def delete_document_annotation():

    ## THIS CODE HASNT BEEN TESTED, PROBABLY DOESNT WORK YET
    ## IT IS THEORETICALLY HOW ANNOTATION DELETION SHOULD WORK

    documentID = request.args.get("documentID")
    annotationID = request.args.get("annotationID")

    # the required parameters were not supplied
    if documentID == "" or annotationID == "":
        result = { "success": False }
        return jsonify(result)

    query = { "documentID" : documentID ,
              "annotationID": annotationID }
    
    collection.delete_one(query)

    result = { "success": True }

    return jsonify(result)

# Route: Generate Dataset for Annotations
@app.route('/generated_dataset_for_annotations', methods=['GET'])
def generated_dataset_for_annotations():
    # TODO: Implement logic to generate a dataset for annotations
    return jsonify('Dataset generation logic to be implemented')

# Route: Generate Attack Flow Visuals
@app.route('/generate_attackflow_visuals', methods=['GET'])
def generate_attackflow_visuals():
    # TODO: Implement logic to generate attack flow visuals
    return jsonify('Attack flow visualization logic to be implemented')

# Route: Get Image
@app.route('/<dir_name>/<image_name>.jpg/', methods=['GET'])
def send_image(image_name, dir_name):
    # Construct the file path for the requested image
    file_path = f"tmp/{dir_name}/{image_name}.jpg"

    # Use Flask's `send_file` function to send the image as a response
    # Set the MIME type to 'image/jpg' to specify the image format
    return send_file(file_path, mimetype='image/jpg')


if __name__ == '__main__':
    app.run()
