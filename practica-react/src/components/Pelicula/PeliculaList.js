import React from 'react';
import './styles/Pelicula.css';

function PeliculaList({ peliculas, onDelete }) {
    return (
        <div className="pelicula-list">
            <h2>Listado de Películas</h2>
            {peliculas.map(pelicula => (
                <div key={pelicula.id} className="pelicula-item">
                    <h3>{pelicula.nombre}</h3>
                    <p>Género: {pelicula.genero}</p>
                    <p>Duración: {pelicula.duracion} minutos</p>
                    <p>Inventario: {pelicula.inventario}</p>
                    <button onClick={() => onDelete(pelicula.id)}>Eliminar</button>
                </div>
            ))}
        </div>
    );
}

export default PeliculaList;
