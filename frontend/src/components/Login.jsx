import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom'; // Import Link from react-router-dom
import { useApi } from '../context/ApiProvider';
import styles from '../styles/Login.module.css'; // Import CSS module for styling

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const apiCall = useApi();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        email: email,
        password: password,
      };
      const result = await apiCall('/auth/login', 'POST', payload);
      localStorage.setItem('token', result.access_token);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Login failed');
    }
  };

  return (
    <div className={styles.loginContainer}>
      <form className={styles.loginForm} onSubmit={handleLogin}>
        <h2>Login</h2>
        <div className={styles.formGroup}>
          <label htmlFor="email">Email:</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="password">Password:</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button className={styles.loginButton} type="submit">
          Login
        </button>
        {error && <p className={styles.errorMessage}>{error}</p>}
        <div className={styles.signupLink}>
          <p>Don't have an account? <Link to="/signup">Sign up now</Link></p>
        </div>
      </form>
    </div>
  );
};

export default Login;
