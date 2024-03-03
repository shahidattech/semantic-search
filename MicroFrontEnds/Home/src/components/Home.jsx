import { Suspense, useState } from "react";
import { useNavigate } from "react-router-dom";
import './Home.scss';

export default Home = ()=>{
    const [logInClicked, setIslogInClicked] = useState(false);
    const navigate = useNavigate();

    const goToLogin = () => {
        setIslogInClicked(true);
        navigate('/login');
      };

      return(
        <>
            <div>
                <div>
                    {logInClicked && (
                        <Suspense fallback={
                        <Backdrop
                            sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
                            open={false}
                        >
                            <CircularProgress color="inherit" />
                        </Backdrop>
                        }>
                        {/* <FirstApp /> */}
                        </Suspense>
                    )}
                </div>
                <header className="container-fluid position-relative p-0">
                    <div className="container">
                        <div className="d-flex justify-content-end mt-3">
                        <button onClick={goToLogin} style={{ border: 'none', backgroundColor: 'transparent', fontFamily: 'Open Sans, sans-serif', fontSize: '1.5rem', cursor: 'pointer' }}>Login</button>
                        </div>
                    </div>

                    <div className="container p-0 Bothome">
                        <div className="position-absolute kadal-position">
                        <p className="col-md-8 fs-4 adj-right">
                            An Embedding Management Platform.
                        </p>
                        <Button onClick={toggleReqDemo} disabled variant="contained" size="large">Request a Callback</Button>
                        </div>
                    </div>
                    <img src={first} loading="lazy" alt="" className="img-fluid h-100" />
                </header>
            </div>
        </>
      )
}