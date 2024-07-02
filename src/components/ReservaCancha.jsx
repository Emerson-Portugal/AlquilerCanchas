import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ReservaCancha = () => {
    const [canchas, setCanchas] = useState([]);
    const [horarios, setHorarios] = useState([]);
    const [formData, setFormData] = useState({
        duracion: '',
        pago: '',
        idAccProducto: '',
        idHorario: '',
        idCancha: ''
    });

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/alquiler/listado/canchas/')
            .then(res => {
                console.log('Canchas:', res.data);
                if (Array.isArray(res.data)) {
                    setCanchas(res.data);
                } else {
                    console.error('La respuesta de canchas no es un array:', res.data);
                }
            })
            .catch(err => console.error('Error al obtener canchas:', err));

        axios.get('http://127.0.0.1:8000/api/alquiler/listado/horarios/')
            .then(res => {
                console.log('Horarios:', res.data);
                if (Array.isArray(res.data)) {
                    setHorarios(res.data);
                } else {
                    console.error('La respuesta de horarios no es un array:', res.data);
                }
            })
            .catch(err => console.error('Error al obtener horarios:', err));
    }, []);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const reservaData = {
            duracion: formData.duracion,
            pago: formData.pago,
            idAccProducto: formData.idAccProducto,
            idHorario: formData.idHorario
        };
        axios.post('http://127.0.0.1:8000/api/alquiler/listado/reservas/', reservaData)
            .then(res => {
                const detalleData = {
                    idReservaCancha: res.data.id,
                    idCancha: formData.idCancha
                };
                return axios.post('http://127.0.0.1:8000/api/alquiler/listado/detalles/', detalleData);
            })
            .then(res => {
                console.log('Reserva realizada con éxito');
            })
            .catch(err => console.error('Error al realizar la reserva:', err));
    };

    return (
        <div>
            <h1>Reservar Cancha</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Duración:</label>
                    <input type="number" name="duracion" value={formData.duracion} onChange={handleChange} />
                </div>
                <div>
                    <label>Pago:</label>
                    <input type="number" name="pago" value={formData.pago} onChange={handleChange} />
                </div>
                <div>
                    <label>Accesorio Producto:</label>
                    <select name="idAccProducto" value={formData.idAccProducto} onChange={handleChange}>
                        <option value="">Seleccione</option>
                        {/* Asumiendo que tienes un endpoint para obtener los productos */}
                    </select>
                </div>
                <div>
                    <label>Horario:</label>
                    <select name="idHorario" value={formData.idHorario} onChange={handleChange}>
                        <option value="">Seleccione</option>
                        {Array.isArray(horarios) && horarios.map(horario => (
                            <option key={horario.idHorario} value={horario.idHorario}>{`${horario.horaInicio} - ${horario.horaFin}`}</option>
                        ))}
                    </select>
                </div>
                <div>
                    <label>Cancha:</label>
                    <select name="idCancha" value={formData.idCancha} onChange={handleChange}>
                        <option value="">Seleccione</option>
                        {Array.isArray(canchas) && canchas.map(cancha => (
                            <option key={cancha.idCancha} value={cancha.idCancha}>{cancha.nomCancha}</option>
                        ))}
                    </select>
                </div>
                <button type="submit">Reservar</button>
            </form>
        </div>
    );
};

export default ReservaCancha;
