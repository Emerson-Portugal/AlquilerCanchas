import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const URL = "http://localhost:8000";

const alquilerApi = axios.create({
  baseURL: `${URL}/api/alquiler/listado`,
});

export const createReserva = (reservaData) => alquilerApi.post("/reservas/", reservaData);

export function GalleryList() {
  const [canchas, setCanchas] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`${URL}/api/alquiler/listado/canchas/`)
      .then(response => {
        setCanchas(response.data.results);
      })
      .catch(error => {
        console.error('Error fetching canchas:', error);
      });
  }, []);

  const handleReserve = (cancha) => {
    const reservaData = {
      duracion: 1.0, // Ejemplo de duración en horas
      estado: true,
      pago: cancha.precio,
      idAccProducto: 1, // ID de un accesorio producto existente
      idHorario: 1 // ID de un horario existente
    };

    createReserva(reservaData)
      .then(response => {
        console.log('Reserva creada:', response.data);
        navigate(`/reserva/${response.data.idReservaCancha}`);
      })
      .catch(error => {
        console.error('Error creating reserva:', error.response?.data || error.message);
      });
  };

  return (
    <div className="gallery">
      {canchas.map((cancha) => (
        <div key={cancha.idCancha} className="gallery-item">
          <img src={cancha.imagen} alt={cancha.nomCancha} />
          <h2>{cancha.nomCancha}</h2>
          <p>{cancha.descripcion}</p>
          <p>Precio: ${cancha.precio}</p>
          <button onClick={() => handleReserve(cancha)}>Reservar</button>
        </div>
      ))}
    </div>
  );
}
