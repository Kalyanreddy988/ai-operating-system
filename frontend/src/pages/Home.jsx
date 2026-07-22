import Navbar from "../components/Navbar";
import UploadCard from "../components/UploadCard";

export default function Home() {
  return (
    <>
      <Navbar />

      <div className="dashboard">

        <UploadCard />

      </div>

    </>
  );
}