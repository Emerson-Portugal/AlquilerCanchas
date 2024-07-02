import axios from "axios";

const URL = "http://localhost:8000";

console.log(URL);
const alquilerApi = axios.create({
  baseURL: `${URL}/api/alquiler/listado/`,
});

export const getAllCanchas = () => alquilerApi.get("canchas/");

export const createReserva = (reservaData) => alquilerApi.post("reservas/", reservaData);
