function RegisterApplication() {

  return (

    <div className="container">

      <h1>Register Application</h1>

      <input
        type="text"
        placeholder="Application Name"
      />

      <input
        type="text"
        placeholder="Docker Image URL"
      />

      <input
        type="number"
        placeholder="Application Port"
      />

      <input
        type="text"
        placeholder="Health Check Endpoint"
      />

      <button>

        Deploy Application

      </button>

    </div>

  );

}

export default RegisterApplication;