import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useApi } from '../context/ApiProvider';
import styles from '../styles/Signup.module.css';

const Signup = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const apiCall = useApi();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        first_name: firstName,
        last_name: lastName,
        email: email,
        password: password,
      };
      const result = await apiCall('/auth/register', 'POST', payload);
      localStorage.setItem('token', result.access_token);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Signup failed');
    }
  };

  return (
    <div className={styles.signupContainer}>
      <form className={styles.signupForm} onSubmit={handleSignup}>
        <h2>Join IoT Systems</h2>
        <div className={styles.formGroup}>
          <label htmlFor='fname'>First Name:</label>
          <input
            id="fname"
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="lname">Last Name:</label>
          <input
            id="lname"
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </div>
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
        <button className={styles.signupButton} type="submit">
          Signup
        </button>
        {error && <p className={styles.errorMessage}>{error}</p>}
        <div className={styles.signinLink}>
        <p>Already have an account? <Link to="/login">Sign in</Link></p>
      </div>
      </form>
    </div>
  );
};

export default Signup;
