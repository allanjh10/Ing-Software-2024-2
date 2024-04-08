import React from 'react';
import { Link } from 'react-router-dom';

const UsuarioList = ({ usuarios, onDelete }) => {
    return (
        <div className="usuario-list">
            {usuarios.map(usuario => (
                <div className="usuario-item" key={usuario.id}>
                    <h3>{usuario.nombre}</h3>
                    <p>Email: {usuario.email}</p>
                    <p>Rol: {usuario.rol}</p>
                    <div className="action-buttons">
                        <Link to={`/usuarios/editar/${usuario.id}`} className="action-button edit">Editar</Link>
                        <button onClick={() => onDelete(usuario.id)} className="action-button delete">Eliminar</button>
                    </div>
                </div>
            ))}
        </div>
    );
}

export default UsuarioList;
