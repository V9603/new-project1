import React, { useEffect, useState } from "react";
import { getDashboardStats, getDashboardCharts } from "../services/api";
import { Pie } from "react-chartjs-2";

const Dashboard = () => {
  const [stats, setStats] = useState({});
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    async function fetchData() {
      const statsData = await getDashboardStats();
      setStats(statsData);

      const chartRes = await getDashboardCharts();
      setChartData({
        labels: Object.keys(chartRes.status_distribution),
        datasets: [
          {
            data: Object.values(chartRes.status_distribution),
            backgroundColor: ["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0"],
          },
        ],
      });
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2>School Dashboard</h2>
      <div>
        <p>Total Students: {stats.total_students}</p>
        <p>Active Students: {stats.active_students}</p>
        <p>Alumni Students: {stats.alumni_students}</p>
        <p>Withdrawn Students: {stats.withdrawn_students}</p>
      </div>
      <div style={{ width: "400px", marginTop: "20px" }}>
        <Pie data={chartData} />
      </div>
    </div>
  );
};

export default Dashboard;
