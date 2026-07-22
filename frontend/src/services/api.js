const API_URL = "http://127.0.0.1:8000";

export async function runTask(goal, file) {
    const formData = new FormData();

    formData.append("goal", goal);
    formData.append("file", file);

    const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        const error = await response.text();
        throw new Error(error);
    }

    return await response.json();
}