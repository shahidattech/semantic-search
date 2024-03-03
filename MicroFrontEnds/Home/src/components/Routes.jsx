import { createHashRouter, Navigate, RouterProvider }  from "react-router-dom";
import { Login } from 'Auth/login';

export default function Routes() {
    const router = createHashRouter([
        {
            path: "/login",
            lazy: false,
            Element: Login
        },
        {
            path: "/*",
            lazy: false,
            element: <Navigate to="/" replace />
          },
          {
            path: "*",
            lazy: false,
            element: <Navigate to="/" replace />
          }
    ], { basename: "localhost:8081" });

    return (
        <>
          <RouterProvider router={router} />
        </>
      );

}