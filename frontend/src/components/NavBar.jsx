import React, { useState, useEffect } from 'react';
import { FaBars, FaBell } from 'react-icons/fa';
import styles from '../styles/NavBar.module.css';
import { useNavigate } from 'react-router-dom';

const NavBar = ({ toggleDrawer }) => {
  const [currentTime, setCurrentTime] = useState('');

  const navigate = useNavigate();

  const handleLogout = async () => {
      localStorage.removeItem('token');
      navigate('/login');
  };

  // Update time every second
  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date();
      setCurrentTime(now.toLocaleTimeString());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <nav className={styles.navBar}>
      <div className={styles.leftSection}>
        <FaBars className={styles.drawerIcon} onClick={toggleDrawer} />
        <span className={styles.companyName}>IoT Smart Homes</span>
      </div>
      <div className={styles.rightSection}>
        <FaBell className={styles.bellIcon} />
        <span className={styles.time}>{currentTime}</span>
        <div className={styles.avatar}>
          <img src="/avatar.png" alt="User Avatar" />
          <ul className={styles.dropdown}>
            <li>Profile</li>
            <li onClick={handleLogout}>Logout</li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
