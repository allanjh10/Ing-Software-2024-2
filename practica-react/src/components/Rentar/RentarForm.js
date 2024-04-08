import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const RentarForm = ({ onSave }) => {
    const [renta, setRenta] = useState({
        idUsuario: '',
        idPelicula: '',
        fecha_renta: '',
        dias_de_renta: 5,
        estatus: 'activo'
    });
    const history = useHistory();

    const handleChange = (e) => {
        setRenta({ ...renta, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSave(renta);
        history.push('/rentar');
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Usuario ID:</label>
            <input type="text" name="idUsuario" value={renta.idUsuario} onChange={handleChange} required />
            <label>Película ID:</label>
            <input type="text" name="idPelicula" value={renta.idPelicula} onChange={handleChange} required />
            <label>Fecha de Renta:</label>
            <input type="date" name="fecha_renta" value={renta.fecha_renta} onChange={handleChange} required />
            <button type="submit">Agregar Renta</button>
        </form>
    );
};

export default RentarForm;
