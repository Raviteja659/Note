import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateSharedUsers } from "../redux/documentsSlice";
import "./Popup.css";

const SharePopup = ({ fileId, sharedUsers = [], onClose }) => {
  const [users, setUsers] = useState(sharedUsers);
  const [newUserId, setNewUserId] = useState("");
  const [permissions, setPermissions] = useState({ view: false, edit: false });
  const [error, setError] = useState("");
  const dispatch = useDispatch();
  const currentUser = useSelector((state) => state.login.loginUser);

  const handleAddUser = () => {
    const userPermissions = Object.keys(permissions).filter(
      (permission) => permissions[permission]
    );
    if (
      newUserId &&
      userPermissions.length > 0 &&
      !users.some((user) => user.userId === newUserId)
    ) {
      setUsers([...users, { userId: newUserId, permissions: userPermissions }]);
      setNewUserId("");
      setPermissions({ view: false, edit: false });
      setError("");
    } else {
      setError(
        "Please enter a valid user ID and select at least one permission."
      );
    }
  };

  const handleRemoveUser = (userId) => {
    setUsers(users.filter((user) => user.userId !== userId));
  };

  const handlePermissionChange = (e) => {
    const { name, checked } = e.target;
    setPermissions({ ...permissions, [name]: checked });
  };

  const handleSave = () => {
    let su = [];
    for (var i = 0; i < sharedUsers.length; i++) {
      su.push({
        userId: sharedUsers[i].userId,
        permission: sharedUsers[i].permissions.join(","),
      });
    }
    console.log(su);
    fetch("http://127.0.0.1:5000/updateFilePermissions", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: currentUser,
        fileId: fileId,
        sharedUsers: su,
      }),
    })
      .then((res) => {
        if (res.status === 200) {
          res.json().then((res) => {
            dispatch(updateSharedUsers({ fileId, sharedUsers: users }));
          });
        } else {
          res.json().then((res) => {
            alert(res.message);
          });
        }
      })
      .catch((err) => {
        alert("Failed to fetch documents due to : \n" + err.message);
      });
    onClose();
  };

  return (
    <div className="popup">
      <div className="popup-inner">
        <h2>Share Document</h2>
        <div>
          <input
            type="text"
            placeholder="Enter user ID"
            value={newUserId}
            onChange={(e) => setNewUserId(e.target.value)}
          />
          <div>
            <label>
              <input
                type="checkbox"
                name="view"
                checked={permissions.view}
                onChange={handlePermissionChange}
              />
              View
            </label>
            <label>
              <input
                type="checkbox"
                name="edit"
                checked={permissions.edit}
                onChange={handlePermissionChange}
              />
              Edit
            </label>
          </div>
          <button onClick={handleAddUser}>Add User</button>
          {error && <p className="error">{error}</p>}
        </div>
        <ul>
          {users.map((user) => (
            <li key={user.userId}>
              <span>
                {user.userId} - {user.permissions.join(", ")}
              </span>
              <button onClick={() => handleRemoveUser(user.userId)}>
                Remove
              </button>
            </li>
          ))}
        </ul>
        <button onClick={handleSave}>Save</button>
        <button onClick={onClose}>Cancel</button>
      </div>
    </div>
  );
};

export default SharePopup;
