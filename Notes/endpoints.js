// register

// request body
body = {
  username: "",
  password: "",
  confirmPassword: "",
};

//response
//if success
statusCode = 200;
response = {
  message: "Registration Success",
};
//else
statusCode = 401;
response = {
  message: "Username already exists",
};
// else
statusCode = 401;
response = {
  message: "Something went wrong",
};
// =========================================================================
// login

//request body
body = {
  username: "",
  password: "",
};

//response
//if success
statusCode = 200;
response = {
  message: "Login Success",
};
//else
statusCode = 401;
response = {
  message: "Username or password incorrect",
};

// else
statusCode = 401;
response = {
  message: "Something went wrong",
};
