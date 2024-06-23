import axios from "axios";

const URL = "http://localhost:8000";

console.log(URL);
const alquilerApi = axios.create({
  baseURL: `${URL}/api/alquiler/listado/canchas`,
});

export const getAllCanchas = () => alquilerApi.get("/");