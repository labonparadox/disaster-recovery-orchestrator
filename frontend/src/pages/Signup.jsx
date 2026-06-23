import { useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";

function Signup() {

  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const handleSignup = async () => {

    try {

      const response = await api.post("/signup", {

        name,

        email,

        password,

      });

      alert(response.data.message);

    }

    catch (error) {

      console.log(error);

      alert("Signup Failed");

    }

  };

  return (

    <div className="container">

      <h1>Signup</h1>

      <input

        type="text"

        placeholder="Name"

        value={name}

        onChange={(e) => setName(e.target.value)}

      />

      <input

        type="email"

        placeholder="Email"

        value={email}

        onChange={(e) => setEmail(e.target.value)}

      />

      <input

        type="password"

        placeholder="Password"

        value={password}

        onChange={(e) => setPassword(e.target.value)}

      />

      <button onClick={handleSignup}>

        Signup

      </button>

      <div className="link">

        Already have an account?

        <Link to="/"> Login</Link>

      </div>

    </div>

  );

}

export default Signup;