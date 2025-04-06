import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import {
  setSharedDocuments,
  setCurrentDocument,
} from "../redux/documentsSlice";
import "./SharedDocuments.css";
import { setLoginUser } from "../redux/loginSlice";

const SharedDocuments = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const currentUser = useSelector((state) => state.login.loginUser);
  const sharedDocuments = useSelector(
    (state) => state.documents.sharedDocuments
  );

  useEffect(() => {
    // fetch("http://127.0.0.1:3658/m1/593636-0-default/getSharedDocuments", {
    //   method: "POST",
    //   credentials: "include",
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    //   body: JSON.stringify({ userId: currentUser }),
    // })
    //   .then((res) => {
    //     if (res.status === 200) {
    //       res.json().then((res) => {
    //         let fetchedSharedDocuments = [...res.filesList];
    //         let l = [];
    //         for (var i = 0; i < fetchedSharedDocuments.length; i++) {
    //           let su = [];
    //           for (
    //             var j = 0;
    //             j < fetchedSharedDocuments[i].sharedUsers.length;
    //             j++
    //           ) {
    //             let obj = {
    //               ...fetchedSharedDocuments[i].sharedUsers[j],
    //             };
    //             su.push({
    //               userId: obj.userId,
    //               permissions: obj.permission.split(","),
    //             });
    //           }
    //           fetchedSharedDocuments[i].sharedUsers = [...su];
    //           fetchedSharedDocuments[i].permissions =
    //             fetchedSharedDocuments[i].permissions.split(",");
    //           l.push(fetchedSharedDocuments[i]);
    //         }
    //         dispatch(setSharedDocuments(l));
    //       });
    //     } else {
    //       res.json().then((res) => {
    //         alert(res.message);
    //       });
    //     }
    //   })
    //   .catch((err) => {
    //     alert("Failed to fetch documents due to : \n" + err.message);
    //   });
    // fetch("http://127.0.0.1:5000/verifyCookie", {
    //   method: "POST",
    // })
    //   .then((res) => {
    //     if (res.status === 200) {
    //       res.json().then((res) => {
    //         dispatch(setLoginUser(res.userId));
    //         fetch("http://127.0.0.1:5000/getSharedDocuments", {
    //           method: "POST",
    //           credentials: "include",
    //           headers: {
    //             "Content-Type": "application/json",
    //           },
    //           body: JSON.stringify({ userId: currentUser }),
    //         })
    //           .then((res) => {
    //             if (res.status === 200) {
    //               res.json().then((res) => {
    //                 let fetchedSharedDocuments = [...res.filesList];
    //                 let l = [];
    //                 for (var i = 0; i < fetchedSharedDocuments.length; i++) {
    //                   let su = [];
    //                   for (
    //                     var j = 0;
    //                     j < fetchedSharedDocuments[i].sharedUsers.length;
    //                     j++
    //                   ) {
    //                     let obj = {
    //                       ...fetchedSharedDocuments[i].sharedUsers[j],
    //                     };
    //                     su.push({
    //                       userId: obj.userId,
    //                       permissions: obj.permission.split(","),
    //                     });
    //                   }
    //                   fetchedSharedDocuments[i].sharedUsers = [...su];
    //                   fetchedSharedDocuments[i].permissions =
    //                     fetchedSharedDocuments[i].permissions.split(",");
    //                   l.push(fetchedSharedDocuments[i]);
    //                 }
    //                 dispatch(setSharedDocuments(l));
    //               });
    //             } else {
    //               res.json().then((res) => {
    //                 alert(res.message);
    //               });
    //             }
    //           })
    //           .catch((err) => {
    //             alert("Failed to fetch documents due to : \n" + err.message);
    //           });
    //       });
    //     } else {
    //       let goToLogin = () => dispatch("/login");
    //       goToLogin();
    //       dispatch(setLoginUser(""));
    //     }
    //   })
    //   .catch((err) => {
    //     alert(err.message);
    //   });
  }, [dispatch]);

  const handleViewClick = (doc) => {
    dispatch(setCurrentDocument(doc));
    navigate(`/dashboard/view-document/${doc.fileId}`);
  };

  const handleEditClick = (doc) => {
    dispatch(setCurrentDocument(doc));
    navigate(`/dashboard/edit-document/${doc.fileId}`);
  };

  return (
    <div className="shared-documents">
      <h2>Shared Documents</h2>
      <div className="document-headers">
        <span className="file-name">File Name</span>
        <span className="owner-name">Owner</span>
        <span className="permissions">Permissions</span>
        <span className="actions">Actions</span>
      </div>
      <ul>
        {sharedDocuments.map((doc) => (
          <li key={doc.fileId}>
            <div className="document-info">
              <span className="file-name">{doc.fileName}</span>
              <span className="owner-name">{doc.ownerName}</span>
              <span className="permissions">{doc.permissions.join(", ")}</span>
            </div>
            <div className="document-actions">
              {doc.permissions.includes("view") && (
                <button
                  className="icon-button"
                  title="View"
                  onClick={() => handleViewClick(doc)}
                >
                  <i className="fas fa-eye"></i>
                </button>
              )}
              {doc.permissions.includes("edit") && (
                <button
                  className="icon-button"
                  title="Edit"
                  onClick={() => handleEditClick(doc)}
                >
                  <i className="fas fa-edit"></i>
                </button>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SharedDocuments;
