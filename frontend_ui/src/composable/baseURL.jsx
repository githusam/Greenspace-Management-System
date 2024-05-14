import axios from 'axios';

const axiosinstance = axios.create({
  //baseURL: 'https://gmsbackend.azurewebsites.net/'
  baseURL: 'http://127.0.0.1:8000/api/v1'
});

export default axiosinstance;