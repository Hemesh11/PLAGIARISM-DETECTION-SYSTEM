import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import Upload from "./components/Upload";

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/upload" element={<Upload />} />
            </Routes>
        </Router>
    );
};

export default App;
