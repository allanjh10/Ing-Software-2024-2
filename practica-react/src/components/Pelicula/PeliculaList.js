import React from 'react';
import { Link } from 'react-router-dom';

const PeliculaList = ({ peliculas, onDelete }) => {
    return (
        <div className="pelicula-list">
            {peliculas.map(pelicula => (
                <div className="pelicula-item" key={pelicula.id}>
                    <h3>{pelicula.nombre}</h3>
                    <p>Género: {pelicula.genero}</p>
                    <p>Duración: {pelicula.duracion} minutos</p>
                    <p>Inventario: {pelicula.inventario}</p>
                    <div className="action-buttons">
                        <Link to={`/peliculas/editar/${pelicula.id}`} className="action-button edit">Editar</Link>
                        <button onClick={() => onDelete(pelicula.id)} className="action-button delete">Eliminar</button>
                    </div>
                </div>
            ))}
        </div>
    );
}

export default PeliculaList;
