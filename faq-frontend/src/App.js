import React, { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import "./i18n"; // Import the i18n configuration
import FAQList from "./FAQList";
import ReactQuill from "react-quill"; // Import React Quill
import "react-quill/dist/quill.snow.css"; // Import the React Quill CSS
import "./App.css";
import QuillEditor from "./components/QuillEditor"; // Import the custom Quill editor
import "./components/MyEditor.css"; // Import the custom Quill editor;

function App() {
  const { t, i18n } = useTranslation();
  const [editorContent, setEditorContent] = useState(""); // State for the editor content
  const [faqs, setFaqs] = useState([]); // State to store fetched FAQ data

  const changeLanguage = (event) => {
    console.log(`Language switched to: ${event.target.value}`); // Log language switch
    i18n.changeLanguage(event.target.value); // Change language
  };

  const handleSearch = (query) => {
    console.log("Performing search for:", query);
  };

  const fetchFAQs = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/faqs/?lang=${i18n.language}`,
        {
          method: "GET",
          headers: {
            "Accept-Language": i18n.language, // Pass language in the headers
          },
        }
      );
      // Add lang to the API call
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json(); // Parse the response to JSON
      setFaqs(data); // Set FAQs data to state
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error); // Handle errors
    }
  };

  useEffect(() => {
    fetchFAQs();
  }, [i18n.language]);

  // Handle changes in the editor content
  const handleEditorChange = (value) => {
    setEditorContent(value);
  };

  return (
    <div className="App">
      <header style={{ padding: "1rem", background: "#f5f5f5" }}>
        <h2>{t("title")}</h2>
        <label htmlFor="language">{t("selectLanguage")}: </label>
        <select
          id="language"
          value={i18n.language}
          onChange={changeLanguage}
          style={{ marginLeft: "0.5rem" }}
        >
          <option value="en">English</option>
          <option value="hi">Hindi</option>
          <option value="bn">Bengali</option>
          <option value="fr">French</option>
          <option value="de">German</option>
          <option value="es">Spanish</option>
          <option value="it">Italian</option>
          <option value="pt">Portuguese</option>
          <option value="ru">Russian</option>
          <option value="zh">Chinese</option>
          <option value="ja">Japanese</option>
          <option value="ko">Korean</option>
          <option value="ar">Arabic</option>
          <option value="tr">Turkish</option>
          <option value="nl">Dutch</option>
          <option value="pl">Polish</option>
          <option value="id">Indonesian</option>
          <option value="th">Thai</option>
          <option value="vi">Vietnamese</option>
          <option value="fa">Persian</option>
          <option value="he">Hebrew</option>
          <option value="pa">Punjabi</option>
          <option value="gu">Gujarati</option>
          <option value="mr">Marathi</option>
          <option value="ta">Tamil</option>
          <option value="te">Telugu</option>
          <option value="ur">Urdu</option>
          <option value="ml">Malayalam</option>
          <option value="kn">Kannada</option>
          <option value="or">Odia</option>
          <option value="as">Assamese</option>
          <option value="ma">Maithili</option>
          <option value="bh">Bhojpuri</option>
          <option value="sd">Sindhi</option>
          <option value="ne">Nepali</option>
          <option value="sn">Shona</option>
        </select>
      </header>
      <main style={{ padding: "1rem" }}>
        <h1 style={{ color: "red" }}>{t("faqTitle")}</h1>{" "}
        {/* Dynamically changing the FAQ title */}
        <div>
          <h3>Search Your Question</h3>
          <QuillEditor onSearch={handleSearch} />
        </div>
        <FAQList faqs={faqs} />
      </main>
    </div>
  );
}

export default App;
