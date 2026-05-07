import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // FastAPI backend

export const getDashboardStats = async () => {
  const res = await axios.get(`${API_URL}/dashboard/stats`);
  return res.data;
};

export const getDashboardCharts = async () => {
  const res = await axios.get(`${API_URL}/dashboard/charts`);
  return res.data;
};

export const getAttendanceSummary = async (studentId) => {
  const res = await axios.get(`${API_URL}/student/${studentId}/attendance_summary`);
  return res.data;
};

export const getFeesSummary = async (studentId) => {
  const res = await axios.get(`${API_URL}/student/${studentId}/fees_summary`);
  return res.data;
};
