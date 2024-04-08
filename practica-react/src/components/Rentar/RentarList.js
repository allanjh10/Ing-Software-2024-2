import React from 'react';
import { Link } from 'react-router-dom';

const RentarList = ({ rentas }) => {
    return (
        <div>
            <h2>Listado de Rentas</h2>
            {rentas.map(renta => (
                <div key={renta.idRentar} className="renta-item">
                    <p>Renta #{renta.idRentar}: Película ID: {renta.idPelicula}, Usuario ID: {renta.idUsuario}, Rentada el: {renta.fecha_renta}, Días: {renta.dias_de_renta}, Estado: {renta.estatus}</p>
                    <Link to={`/rentar/editar/${renta.idRentar}`}>Editar</Link>
                </div>
            ))}
            <div className="add-renta-button">
                <Link to="/rentar/agregar" className="action-button">Agregar Renta</Link>
            </div>
        </div>
    );
};

export default RentarList;
