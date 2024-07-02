import { useEffect, useState } from "react";
import { getAllCanchas } from "../api/alquiler.api";

export function GalleryList() {
  const [canchas, setCanchas] = useState([]);

  useEffect(() => {
    getAllCanchas()
      .then(response => {
        setCanchas(response.data.results); // Extraer el arreglo de `results`
      })
      .catch(error => {
        console.error('Error fetching canchas:', error);
      });
  }, []);

  const handleReserve = (canchaId) => {
    // Aquí puedes implementar la lógica para la reserva, por ejemplo, hacer una solicitud POST al backend
    console.log(`Cancha reservada con ID: ${canchaId}`);
  };

  return (
    <div className="gallery">
      {canchas.map((cancha) => (
        <div key={cancha.idCancha} className="gallery-item">
          <img src={cancha.imagen} alt={cancha.nomCancha} />
          <h2>{cancha.nomCancha}</h2>
          <p>{cancha.descripcion}</p>
          <p>Precio: ${cancha.precio}</p>
          <button onClick={() => handleReserve(cancha.idCancha)}>Reservar</button>
        </div>
      ))}
    </div>
  );
}
