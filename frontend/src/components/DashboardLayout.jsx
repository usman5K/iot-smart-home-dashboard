import React, { useState } from 'react';
import NavBar from './NavBar';
import Drawer from './Drawer';
import styles from '../styles/DashboardLayout.module.css';
import { Outlet } from 'react-router-dom';

const DashboardLayout = () => {
  const [isDrawerOpen, setDrawerOpen] = useState(false);
  const [isDrawerPinned, setDrawerPinned] = useState(false);

  const toggleDrawer = () => {
    setDrawerOpen(!isDrawerOpen);
  };

  const pinDrawer = () => {
    setDrawerPinned(!isDrawerPinned);
    // Close the drawer when unpinning
    if (isDrawerPinned) {
      setDrawerOpen(false); // Close drawer if unpinning
    }
  };

  return (
    <div className={styles.dashboard}>
      <NavBar toggleDrawer={toggleDrawer} />
      <div className={styles.mainLayout}>
        {isDrawerOpen && <Drawer
          isOpen={isDrawerOpen || isDrawerPinned}
          pinDrawer={pinDrawer}
          toggleDrawer={toggleDrawer}
          isPinned={isDrawerPinned}
        />}
        <div className={styles.contentArea}>
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default DashboardLayout;
