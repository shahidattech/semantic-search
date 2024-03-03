import React, { useState } from 'react';
import { useNavigate, Link } from "react-router-dom";
import { useFormik } from 'formik';
import * as Yup from 'yup';

import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Grid from '@mui/material/Grid';
import FormHelperText from '@mui/material/FormHelperText';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';


const validationSchema = Yup.object({
    username: Yup.string().required('Please enter a valid username'),
    password: Yup.string().required('Please enter a valid password')
})



export const Login = ()=>{

    const formik = useFormik({
        initialValues: {
            username: '',
            password: ''
        },
        validationSchema : validationSchema,
        onsubmit: handleLogin
    });

  
    const navigate = useNavigate();
  
    const handleKeyDown = (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        formik.handleSubmit();
      }
    };

    const handleLogin = (params) => {
      console.log("Loggin in");
    }

    // const handleLogin = (params) => {
    //   const payload = {
    //     username: params.username,
    //     password: params.password
    //   }
    //   const endpoint = KadalEndpoints.login;
    //   handlePostCaller(payload, endpoint)
    //     .then((response) => {
    //       if (response?.data && response?.data?.status_code === 200) {
    //         clearLocalStorage();
    //         setLocalStorage('access_token', response.data?.data?.access_token || '');
    //         setLocalStorage('refresh_token', response.data?.data?.refresh_token || '');
    //         navigate('/try-and-build', { replace: true });
    //       } else {
    //         alert('Login failed. Please try again.');
    //       }
    //     }).catch((err) => {
    //       clearLocalStorage();
    //       updateToaster({ show: true, message: 'Login failed. Please try again.', severity: 'error' });
    //       console.error('Failed to connect to the API', err);
    //     }).finally(() => {
    //       if (KadalCore.IS_LOCALHOST)
    //         navigate('/try-and-build');
    //     });
    // }

    return (
        <>
            <Container component="main" maxWidth="xs">
              <CssBaseline />
              <Box
                sx={{
                  marginTop: 8,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                }}
              >
                <Typography component="h1" variant="h1" sx={{ marginTop: 4, fontWeight: 600 }}>
                  Login
                </Typography>
                <Typography variant="body2" sx={{ marginTop: 2 }}>
                  Please fill your username and password below
                </Typography>
                <Box component="form" noValidate sx={{ mt: 1, width: '100%' }} onSubmit={formik.handleSubmit}>
                  <TextField
                    value={formik.values.username}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    error={formik.touched.username && Boolean(formik.errors.username)}
                    helperText={formik.touched.username && formik.errors.username}
                    margin="normal"
                    required
                    fullWidth
                    id="username"
                    name="username"
                    label="Username"
                    onKeyDown={handleKeyDown}
                  />
                  <TextField
                    value={formik.values.password}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    error={formik.touched.password && Boolean(formik.errors.password)}
                    helperText={formik.touched.password && formik.errors.password}
                    margin="normal"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    onKeyDown={handleKeyDown}
                  />
                  <Grid container sx={{ alignItems: 'center' }}>
                    <Grid item xs>
                      <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                        sx={{fontSize: '.875rem'}}
                        
                      />
                    </Grid>
                    <Grid item>
                      <Link to="/forgot-password" relative="path" className='semi-bold pointer' style={{ fontSize: '.875rem' }}>
                        Forgot password?
                      </Link>
                    </Grid>
                  </Grid>
                  <Button
                    type="button"
                    variant="contained"
                    color='secondary'
                    sx={{ mt: 3, mb: 2, px: 3 }}
                    onClick={formik.handleSubmit}
                  >
                    Login
                  </Button>
                </Box>
              </Box>
            </Container>
        </>
      );
}