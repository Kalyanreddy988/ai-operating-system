export default function FileUpload({ setFile }) {
  return (
    <div>
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />
    </div>
  );
}
