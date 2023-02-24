import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

const App = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [suggestedUsername, setSuggestedUsername] = useState('');
  const [usernameValidity, setUsernameValidity] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/register', { username, email, password });
      setMessage(response.data.message);
      setErrorMessage('');
    } catch (error) {
      setErrorMessage(error.response.data.message);
      setMessage('');
    }
  };

  const handleUsernameBlur = async () => {
    try {
      const response = await axios.get(`/api/check-username/${username}`);
      if (response.data.suggested_username) {
        setSuggestedUsername(response.data.suggested_username);
      } else {
        setSuggestedUsername('');
      }

      setUsernameValidity(response.data.exists ? false : true);
    } catch (error) {
      console.error(error);
      setUsernameValidity(false);
    }
  };

  return (
    <div className="registration-page">
      
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
      {message && <div>{message}</div>}
      {errorMessage && <div>{errorMessage}</div>}
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} onBlur={handleUsernameBlur} />
          {usernameValidity === false && <span style={{ color: 'red' }}>*</span>}
          {usernameValidity === true && <span style={{ color: 'green' }}>&#10004;</span>}
        </label>
        {suggestedUsername && <div>Suggested username: {suggestedUsername}</div>}
        <br />
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        <button type="submit">Register</button>
      </form>
      <div className="already-have-account">
        Already have an account? <a href="/login">Log in</a>
      </div>
    </div>
  );
};

export default App;
