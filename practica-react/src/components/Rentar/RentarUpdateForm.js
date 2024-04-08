import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';

const RentarUpdateForm = ({ rentas, updateRenta }) => {
    const { id } = useParams();
    const history = useHistory();
    const [renta, setRenta] = useState({
        idUsuario: '',
        idPelicula: '',
        fecha_renta: '',
        dias_de_renta: 5,
        estatus: 'activo'
    });

    useEffect(() => {
        const rentaExistente = rentas.find(r => r.idRentar === parseInt(id));
        if (rentaExistente) {
            setRenta(rentaExistente);
        }
    }, [id, rentas]);

    const handleChange = (e) => {
        setRenta({ ...renta, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        updateRenta(id, renta);
        history.push('/rentar');
    };

    return (
        <form onSubmit={handleSubmit} className="update-form">
            <h2>Editar Renta</h2>
            <div className="form-group">
                <label htmlFor="idUsuario">ID Usuario:</label>
                <input
                    type="text"
                    id="idUsuario"
                    name="idUsuario"
                    value={renta.idUsuario}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="idPelicula">ID Película:</label>
                <input
                    type="text"
                    id="idPelicula"
                    name="idPelicula"
                    value={renta.idPelicula}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="fecha_renta">Fecha de Renta:</label>
                <input
                    type="date"
                    id="fecha_renta"
                    name="fecha_renta"
                    value={renta.fecha_renta}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="dias_de_renta">Días de Renta:</label>
                <input
                    type="number"
                    id="dias_de_renta"
                    name="dias_de_renta"
                    value={renta.dias_de_renta}
                    onChange={handleChange}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="estatus">Estatus:</label>
                <select
                    id="estatus"
                    name="estatus"
                    value={renta.estatus}
                    onChange={handleChange}
                    required
                >
                    <option value="activo">Activo</option>
                    <option value="devuelto">Devuelto</option>
                </select>
            </div>
            <button type="submit" className="btn">Actualizar Renta</button>
        </form>
    );
};

export default RentarUpdateForm;
