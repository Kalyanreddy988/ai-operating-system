import { useState } from "react";

export default function TaskForm() {
  const [goal, setGoal] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("goal", goal);

    try {
      const res = await fetch("http://127.0.0.1:8000/run-task", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("Failed to run AI task");
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h1>🧠 AI Operating System</h1>
      <p className="subtitle">AutoML · CV · Explainability</p>

      <input
        className="input"
        placeholder="do ml tasks"
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
      />

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button className="run-btn" onClick={handleSubmit} disabled={loading}>
        {loading ? "⏳ Training..." : "🚀 Run AI Task"}
      </button>

      {error && <p className="error">{error}</p>}

      {/* ✅ CLEAN RESULT UI */}
      {result && (
        <div className="results-card">
          <h3>📊 Results</h3>

          <p><b>Model:</b> {result.model}</p>
          <p><b>Metric:</b> {result.metric}</p>
          <p><b>Score:</b> {result.score}</p>
          <p><b>Confidence:</b> {result.confidence}</p>

          {result.llm_explanation && (
            <>
              <h4>🧠 LLM Explanation</h4>
              <p>{result.llm_explanation.summary}</p>
            </>
          )}

          {/* ✅ DOWNLOAD BUTTON */}
          {result.model_id && (
            <a
              className="download-btn"
              href={`http://127.0.0.1:8000/download/${result.model_id}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              ⬇ Download Trained Model
            </a>
          )}
        </div>
      )}
    </div>
  );
}
