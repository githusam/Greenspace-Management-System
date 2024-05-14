import React from "react";
import axiosinstance from '../composable/baseURL';
import { Link } from "react-router-dom";

const Garden = ({ garden, setGarden }) => {
  const removeFromGarden = async (id) => {
    try {
      await axiosinstance.delete(
        `/plants/remove_from_garden/${id}`
      );
      const updatedGarden = garden.filter((plant) => plant.id !== id);
      setGarden(updatedGarden);
    } catch (error) {
      console.error("Error removing plant from garden:", error);
    }
  };

  return (
    <div>
      <h3 className="text-xl font-semibold text-gray-900 mb-4">Your Garden</h3>
      <div className="shadow-lg rounded-lg overflow-x-auto">
        <table className="min-w-full bg-white">
          <thead className="bg-gray-800 text-white">
            <tr>
              <th className="text-left py-3 px-4 uppercase font-semibold text-sm">
                ID
              </th>
              <th className="text-left py-3 px-4 uppercase font-semibold text-sm">
                Plant Name
              </th>

              <th className="text-left py-3 px-4 uppercase font-semibold text-sm">
                Actions
              </th>
            </tr>
          </thead>
          <tbody className="text-gray-700">
            {garden.map((plant) => (
              <tr key={plant.id}>
                <td className="text-left py-3 px-4">{plant.id}</td>
                <td className="text-left py-3 px-4">{plant.name}</td>

                <td className="text-left py-3 px-4">
                  <Link
                    to={`/schedule/${plant.id}`}
                    className="text-blue-500 hover:underline mr-7"
                  >
                    View Schedule
                  </Link>
                  <button
                    onClick={() => removeFromGarden(plant.id)} // Update this line
                    className="text-red-500 hover:text-red-700"
                  >
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Garden;
