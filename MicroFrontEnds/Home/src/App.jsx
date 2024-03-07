// import { StrictMode } from "react";
import { lazy } from 'react';
import { createRoot } from 'react-dom/client';
import Routes from "./components/Routes";
import {BrowserRouter} from "react-router-dom";
import {StoreProvider} from 'Tools/StoreProvider';

const container = document.getElementById('app');
const root = createRoot(container);

const App = () => (
  <StoreProvider>
    <Routes />
  </StoreProvider>
);

root.render(<App />);