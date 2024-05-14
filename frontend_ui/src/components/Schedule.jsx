import React, { useEffect, useState } from 'react';
import '../assets/css/index.css';
import { useParams } from 'react-router-dom';
import axiosinstance from '../composable/baseURL';
import { BsCalendar2Day } from "react-icons/bs";

const Schedule = () => {
  let { plantId } = useParams();
  const [schedule, setSchedule] = useState([]);
  
  useEffect(() => {
    const fetchSchedule = async () => {
      try {
        const daysOfWeek = ['Day of the week', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const response = await axiosinstance.get(`/plants/plantwatering_schedule/${plantId}`);
        const { data } = response;
        console.log(data);
        const scheduleData = daysOfWeek.map((day, index) => {
          if (index === 0) {
            return { day, dayToWater : ['Water this day?'], periods: ['Time of day to water plant'] }; 
          } else {
            return { day, dayToWater: [data.dayToWater[index - 1]], periods: [data.periods[index - 1]] }; 
          }
        });
        setSchedule(scheduleData);
      } catch (error) {
        console.error('Error fetching schedule:', error);
      }
    };
    fetchSchedule();
  }, [plantId]);


  return (
    <div className='bg-slate-400 h-screen '>
      <div className='bg-slate-800 pb-2 pt-7 text-center'>
       <h2 className="inline-block text-center text-5xl font-mono text-slate-50">Weekly Schedule 
       </h2>
       <BsCalendar2Day style={
        {color : "white",
        bottom: '15px',
        position: "relative",
        fontSize: '3.5em',
        marginLeft: '20px',
        display: 'inline-block'
        }}/>
      </div>
      <div className="flex flex-col items-center py-10">
        {schedule.map((daySchedule, index) => (
          //table
          <div class="table" className={`${index === 0 ? "flex w-128 bg-slate-800 rounded-tl-lg rounded-tr-lg border-black font-sans" 
          : (index === schedule.length-1 ? "flex w-128 rounded-bl-lg rounded-br-lg bg-white border-black font-sans" 
            : "flex w-128 bg-white font-sans")}`} key={daySchedule}> 
            <div className={`${index===0 ? 'rounded-tl-lg  text-xl w-64 px-2 py-4 text-left  border-black text-white' 
            : (index === schedule.length -1 ? ' rounded-bl-lg  w-64 px-2 py-4 text-left border-black' 
              : 'border-b-2 w-64 px-2 py-4 text-left ')}`}>
              <strong className='font-mono'>{daySchedule.day}</strong>
            </div>
            
            <div className={`${index === 0 ? 'rounded-tr-lg  font-bold text-xl w-64 px-2 py-4 text-left   text-white' 
            : (index === schedule.length - 1 ? 'rounded-br-lg text-lg w-64 px-2 py-4 text-left' 
              : ' border-b-2 text-lg  w-64 px-2 py-4 text-left ')} font-mono`}>
                {(index === 0 ? 'Water this day?' : (daySchedule.dayToWater[0] === 1 ? "Yes" : "No"))}
            </div>

            <div className={`${index === 0 ? 'rounded-tr-lg  font-bold text-xl w-64 px-2 py-4 text-left   text-white' 
            : (index === schedule.length - 1 ? 'rounded-br-lg text-lg w-64 px-2 py-4 text-left' 
              : ' border-b-2 text-lg  w-64 px-2 py-4 text-left ')} font-mono`}>
              {daySchedule.periods}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Schedule;
