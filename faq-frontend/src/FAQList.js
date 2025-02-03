import React, { useEffect, useState } from "react";
import axios from "axios";
import i18n from "./i18n"; //  Import i18n setup

function FAQList() {
  const [faqs, setFaqs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentLang, setCurrentLang] = useState(i18n.language); // Store language state

  useEffect(() => {
    console.log(`Fetching FAQs for language: ${currentLang}`);

    axios
      .get(`http://localhost:8000/api/faqs/?lang=${currentLang}`)
      .then((response) => {
        setFaqs(response.data);
        setLoading(false);
        console.log("FAQs fetched:", response.data);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });

    // Listen for i18n language changes and update state
    const handleLanguageChange = () => {
      setCurrentLang(i18n.language);
    };
    i18n.on("languageChanged", handleLanguageChange);

    return () => {
      i18n.off("languageChanged", handleLanguageChange);
    };
  }, [currentLang]); // Re-run effect when language changes

  if (loading) return <div>Loading FAQs...</div>;
  if (error) return <div>Error loading FAQs: {error.message}</div>;

  return (
    <div>
      {faqs.map((faq) => (
        <div key={faq.id} style={{ marginBottom: "2rem" }}>
          <h3>{faq.question}</h3>
          <div dangerouslySetInnerHTML={{ __html: faq.answer }} />
        </div>
      ))}
    </div>
  );
}

export default FAQList;
