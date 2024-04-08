import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';

function PeliculaUpdateForm({ getPeliculaById, updatePelicula }) {
    const { id } = useParams();
    const history = useHistory();
    const [pelicula, setPelicula] = useState({ nombre: '', genero: '', duracion: '', inventario: '' });

    useEffect(() => {
        const pelicula = getPeliculaById(id);
        if (pelicula) {
            setPelicula(pelicula);
        } else {
            // Handle error or redirect
            history.push('/listar');
        }
    }, [id, getPeliculaById, history]);

    const handleChange = (e) => {
        setPelicula({ ...pelicula, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        updatePelicula(id, pelicula);
        history.push('/listar');
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Nombre:
                <input type="text" name="nombre" value={pelicula.nombre} onChange={handleChange} required />
            </label>
            <label>Género:
                <input type="text" name="genero" value={pelicula.genero} onChange={handleChange} required />
            </label>
            <label>Duración (minutos):
                <input type="number" name="duracion" value={pelicula.duracion} onChange={handleChange} required />
            </label>
            <label>Inventario:
                <input type="number" name="inventario" value={pelicula.inventario} onChange={handleChange} required />
            </label>
            <button type="submit">Actualizar Película</button>
        </form>
    );
}

export default PeliculaUpdateForm;
