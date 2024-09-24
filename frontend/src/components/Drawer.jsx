import React from 'react';
import { NavLink } from 'react-router-dom'; // For navigation
import styles from '../styles/Drawer.module.css';

const Drawer = ({ isOpen, pinDrawer, toggleDrawer, isPinned }) => {
  const handlePinToggle = () => {
    pinDrawer();
    if (isPinned) {
      toggleDrawer();
    }
  };

  return (
    <div className={`${styles.drawer} ${isOpen ? styles.open : ''}`}>
      <nav className={styles.navMenu}>
        <NavLink
          to="/dashboard"
          className={({ isActive }) => (isActive ? styles.active : undefined)}
          end
        >
          Dashboard
        </NavLink>
        <NavLink
          to="/dashboard/houses"
          className={({ isActive }) => (isActive ? styles.active : undefined)}
        >
          Houses
        </NavLink>
        <NavLink
          to="/dashboard/areas"
          className={({ isActive }) => (isActive ? styles.active : undefined)}
        >
          Areas
        </NavLink>
        <NavLink
          to="/dashboard/devices"
          className={({ isActive }) => (isActive ? styles.active : undefined)}
        >
          Devices
        </NavLink>
        <NavLink
          to="/dashboard/reports"
          className={({ isActive }) => (isActive ? styles.active : undefined)}
        >
          Reports
        </NavLink>
      </nav>
      <button onClick={handlePinToggle} className={styles.pinButton}>
        {isPinned ? 'Unpin Drawer' : 'Pin Drawer'}
      </button>
    </div>
  );
};

export default Drawer;
