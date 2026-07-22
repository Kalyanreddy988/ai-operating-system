export default function GoalInput({ goal, setGoal }) {
    return (
        <div className="input-group">
            <label>AI Goal</label>

            <input
                className="text-input"
                type="text"
                placeholder="Example: Train ML Model"
                value={goal}
                onChange={(e) => setGoal(e.target.value)}
            />
        </div>
    );
}