import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import "./MyEditor.css";

function MyEditor() {
  const [editorContent, setEditorContent] = useState("");

  const handleSubmit = async () => {
    const query = editorContent; // Get the text from the editor
    const response = await fetch(
      `http://localhost:8000/api/faqs/search/?query=${encodeURIComponent(
        query
      )}`,
      {
        method: "GET",
      }
    );

    if (response.ok) {
      const data = await response.json();
      console.log(data); // Handle the response
    } else {
      console.error("Search failed with status:", response.status);
    }
  };

  return (
    <div style={{ textAlign: "left", width: "100%" }}>
      <ReactQuill
        value={editorContent}
        onChange={setEditorContent}
        placeholder="Write your FAQ here..."
      />

      {/* Submit Button */}
      <button
        onClick={handleSubmit}
        // style={{
        //   marginTop: "10px",
        //   padding: "10px 15px",
        //   backgroundColor: "#007bff",
        //   color: "white",
        //   border: "none",
        //   borderRadius: "5px",
        //   cursor: "pointer",
        //   fontSize: "16px",
        // }}
      >
        Search FAQ
      </button>
    </div>
  );
}

export default MyEditor;
