import React from 'react';
import ReactDOM from 'react-dom/client';
import './assets/css/index.css';
import Main from './components/Main';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './components/App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Router>
      <App />
    </Router>
);
