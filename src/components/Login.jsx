import React, { useState, useEffect } from 'react';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [csrfToken, setCsrfToken] = useState('');

    useEffect(() => {
        // Función para obtener el token CSRF desde el backend de Django
        const getCsrfToken = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/login/csrf/', {
                    method: 'GET',
                    credentials: 'include'
                });
                const data = await response.json();
                setCsrfToken(data.csrfToken);
            } catch (error) {
                console.error('Error al obtener el token CSRF:', error);
            }
        };

        getCsrfToken();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:8000/login/login_user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ username, password }),
            credentials: 'include'
        });

        if (response.ok) {
            // Redirigir a la página de inicio del usuario después del login exitoso
            window.location.href = 'http://127.0.0.1:8000/listadoCancha/'; // Cambia '/dashboard' por la ruta deseada
        } else {
            alert('Error en inicio de sesión. Por favor, inténtalo de nuevo.');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </label>
                <br />
                <label>
                    Password:
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>
                <br />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;
