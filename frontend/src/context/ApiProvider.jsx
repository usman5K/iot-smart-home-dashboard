import React, { createContext, useContext } from 'react';

const ApiContext = createContext();

const API_BASE_URL = 'http://localhost:8010/api/v1'; // Your FastAPI backend URL

export const ApiProvider = ({ children }) => {
  const apiCall = async (url, method = 'GET', data = null, auth = false) => {

    const token = auth ? localStorage.getItem('token') : null;

    const headers = {
      'Content-Type': 'application/json',
    };
    if (auth && token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const options = {
      method,
      headers,
    };
    if (data) {
      options.body = JSON.stringify(data);
    }

    try {
      const response = await fetch(`${API_BASE_URL}${url}`, options);
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API fetch error:', error);
      throw error;
    }
  };

  return (
    <ApiContext.Provider value={apiCall}>
      {children}
    </ApiContext.Provider>
  );
};

export const useApi = () => {
  return useContext(ApiContext);
};
