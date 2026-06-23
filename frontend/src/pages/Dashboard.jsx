import { Link } from "react-router-dom";

function Dashboard() {

  return (

    <div className="dashboard">

      <h1>Dashboard</h1>

      <br />

      <div className="card">

        <h2>Welcome to Disaster Recovery Platform</h2>

        <br />

        <p>User can register and deploy applications here.</p>

        <br />

        <Link to="/register-application">

          <button>

            Register Application

          </button>

        </Link>

      </div>

    </div>

  );

}

export default Dashboard;