export async function runTask(goal, file) {
  const formData = new FormData();
  formData.append("files", file);

  const response = await fetch(
    `http://127.0.0.1:8000/run-task?user_goal=${encodeURIComponent(goal)}`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error("Backend error");
  }

  return await response.json();
}
