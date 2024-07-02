import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';


function ReservaDetail() {
  const { id } = useParams();
  const [reserva, setReserva] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/alquiler/listado/reservas/${id}/`)
      .then(response => {
        setReserva(response.data);
      })
      .catch(error => {
        console.error('Error fetching reserva details:', error);
      });
  }, [id]);

  if (!reserva) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Detalles de la Reserva</h1>
      <p>ID Reserva: {reserva.idReservaCancha}</p>
      <p>Duración: {reserva.duracion} horas</p>
      <p>Estado: {reserva.estado ? 'Activo' : 'Inactivo'}</p>
      <p>Pago: ${reserva.pago}</p>
      <p>Horario ID: {reserva.idHorario}</p>
      <p>Accesorio Producto ID: {reserva.idAccProducto}</p>
      {/* Agrega más detalles según sea necesario */}
    </div>
  );
}

export default ReservaDetail;
