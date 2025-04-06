import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  username: "",
  password: "",
  loginUser: "",
  isLogin: false,
};

const loginSlice = createSlice({
  name: "login",
  initialState,
  reducers: {
    setLoginData: (state, action) => {
      state[action.payload.name] = action.payload.value;
    },
    setLoginUser: (state, action) => {
      state.loginUser = action.payload;
      state.isLogin = true;
    },
    setLogout: (state) => {
      state.isLogin = false;
    },
    resetLoginForm: () => initialState,
  },
});

export const { setLoginData, resetLoginForm, setLoginUser, setLogout } =
  loginSlice.actions;
export default loginSlice.reducer;
