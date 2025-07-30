import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { ResponsiveContainer, ComposedChart, XAxis, YAxis, Tooltip, CartesianGrid, Bar } from "recharts";

const Upload = () => {
    const [files, setFiles] = useState([]);
    const [report, setReport] = useState([]);
    const navigate = useNavigate();

    const handleFileChange = (e) => {
        setFiles(e.target.files);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        for (let file of files) {
            formData.append("files", file);
        }

        try {
            const response = await axios.post("http://127.0.0.1:5000/upload", formData);
            setReport(response.data.similarity_report);
        } catch (error) {
            console.error("Error uploading files:", error);
        }
    };

    const handleLogout = () => {
        navigate("/"); // Redirect to Login Page
    };

    return (
        <div style={{ textAlign: "center", padding: "20px" }}>
            <h2>Upload PDFs for Plagiarism Check</h2>
            <button onClick={handleLogout} style={{ marginBottom: "10px" }}>Logout</button>
            <input type="file" multiple onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload & Analyze</button>

            {report.length > 0 && (
                <div>
                    <h3>Similarity Report</h3>
                    <table border="1" style={{ margin: "auto", marginBottom: "20px" }}>
                        <thead>
                            <tr>
                                <th>File 1</th>
                                <th>File 2</th>
                                <th>Similarity Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            {report.map((entry, index) => (
                                <tr key={index}>
                                    <td>{entry["File 1"]}</td>
                                    <td>{entry["File 2"]}</td>
                                    <td>{entry["Similarity Score"]}%</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>

                    {/* Heatmap Visualization */}
                    <h3>Heatmap Visualization</h3>
                    <ResponsiveContainer width="80%" height={300}>
                        <ComposedChart
                            data={report.map(entry => ({
                                name: `${entry["File 1"]} vs ${entry["File 2"]}`,
                                similarity: entry["Similarity Score"]
                            }))}
                            layout="vertical"
                        >
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis type="number" domain={[0, 100]} />
                            <YAxis dataKey="name" type="category" width={150} />
                            <Tooltip />
                            <Bar dataKey="similarity" fill="#8884d8" barSize={20} />
                        </ComposedChart>
                    </ResponsiveContainer>
                </div>
            )}
        </div>
    );
};

export default Upload;
