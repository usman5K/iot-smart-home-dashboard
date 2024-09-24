import React from 'react';
import { Link } from 'react-router-dom';
import styles from '../styles/NotFound.module.css'; // Import CSS module

const NotFound = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>404</h1>
      <p className={styles.message}>Oops! The page you're looking for doesn't exist.</p>
      <Link to="/dashboard" className={styles.backLink}>Back to Dashboard</Link>
    </div>
  );
};

export default NotFound;
