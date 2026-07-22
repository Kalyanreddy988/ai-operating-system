def decompose(plan: dict):
    """
    Converts a high-level plan into executable tasks.
    """

    tasks = []

    for index, step in enumerate(plan["steps"], start=1):
        tasks.append({
            "id": index,
            "task": step,
            "status": "pending"
        })

    return tasks