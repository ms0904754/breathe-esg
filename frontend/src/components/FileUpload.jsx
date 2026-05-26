import { useState } from "react";
import api from "../api/api";

export default function FileUpload({ onUploadSuccess }) {

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      setLoading(true);

      await api.post(
        "/emissions/upload/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      alert("File uploaded successfully");

      onUploadSuccess();

    } catch (error) {

      console.error(error);

      alert("Upload failed");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div
      style={{
        marginBottom: "20px",
      }}
    >

      <input
        type="file"
        accept=".csv"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <button
        onClick={handleUpload}
        style={{
          marginLeft: "10px",
          padding: "8px 16px",
          cursor: "pointer",
        }}
      >

        {loading
          ? "Uploading..."
          : "Upload CSV"}

      </button>

    </div>
  );
}