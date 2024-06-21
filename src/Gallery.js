import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Gallery.css';

const Gallery = () => {
    const [canchas, setCanchas] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/canchas/')
            .then(response => {
                setCanchas(response.data);
            })
            .catch(error => {
                console.error('Error fetching the canchas!', error);
            });
    }, []);

    return (
        <div className="gallery">
            {canchas.map((cancha) => (
                <div key={cancha.idCancha} className="gallery-item">
                    <img src={cancha.imagen} alt={cancha.nomCancha} />
                    <h2>{cancha.nomCancha}</h2>
                    <p>{cancha.descripcion}</p>
                    <p>Precio: ${cancha.precio}</p>
                </div>
            ))}
        </div>
    );
}

export default Gallery;
