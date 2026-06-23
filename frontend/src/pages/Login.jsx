import { Link } from "react-router-dom";

function Login() {

  return (

    <div className="container">

      <h1>Login</h1>

      <input type="email" placeholder="Email"/>

      <input type="password" placeholder="Password"/>

      <button>Login</button>

      <div className="link">

        New User?

        <Link to="/signup"> Signup</Link>

      </div>

    </div>

  );

}

export default Login;