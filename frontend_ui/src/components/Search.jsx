import React, { useState } from "react";
import axios from "axios";
import { Link } from 'react-router-dom';

const Search = ({onAddToGarden}) => {
  const [query, setQuery] = useState("");
  const [plants, setPlants] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/plants/search`,
        { params: { query } }
      );
      setPlants(response.data); 
      setIsLoading(false);
    } catch (error) {
      console.error("Error fetching search results:", error);
      setIsLoading(false);
    }
  };

  const resetSearch = () => {
    setQuery("");    // Reset the search query
    setPlants([]);   // Clear the search results
    setIsLoading(false);
  };

  const handleAddToGarden = async (plantId) => {
    await onAddToGarden(plantId);
    resetSearch(); // Resets the search after adding to garden
  };

  return (
<div className="p-4">
  <div className="mb-4">
    <form onSubmit={handleSearch} className="flex w-full">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search for plants..."
        className="flex-grow p-2 border-2 border-gray-200 rounded focus:outline-none focus:border-blue-500 transition duration-150 ease-in-out"
      />
      <button
        type="submit"
        className={`ml-2 bg-blue-500 text-white p-2 rounded hover:bg-blue-600 focus:outline-none transition duration-150 ease-in-out ${
          isLoading ? "opacity-50 cursor-not-allowed" : ""
        }`}
        disabled={isLoading}
      >
        {isLoading ? "Searching..." : "Search"}
      </button>
    </form>
  </div>

  {/* Results container with responsive design */}
  <div className="flex flex-wrap">
    {plants.map((plant) => (
      <div key={plant.id} className="p-4 w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
        <div className="border-2 bg-white border-gray-200 rounded-lg p-4 hover:shadow-md transition duration-150 ease-in-out">
          <h3 className="font-bold">{plant.common_name}</h3>
          <button
                onClick={() => handleAddToGarden(plant.id)}
                className="mt-2 bg-green-500 text-white p-2 rounded hover:bg-green-600 focus:outline-none transition duration-150 ease-in-out;
                "
              >
                Add to Garden
              </button>
        </div>
      </div>
    ))}
  </div>
</div>

  );
};

export default Search;
