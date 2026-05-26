import FileUpload from "../components/FileUpload";
import { useEffect, useState } from "react";
import api from "../api/api";

export default function Dashboard() {

  const [records, setRecords] = useState([]);

  const [filter, setFilter] = useState("ALL");

  const fetchRecords = async () => {

    try {

      const response = await api.get(
        "/emissions/records/"
      );

      setRecords(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const reviewRecord = async (id, action) => {

    try {

      await api.patch(
        `/emissions/review/${id}/`,
        { action }
      );

      fetchRecords();

    } catch (error) {

      console.error(error);
    }
  };

  useEffect(() => {

    fetchRecords();

  }, []);

  const filteredRecords = records.filter((record) => {

    if (filter === "APPROVED") {
      return record.status === "APPROVED";
    }

    if (filter === "REJECTED") {
      return record.status === "REJECTED";
    }

    if (filter === "SUSPICIOUS") {
      return record.is_suspicious;
    }

    return true;
  });

  return (

    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        backgroundColor: "#f4f6f8",
        minHeight: "100vh",
      }}
    >

      <h1
        style={{
          marginBottom: "20px",
        }}
      >
        ESG Analyst Dashboard
      </h1>

      <div
        style={{
          display: "flex",
          gap: "20px",
          marginBottom: "20px",
          flexWrap: "wrap",
        }}
      >

        <StatCard
          title="Total Records"
          value={records.length}
        />

        <StatCard
          title="Approved"
          value={
            records.filter(
              (r) => r.status === "APPROVED"
            ).length
          }
        />

        <StatCard
          title="Rejected"
          value={
            records.filter(
              (r) => r.status === "REJECTED"
            ).length
          }
        />

        <StatCard
          title="Suspicious"
          value={
            records.filter(
              (r) => r.is_suspicious
            ).length
          }
        />

      </div>

      <FileUpload onUploadSuccess={fetchRecords} />

      <select
        value={filter}

        onChange={(e) =>
          setFilter(e.target.value)
        }

        style={{
          marginBottom: "20px",
          padding: "10px",
          borderRadius: "6px",
        }}
      >

        <option value="ALL">
          All Records
        </option>

        <option value="APPROVED">
          Approved
        </option>

        <option value="REJECTED">
          Rejected
        </option>

        <option value="SUSPICIOUS">
          Suspicious
        </option>

      </select>

      <div
        style={{
          overflowX: "auto",
          backgroundColor: "white",
          borderRadius: "10px",
          padding: "20px",
          boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
        }}
      >

        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
          }}
        >

          <thead>

            <tr
              style={{
                backgroundColor: "#1f2937",
                color: "white",
              }}
            >

              <th style={thStyle}>Description</th>
              <th style={thStyle}>Category</th>
              <th style={thStyle}>Quantity</th>
              <th style={thStyle}>Unit</th>
              <th style={thStyle}>Scope</th>
              <th style={thStyle}>Status</th>
              <th style={thStyle}>Suspicious</th>
              <th style={thStyle}>Actions</th>

            </tr>

          </thead>

          <tbody>

            {filteredRecords.map((record) => (

              <tr
                key={record.id}

                style={{
                  backgroundColor:
                    record.is_suspicious
                      ? "#ffe5e5"
                      : "white",
                }}
              >

                <td style={tdStyle}>
                  {record.description}
                </td>

                <td style={tdStyle}>
                  {record.category}
                </td>

                <td style={tdStyle}>
                  {record.quantity}
                </td>

                <td style={tdStyle}>
                  {record.unit}
                </td>

                <td style={tdStyle}>
                  {record.scope}
                </td>

                <td style={tdStyle}>

                  <span
                    style={{
                      padding: "6px 10px",
                      borderRadius: "6px",
                      color: "white",

                      backgroundColor:
                        record.status === "APPROVED"
                          ? "#16a34a"
                          : record.status === "REJECTED"
                          ? "#dc2626"
                          : "#f59e0b",
                    }}
                  >

                    {record.status}

                  </span>

                </td>

                <td style={tdStyle}>

                  {record.is_suspicious
                    ? "⚠️ Yes"
                    : "No"}

                </td>

                <td style={tdStyle}>

                  <button
                    onClick={() =>
                      reviewRecord(
                        record.id,
                        "approve"
                      )
                    }

                    style={{
                      marginRight: "10px",
                      backgroundColor: "#16a34a",
                      color: "white",
                      border: "none",
                      padding: "8px 14px",
                      borderRadius: "6px",
                      cursor: "pointer",
                    }}
                  >
                    Approve
                  </button>

                  <button
                    onClick={() =>
                      reviewRecord(
                        record.id,
                        "reject"
                      )
                    }

                    style={{
                      backgroundColor: "#dc2626",
                      color: "white",
                      border: "none",
                      padding: "8px 14px",
                      borderRadius: "6px",
                      cursor: "pointer",
                    }}
                  >
                    Reject
                  </button>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

function StatCard({ title, value }) {

  return (

    <div
      style={{
        backgroundColor: "white",
        padding: "20px",
        borderRadius: "10px",
        minWidth: "180px",
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
      }}
    >

      <h3>{title}</h3>

      <h1>{value}</h1>

    </div>
  );
}

const thStyle = {
  padding: "14px",
  textAlign: "left",
};

const tdStyle = {
  padding: "14px",
  borderBottom: "1px solid #ddd",
};