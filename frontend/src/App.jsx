import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Signup from './components/Signup'; 
import Login from './components/Login';
import DashboardLayout from './components/DashboardLayout';
import Dashboard from './components/Dashboard';
import Houses from './components/Houses';
import Areas from './components/Areas';
import Devices from './components/Devices';
import Reports from './components/Reports';
import { ApiProvider } from './context/ApiProvider';
import NotFound from './components/NotFound';

const App = () => {
  // Check if the user is authenticated
  const isAuthenticated = !!localStorage.getItem('token');

  return (
    <ApiProvider>
    <Router>
      <Routes>

        {/* Auth Routes */}
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />

        {/* Protected Routes */}
        <Route path="/dashboard" element={isAuthenticated ? <DashboardLayout /> : <Navigate to="/login" />}>
          <Route path="houses" element={<Houses />} />
          <Route path="areas" element={<Areas />} />
          <Route path="devices" element={<Devices />} />
          <Route path="reports" element={<Reports />} />
          <Route index element={<Dashboard />} />
        </Route>
        
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
    </ApiProvider>
  );
};

export default App;
