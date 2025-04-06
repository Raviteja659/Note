# from flask import Flask, request, jsonify, make_response, session
# from flask_cors import CORS
# from flask_session import Session
# from flask_socketio import join_room, leave_room, send, SocketIO
# from lib.db.db import register_user, login_user, insert_encryption, get_encryption, getDocuments, getSharedDocuments, getDocumentContent as getDocContent, deleteDocument as deleteDoc,renameDocument as renameDoc, updateFilePermissions as updateFileAccess, newFile as newFileDoc,saveDocumentContent as saveDocContent
# from lib.utils.cryptic import encrypt_to_fixed_length_string, decrypt_from_fixed_length_string
# import traceback
# app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
# socketio = SocketIO(app,cors_allowed_origins="*")
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# @app.route("/register",methods=["POST"])
# def register():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["username"] == "" or json["password"]=="" or json["confirmPassword"]!=json["password"]:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = register_user(json["username"],json["password"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/login",methods=["POST"])
# def login():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["username"] == "" or json["password"]=="":
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = login_user(json["username"],json["password"])
#                 response = make_response(jsonify(result["body"]))
#                 response.status_code = result["status_code"]
#                 enc_object = encrypt_to_fixed_length_string({"ip":request.remote_addr,"username":json["username"]})
#                 insert_encryption(enc_object["identifier"],enc_object["encrypted_data"])
#                 print(enc_object["encrypted_data"])
#                 response.set_cookie('user', enc_object["identifier"], max_age=60*60*24, httponly=True, secure=False, samesite='None')
#                 return response
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response
    
# @app.route("/verifyCookie",methods=["POST"])
# def verifyCookie():
#     try:
#         identifier = request.cookies.get("user")
#         if identifier:
#             enc_signal_obj = get_encryption(identifier)
#             if enc_signal_obj["signal"]:
#                 enc_obj = decrypt_from_fixed_length_string(enc_signal_obj["encrypted_string"])
#                 print(enc_obj)
#                 if enc_obj["ip"] == request.remote_addr:
#                     response = make_response(jsonify({"message":"User Verified"}))
#                     response.status_code = 200
#                     return response
#                 else:
#                     response = make_response(jsonify({"message":"Please login Again"}))
#                     response.status_code = 401
#                     return response
#             else:
#                 response = make_response(jsonify({"message":"Invalid Cookie"}))
#                 response.status_code = 401
#                 return response
#         else:
#             response = make_response(jsonify({"message":"Cookie not found"}))
#             response.status_code = 401
#             return response
#     except Exception as error:
#         print(traceback.format_exec())
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/getUserDocuments",methods=["POST"])
# def getUserDocuments():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["userId"] == "" or json["userId"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = getDocuments(json["userId"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/getSharedDocuments",methods=["POST"])
# def getSharedDocuments():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["userId"] == "" or json["userId"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = getSharedDocuments(json["userId"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response
    
# @app.route("/getDocumentContent",methods=["POST"])
# def getDocumentContent():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = getDocContent(json["userId"], json["fileId"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/deleteDocument",methods=["POST"])
# def deleteDocument():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = deleteDoc(json["userId"], json["fileId"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/renameDocument",methods=["POST"])
# def renameDocument():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = renameDoc(json["userId"], json["fileId"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/updateFilePermissions",methods=["POST"])
# def updateFilePermissions():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None or json["sharedUsers"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = updateFileAccess(json["userId"], json["fileId"], json["sharedUsers"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response
    
# @app.route("/newFile",methods=["POST"])
# def newFile():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["fileName"] == "" or json["fileName"] is None or json["userId"] == "" or json["userId"]  is None or json["dateCreated"] == "" or json["dateCreated"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = newFileDoc(json["userId"], json["fileName"], json["dateCreated"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# @app.route("/saveDocumentContent",methods=["POST"])
# def saveDocumentContent():
#     try:
#         content_type = request.headers.get('Content-Type')
#         if (content_type == 'application/json'):
#             json = request.json
#             if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"]  is None or json["content"] == "" or json["content"] is None:
#                 response = make_response(jsonify({"message":'Invalid Data'}))
#                 response.status_code = 400
#                 return response
#             else:
#                 result = saveDocContent(json["userId"], json["fileName"], json["dateCreated"])
#                 return jsonify(result["body"]),result["status_code"]
#         else:
#             response = make_response(jsonify({"message":'Content-Type not supported!'}))
#             response.status_code = 400
#             return response
#     except Exception as error:
#         response = make_response(jsonify({"message":repr(error)}))
#         response.status_code = 500
#         return response

# if __name__ == "__main__":
#     # app.run(debug=True)
#     socketio.run(app, debug=True)


from flask import Flask, request, jsonify, make_response, session
from flask_cors import CORS
from flask_socketio import join_room, leave_room, send, SocketIO
from lib.db.db import register_user, login_user, insert_encryption, get_encryption, getDocuments, getSharedDocuments, getDocumentContent as getDocContent, deleteDocument as deleteDoc,renameDocument as renameDoc, updateFilePermissions as updateFileAccess, newFile as newFileDoc
from lib.utils.cryptic import encrypt_to_fixed_length_string, decrypt_from_fixed_length_string
import traceback
app = Flask(__name__)
app.config["SECRET_KEY"] = "vafuiwkxdml"
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)
socketio = SocketIO(app,cors_allowed_origins="http://localhost:3000")

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route("/register",methods=["POST"])
def register():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["username"] == "" or json["password"]=="" or json["confirmPassword"]!=json["password"]:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = register_user(json["username"],json["password"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@app.route("/login",methods=["POST"])
def login():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["username"] == "" or json["password"]=="":
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = login_user(json["username"],json["password"])
                response = make_response(jsonify(result["body"]))
                response.status_code = result["status_code"]
                enc_object = encrypt_to_fixed_length_string({"ip":request.remote_addr,"username":json["username"]})
                insert_encryption(enc_object["identifier"],enc_object["encrypted_data"])
                print(enc_object["encrypted_data"])
                response.set_cookie('user', enc_object["identifier"], max_age=60*60*24, httponly=True, secure=False, samesite='None')
                return response
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response
    
@app.route("/verifyCookie",methods=["POST"])
def verifyCookie():
    try:
        identifier = request.cookies.get("user")
        if identifier:
            enc_signal_obj = get_encryption(identifier)
            if enc_signal_obj["signal"]:
                enc_obj = decrypt_from_fixed_length_string(enc_signal_obj["encrypted_string"])
                print(enc_obj)
                if enc_obj["ip"] == request.remote_addr:
                    response = make_response(jsonify({"message":"User Verified"}))
                    response.status_code = 200
                    return response
                else:
                    response = make_response(jsonify({"message":"Please login Again"}))
                    response.status_code = 401
                    return response
            else:
                response = make_response(jsonify({"message":"Invalid Cookie"}))
                response.status_code = 401
                return response
        else:
            response = make_response(jsonify({"message":"Cookie not found"}))
            response.status_code = 401
            return response
    except Exception as error:
        print(traceback.format_exec())
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@app.route("/getUserDocuments",methods=["POST"])
def getUserDocuments():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["userId"] == "" or json["userId"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = getDocuments(json["userId"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@app.route("/getSharedDocuments",methods=["POST"])
def getSharedDocuments():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["userId"] == "" or json["userId"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = getSharedDocuments(json["userId"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response
    
@app.route("/getDocumentContent",methods=["POST"])
def getDocumentContent():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = getDocContent(json["userId"], json["fileId"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@app.route("/deleteDocument",methods=["POST"])
def deleteDocument():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = deleteDoc(json["userId"], json["fileId"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@app.route("/renameDocument",methods=["POST"])
def renameDocument():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = renameDoc(json["userId"], json["fileId"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@app.route("/updateFilePermissions",methods=["POST"])
def updateFilePermissions():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"] is None or json["sharedUsers"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = updateFileAccess(json["userId"], json["fileId"], json["sharedUsers"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response
    
@app.route("/newFile",methods=["POST"])
def newFile():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["fileName"] == "" or json["fileName"] is None or json["userId"] == "" or json["userId"]  is None or json["dateCreated"] == "" or json["dateCreated"] is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                result = newFileDoc(json["userId"], json["fileName"], json["dateCreated"])
                return jsonify(result["body"]),result["status_code"]
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response


rooms={}

@app.route("/preConnect",methods=["POST"])
def preConnect():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json["fileId"] == "" or json["fileId"] is None or json["userId"] == "" or json["userId"]  is None:
                response = make_response(jsonify({"message":'Invalid Data'}))
                response.status_code = 400
                return response
            else:
                session["userId"] = json["userId"]
                session["fileId"] = json["fileId"]
                if json["fileId"] not in rooms.keys():
                    rooms[json["fileId"]] = {"users":[],"changes":[]}
                    return {"message":"Room created for this file"}, 200
                else:
                    return {"message":"Room already exists for this file"}, 200
        else:
            response = make_response(jsonify({"message":'Content-Type not supported!'}))
            response.status_code = 400
            return response
    except Exception as error:
        response = make_response(jsonify({"message":repr(error)}))
        response.status_code = 500
        return response

@socketio.on("connect")
def connect(auth):
    userId = session.get("userId")
    fileId = session.get("fileId")
    if not userId or not fileId:
        return
    if fileId not in rooms.keys():
        leave_room(fileId)
        return
    print("connected")
    join_room(fileId)
    send({"change":"Connected to file room", "userId":""})
    rooms[fileId]["users"].push(userId)

@socketio.on("change")
def change(data):
    userId = session.get("userId")
    fileId = session.get("fileId")
    if not userId or not fileId or fileId not in rooms.keys():
        return
    send({"data":data.content,"userId":userId},to=fileId)
    rooms[fileId]["changes"].append({"data":data.content,"userId":userId})
    print(data.user, fileId, data.content)

@socketio.on("disconnect")
def disconnect():
    userId = session.get("userId")
    fileId = session.get("fileId")
    leave_room(fileId)
    if fileId in rooms.keys():
        rooms[fileId]["users"].remove(userId)
        if len(rooms[fileId]["users"])==0:
            del rooms[fileId]
    send({"change":"Connected to file room", "userId":""})
    print("disconnected", userId, fileId)

if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app, debug=True)