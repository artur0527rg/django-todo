import { useState } from "react"
import { Navigate } from "react-router-dom"

const PrivateRoute = ({ check, children }) => {
    return check? children : <Navigate to='/login'/>
}

export default PrivateRoute