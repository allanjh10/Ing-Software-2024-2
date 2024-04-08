import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import PeliculaList from './components/Pelicula/PeliculaList';
import PeliculaForm from './components/Pelicula/PeliculaForm';
import PeliculaUpdateForm from './components/Pelicula/PeliculaUpdateForm';
import './App.css'; // Asegúrate de que este archivo contiene los estilos que hemos definido

function App() {
    const [peliculas, setPeliculas] = useState([
        { id: 1, nombre: 'Interstellar', genero: 'Ciencia Ficción', duracion: 169, inventario: 10 },
        { id: 2, nombre: 'Inception', genero: 'Thriller', duracion: 148, inventario: 15 },
        { id: 3, nombre: 'The Dark Knight', genero: 'Acción', duracion: 152, inventario: 20 },
        { id: 4, nombre: 'Avatar', genero: 'Aventura', duracion: 162, inventario: 8 },
        { id: 5, nombre: 'The Matrix', genero: 'Ciencia Ficción', duracion: 136, inventario: 12 }
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

    return (
        <Router>
            <div className="App">
                <header>
                    <nav>
                        <ul className="main-nav">
                            <li><Link to="/">Inicio</Link></li>
                            <li><Link to="/peliculas">Listar Películas</Link></li>
                            <li><Link to="/peliculas/agregar">Agregar Película</Link></li>
                        </ul>
                    </nav>
                </header>
                <main>
                    <Switch>
                        <Route path="/peliculas/agregar">
                            <PeliculaForm onSave={addPelicula} />
                        </Route>
                        <Route path="/peliculas/editar/:id">
                            <PeliculaUpdateForm getPeliculaById={(id) => peliculas.find(p => p.id === parseInt(id))} updatePelicula={updatePelicula} />
                        </Route>
                        <Route path="/peliculas">
                            <PeliculaList peliculas={peliculas} onDelete={deletePelicula} />
                        </Route>
                        <Route path="/" exact>
                            <h1>Bienvenido a la Administración de Películas</h1>
                        </Route>
                    </Switch>
                </main>
            </div>
        </Router>
    );
}

export default App;
