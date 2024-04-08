import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';

const UsuarioUpdateForm = ({ usuarios, updateUsuario }) => {
    const { id } = useParams();
    const history = useHistory();
    const [usuario, setUsuario] = useState({ nombre: '', email: '', rol: '' });

    useEffect(() => {
        const usuarioActual = usuarios.find(u => u.id === parseInt(id));
        setUsuario(usuarioActual || {});
    }, [id, usuarios]);

    const handleChange = e => {
        setUsuario({ ...usuario, [e.target.name]: e.target.value });
    };

    const handleSubmit = e => {
        e.preventDefault();
        updateUsuario(id, usuario);
        history.push('/usuarios');
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <label>Nombre:
                <input type="text" name="nombre" value={usuario.nombre} onChange={handleChange} required />
            </label>
            <label>Email:
                <input type="email" name="email" value={usuario.email} onChange={handleChange} required />
            </label>
            <label>Rol:
                <input type="text" name="rol" value={usuario.rol} onChange={handleChange} required />
            </label>
            <button type="submit">Actualizar Usuario</button>
        </form>
    );
}

export default UsuarioUpdateForm;
