import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';

const PeliculaUpdateForm = ({ peliculas, updatePelicula }) => {
    const { id } = useParams();
    const history = useHistory();
    const [pelicula, setPelicula] = useState({
        nombre: '',
        genero: '',
        duracion: '',
        inventario: ''
    });

    useEffect(() => {
        const peliculaActual = peliculas.find(p => p.id.toString() === id);
        if (peliculaActual) {
            setPelicula(peliculaActual);
        }
    }, [id, peliculas]);

    const handleChange = (e) => {
        setPelicula({ ...pelicula, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        updatePelicula(id, pelicula);
        history.push('/peliculas');
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Editar Película</h2>
            <div>
                <label>Nombre:</label>
                <input type="text" name="nombre" value={pelicula.nombre} onChange={handleChange} required />
            </div>
            <div>
                <label>Género:</label>
                <input type="text" name="genero" value={pelicula.genero} onChange={handleChange} required />
            </div>
            <div>
                <label>Duración (minutos):</label>
                <input type="number" name="duracion" value={pelicula.duracion} onChange={handleChange} required />
            </div>
            <div>
                <label>Inventario:</label>
                <input type="number" name="inventario" value={pelicula.inventario} onChange={handleChange} required />
            </div>
            <button type="submit">Actualizar Película</button>
        </form>
    );
};

export default PeliculaUpdateForm;
