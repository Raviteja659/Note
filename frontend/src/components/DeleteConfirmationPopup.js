import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { deleteDocument } from "../redux/documentsSlice";
import "./Popup.css";

const DeleteConfirmationPopup = ({ fileId, fileName, onClose }) => {
  const currentUser = useSelector((state) => state.login.loginUser);

  const dispatch = useDispatch();

  const handleDelete = () => {
    fetch("http://127.0.0.1:5000/deleteDocument", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userId: currentUser, fileId: fileId }),
    })
      .then((res) => {
        if (res.status === 200) {
          res.json().then((res) => {
            dispatch(deleteDocument(fileId));
          });
        } else {
          res.json().then((res) => {
            alert(res.message);
          });
        }
        onClose();
      })
      .catch((err) => {
        alert("Failed to delete document due to : \n" + err.message);
      });
  };

  return (
    <div className="popup">
      <div className="popup-inner">
        <h2>Delete Document</h2>
        <p>Are you sure you want to delete {fileName}?</p>
        <button onClick={handleDelete}>Delete</button>
        <button onClick={onClose}>Cancel</button>
      </div>
    </div>
  );
};

export default DeleteConfirmationPopup;
