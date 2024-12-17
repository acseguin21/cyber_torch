import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { Button, Container, Typography, Box, Paper, TextField } from '@mui/material';
import Register from './Register';
import './index.css';

function App() {
    const [isRegistering, setIsRegistering] = useState(false);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleLogin = async () => {
        try {
            const response = await fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();
            if (response.ok) {
                localStorage.setItem('token', data.access_token);
                setMessage('Login successful!');
            } else {
                setMessage(data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            setMessage('Error connecting to server');
        }
    };

    return (
        <Container maxWidth="xs">
            <Paper elevation={3} style={{ padding: '20px', marginTop: '50px' }}>
                <Typography variant="h4" component="h1" gutterBottom>
                    CSPM App
                </Typography>
                {isRegistering ? (
                    <Register />
                ) : (
                    <Box>
                        <TextField
                            label="Username"
                            variant="outlined"
                            fullWidth
                            margin="normal"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                        <TextField
                            label="Password"
                            type="password"
                            variant="outlined"
                            fullWidth
                            margin="normal"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <Button variant="contained" color="primary" fullWidth onClick={handleLogin}>
                            Login
                        </Button>
                        <Button variant="outlined" color="secondary" fullWidth onClick={() => setIsRegistering(true)} style={{ marginTop: '10px' }}>
                            Register
                        </Button>
                    </Box>
                )}
                <Typography variant="body2" color="textSecondary" align="center" style={{ marginTop: '10px' }}>
                    {message}
                </Typography>
            </Paper>
        </Container>
    );
}

ReactDOM.render(<App />, document.getElementById('root')); 