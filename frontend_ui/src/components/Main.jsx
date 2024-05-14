import React, { useState, useEffect } from "react";
import Search from "./Search";
import axiosinstance from '../composable/baseURL';
import Garden from "./Garden";

export function Main() {
  const [garden, setGarden] = useState([]);

  useEffect(() => {
    const fetchGardenData = async () => {
      try {
        const response = await axiosinstance.get(
          "/plants/get_plants_in_garden"
        );
        setGarden(response.data);
      } catch (error) {
        console.error("Error fetching garden data:", error);
      }
    };
    fetchGardenData();
  }, []);


  const onAddToGarden = async (plantId) => {
    try {
      const response = await axiosinstance.post(
        `/plants/add_to_garden/${plantId}`
      );
      if (response.status === 200) {
        setGarden([...garden, response.data]);
      }
    } catch (error) {
      console.error("Error adding plant to garden:", error);
    }
  };


  return (
    <div className="w-full min-h-screen bg-slate-400">
      <header className="text-white body-font border-b bg-slate-900 border-black">
        <div className="container mx-auto w-fullflex flex-wrap p-5 flex-col md:flex-row items-center">
          <a className="flex title-font font-medium items-center text-white mb-4 md:mb-0">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              className="w-10 h-10 text-white p-2 bg-green-500 rounded-full"
              viewBox="0 0 24 24"
            >
              <path d="M12 2L2 7l10 5 10-5-10-5zm0 13l-10 5 10 5 10-5-10-5z"></path>
            </svg>
            <span className="ml-3 text-xl">Greenspace Management System</span>
          </a>
        </div>
      </header>
      <main className="container mx-auto px-4 flex-grow">
        <div className="mb-8">
        <Search onAddToGarden={onAddToGarden} />
        </div>

        <div className="flex flex-wrap md:flex-nowrap">
          <div className="w-full md:max-w-4xl md:mx-auto">
            <Garden garden={garden} setGarden={setGarden} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default Main;
