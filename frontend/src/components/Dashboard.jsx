//write react component to show you are logged in

import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useApi } from '../context/ApiProvider'; // Import the API hook

const Dashboard = () => {
    const navigate = useNavigate();

    const handleLogout = async () => {
        localStorage.removeItem('token');
        navigate('/login');
    };

    return (
        <div>
            <h2>Dashboard</h2>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Dashboard;