import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import DOMPurify from "dompurify";
import { useNavigate } from "react-router-dom";
import {
  setLoginData,
  resetLoginForm,
  setLoginUser,
} from "../redux/loginSlice";
import FormInput from "./FormInput";
import Button from "./Button";
import "./Login.css";

const Login = () => {
  const dispatch = useDispatch();
  const loginData = useSelector((state) => state.login);
  const [errors, setErrors] = useState({});
  const [message, setMessage] = useState("");
  const [passwordVisible, setPasswordVisible] = useState(false);
  const navigate = useNavigate();
  const handleChange = (e) => {
    const sanitizedValue = DOMPurify.sanitize(e.target.value);
    dispatch(setLoginData({ name: e.target.name, value: sanitizedValue }));
  };

  useEffect(() => {
    fetch("http://127.0.0.1:5000/verifyCookie", {
      method: "POST",
      credentials: "include",
    })
      .then((res) => {
        if (res.status === 200) {
          res.json().then((res) => {
            dispatch(setLoginUser(res.userId));
            let goToDashBoard = () => navigate("/dashboard");
            goToDashBoard();
          });
        }
      })
      .catch((err) => {
        alert(err.message);
      });
  }, []);

  const validate = () => {
    const errors = {};
    if (!loginData.username.trim()) {
      errors.username = "Username is required";
    }
    if (!loginData.password) {
      errors.password = "Password is required";
    }
    return errors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    try {
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: loginData.username,
          password: loginData.password,
        }),
      });
      const data = await response.json();
      if (response.ok) {
        setMessage("Login successful!");
        dispatch(setLoginUser(loginData.username));
        dispatch(resetLoginForm());
        let goToDashBoard = () => navigate("/dashboard");
        goToDashBoard();
      } else {
        setMessage(`Login failed: ${data.message}`);
      }
    } catch (error) {
      setMessage(`Login failed: ${error.message}`);
    }
  };

  return (
    <div className="login">
      <h2>Login</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <FormInput
          type="text"
          name="username"
          label="Username"
          value={loginData.username}
          onChange={handleChange}
          error={errors.username}
        />
        <FormInput
          type={passwordVisible ? "text" : "password"}
          name="password"
          label="Password"
          value={loginData.password}
          onChange={handleChange}
          error={errors.password}
          toggleVisibility={() => setPasswordVisible(!passwordVisible)}
          isPassword
        />
        <Button type="submit" label="Login" />
      </form>
    </div>
  );
};

export default Login;
