import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import './styles/Pelicula.css';

function PeliculaForm({ onSave }) {
    const [pelicula, setPelicula] = useState({
        nombre: '',
        genero: '',
        duracion: '',
        inventario: ''
    });

    const history = useHistory();
    const handleChange = (e) => {
        setPelicula({ ...pelicula, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!pelicula.nombre || !pelicula.genero || !pelicula.duracion || !pelicula.inventario) {
            alert('Por favor, completa todos los campos');
            return;
        }
        onSave(pelicula);
        setPelicula({ nombre: '', genero: '', duracion: '', inventario: '' });
        history.push('/peliculas');
    };

    return (
        <form onSubmit={handleSubmit} className="pelicula-form">
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
            <button type="submit">Guardar Película</button>
        </form>
    );
}

export default PeliculaForm;
