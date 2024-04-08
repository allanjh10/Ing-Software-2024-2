import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const UsuarioForm = ({ onSave }) => {
    const [usuario, setUsuario] = useState({
        nombre: '',
        email: '',
        rol: ''
    });

    const history = useHistory();


    const handleChange = (e) => {
        setUsuario({ ...usuario, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSave(usuario);
        history.push('/usuarios');
    };

    return (
        <div className="form-container">
            <h2>Agregar Usuario</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Nombre:</label>
                    <input type="text" name="nombre" value={usuario.nombre} onChange={handleChange} required />
                </div>
                <div className="form-group">
                    <label>Email:</label>
                    <input type="email" name="email" value={usuario.email} onChange={handleChange} required />
                </div>
                <div className="form-group">
                    <label>Rol:</label>
                    <input type="text" name="rol" value={usuario.rol} onChange={handleChange} required />
                </div>
                <button type="submit" className="btn">Guardar Usuario</button>
            </form>
        </div>
    );
}

export default UsuarioForm;
