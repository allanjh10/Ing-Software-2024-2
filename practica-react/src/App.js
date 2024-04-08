import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import PeliculaList from './components/Pelicula/PeliculaList';
import PeliculaForm from './components/Pelicula/PeliculaForm';
import PeliculaUpdateForm from './components/Pelicula/PeliculaUpdateForm';
import UsuarioList from './components/Usuario/UsuarioList';
import UsuarioForm from './components/Usuario/UsuarioForm';
import UsuarioUpdateForm from './components/Usuario/UsuarioUpdateForm';
import './App.css';

ReactDOM.render(
  <Router>
      <App />
  </Router>,
  document.getElementById('root')
);


function App() {
    const [peliculas, setPeliculas] = useState([
        { id: 1, nombre: 'Interstellar', genero: 'Ciencia Ficción', duracion: 169, inventario: 10 },
        { id: 2, nombre: 'Inception', genero: 'Thriller', duracion: 148, inventario: 15 },
        { id: 3, nombre: 'The Dark Knight', genero: 'Acción', duracion: 152, inventario: 20 },
        { id: 4, nombre: 'Avatar', genero: 'Aventura', duracion: 162, inventario: 8 },
        { id: 5, nombre: 'The Matrix', genero: 'Ciencia Ficción', duracion: 136, inventario: 12 }
    ]);

    const [usuarios, setUsuarios] = useState([
      { id: 1, nombre: 'John Doe', email: 'john.doe@example.com', rol: 'Administrador' },
      { id: 2, nombre: 'Jane Smith', email: 'jane.smith@example.com', rol: 'Usuario' },
      { id: 3, nombre: 'Allan Williams', email: 'allan@example.com', rol: 'Usuario' },
      { id: 4, nombre: 'Arya Kelce', email: 'kelcearya14@example.com', rol: 'Usuario' },
      { id: 5, nombre: 'Iris West', email: 'iris.west@example.com', rol: 'Usuario' }

  ]);

    const addPelicula = pelicula => {
        pelicula.id = peliculas.length + 1; // Asegura un ID único
        setPeliculas([...peliculas, pelicula]);
        
    };

    const updatePelicula = (id, updatedPelicula) => {
        setPeliculas(peliculas.map(pelicula => pelicula.id === parseInt(id) ? { ...updatedPelicula, id: parseInt(id) } : pelicula));
    };

    const deletePelicula = id => {
        setPeliculas(peliculas.filter(pelicula => pelicula.id !== parseInt(id)));
    };

    const addUsuario = usuario => {
        usuario.id = usuarios.length + 1;
        setUsuarios([...usuarios, usuario]);
    };

    const updateUsuario = (id, usuarioActualizado) => {
        const updatedItems = usuarios.map(item => item.id === parseInt(id) ? { ...usuarioActualizado, id: parseInt(id) } : item);
        setUsuarios(updatedItems);
    };

    const deleteUsuario = id => {
        setUsuarios(usuarios.filter(usuario => usuario.id !== parseInt(id)));
    };


    return (
      <Router>
          <div className="App">
              <header>
                  <nav>
                      <ul className="main-nav">
                          <li><Link to="/">Inicio</Link></li>
                          <li><Link to="/peliculas">Peliculas</Link></li>
                          <li><Link to="/usuarios">Usuarios</Link></li>
                      </ul>
                  </nav>
              </header>
              <main>
                  <Switch>
                      <Route path="/peliculas/agregar" render={(props) => <PeliculaForm onSave={addPelicula} {...props} />} />
                      <Route path="/peliculas/editar/:id" component={() => <PeliculaUpdateForm peliculas={peliculas} updatePelicula={updatePelicula} />} />
                      <Route path="/peliculas" exact>
                          <PeliculaList peliculas={peliculas} onDelete={deletePelicula} />
                          <Link to="/peliculas/agregar" className="action-button">Agregar Película</Link>
                      </Route>
                      <Route path="/usuarios/agregar" render={(props) => <UsuarioForm onSave={addUsuario} {...props} />} />
                      <Route path="/usuarios/editar/:id" component={() => <UsuarioUpdateForm usuarios={usuarios} updateUsuario={updateUsuario} />} />
                      <Route path="/usuarios" exact>
                          <UsuarioList usuarios={usuarios} onDelete={deleteUsuario} />
                          <Link to="/usuarios/agregar" className="action-button">Agregar Usuario</Link>
                      </Route>
                      <Route path="/" exact>
                          <h1>Bienvenido a la Administración de Películas y Usuarios</h1>
                      </Route>
                  </Switch>
              </main>
          </div>
      </Router>
  );
}


export default App;
