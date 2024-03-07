import React from "react";

import ReactDOM from "react-dom";
import {BrowserRouter} from "react-router-dom";
import { createRoot } from 'react-dom/client';
import {Login} from './components/Login'

import "./index.css";


const container = document.getElementById("app");
const root = createRoot(container);

const App = () => (
  
  <BrowserRouter>
  <h1>ALERT: Auth is Running locally</h1>
    <Login />
  </BrowserRouter>
);

root.render(<App/>)