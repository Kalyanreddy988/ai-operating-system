import { useState } from "react";
import GoalInput from "./GoalInput";
import LoadingSpinner from "./LoadingSpinner";
import { runTask } from "../services/api";

export default function UploadCard() {

    const [goal, setGoal] = useState("Train ML Model");
    const [file, setFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const [response, setResponse] = useState(null);

    const [error, setError] = useState("");

    async function handleRun() {

        if (!file) {
            alert("Please choose a CSV file.");
            return;
        }

        try {

            setLoading(true);

            setError("");

            setResponse(null);

            const result = await runTask(goal, file);

            setResponse(result);

        }

        catch (err) {

            setError(err.message);

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <div className="card">

            <h2>Upload Dataset</h2>

            <GoalInput
                goal={goal}
                setGoal={setGoal}
            />

            <br />

            <input
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <br /><br />

            <button
                className="run-btn"
                onClick={handleRun}
            >
                🚀 Run AI Task
            </button>

            <br /><br />

            {loading && <LoadingSpinner />}

            {error &&

                <div className="error-box">

                    {error}

                </div>

            }

            {response &&

                <pre className="json-box">

                    {JSON.stringify(response, null, 2)}

                </pre>

            }

        </div>

    );

}