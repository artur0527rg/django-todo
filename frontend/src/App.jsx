import { RouterProvider, createBrowserRouter } from "react-router-dom"
import LoginRegister from "./components/LoginRegister/LoginRegister"
import Main from "./components/Main/Main"
import { useEffect, useState } from "react"
import PrivateRoute from "./components/PrivateRouter/PrivateRouter"

function App() {
  const [jwt, setJwt] = useState(localStorage.getItem('jwt'))
  useEffect(()=>{
    if (jwt){
      localStorage.setItem('jwt', jwt)
    }
  }, [jwt])

  const router = createBrowserRouter([
    {
      path: '/login',
      element: <LoginRegister jwt={jwt} setJwt={setJwt}/>,
    },
    {
      path: '/*',
      element: <PrivateRoute check={jwt}><Main jwt={jwt} setJwt={setJwt} /></PrivateRoute>,
    },
  ])

  return (
    <>
    <RouterProvider router={router}/>
    </>
  )
}

export default App
