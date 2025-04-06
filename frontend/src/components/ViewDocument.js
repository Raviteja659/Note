import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./ViewDocument.css";
import { setLoginUser } from "../redux/loginSlice";
import io from "socket.io-client";
const socket = io.connect("http://localhost:3001");

const ViewDocument = () => {
  const currentUser = useSelector((state) => state.login.loginUser);
  // const currentUser = "chandu";
  const [content, setContent] = useState("");
  const currentDocument = useSelector(
    (state) => state.documents.currentDocument
  );
  const dispatch = useDispatch();
  const [roomMessage, setRoomMessage] = useState("");

  const joinRoom = () => {
    if (currentDocument.fileId !== "") {
      socket.emit("join_room", {
        fileId: currentDocument.fileId,
        userId: currentUser,
      });
    }
  };

  const sendMessage = (content) => {
    socket.emit("send_message", {
      userId: currentUser,
      fileId: currentDocument.fileId,
      content: content,
    });
  };

  useEffect(() => {
    socket.on("receive_message", (data) => {
      if (data.roomMessage) {
        setRoomMessage(data.roomMessage);
      }
      if (data.userId && data.newContent) {
        setContent(data.newContent);
      }
    });
  }, [socket]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/verifyCookie", {
      method: "POST",
    })
      .then((res) => {
        if (res.status === 200) {
          res.json().then((res) => {
            dispatch(setLoginUser(res.userId));
            if (currentDocument) {
              fetch("http://127.0.0.1:5000/getDocumentContent", {
                method: "POST",
                credentials: "include",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  userId: currentUser,
                  fileId: currentDocument.fileId,
                }),
              })
                .then((res) => {
                  if (res.status === 200) {
                    res.json().then((res) => {
                      setContent(res.fileContent);
                      joinRoom();
                    });
                  } else {
                    res.json().then((res) => {
                      alert(res.message);
                    });
                  }
                })
                .catch((err) => {
                  alert(
                    "Failed to fetch the document content due to : \n",
                    err.message
                  );
                });
            }
          });
        } else {
          let goToLogin = () => dispatch("/login");
          goToLogin();
          dispatch(setLoginUser(""));
        }
      })
      .catch((err) => {
        alert(err.message);
      });
  }, []);

  if (!currentDocument) {
    return <div>No document selected</div>;
  }

  return (
    <div className="view-document">
      <div className="document-info">
        <h2>Document Viewer</h2>
        <p>
          <strong>File Name:</strong> {currentDocument.fileName}
        </p>
        <p>
          <strong>File ID:</strong> {currentDocument.fileId}
        </p>
        {currentDocument.ownerName && (
          <p>
            <strong>Owner:</strong> {currentDocument.ownerName}
          </p>
        )}
        {roomMessage.length !== 0 ? <p>{roomMessage}</p> : <></>}
        {currentDocument.sharedUsers && (
          <div>
            <strong>Shared With:</strong>
            <ul>
              {currentDocument.sharedUsers.map((user, index) => (
                <li key={index}>
                  {user.userId} - {user.permissions.join(", ")}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
      <div className="viewer">
        <textarea
          className="viewer-textarea"
          value={content}
          readOnly
        ></textarea>
      </div>
    </div>
  );
};

export default ViewDocument;
