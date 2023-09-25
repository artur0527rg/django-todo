import { useState } from 'react'
import './LoginRegister.css'
import swal from 'sweetalert';
import { Navigate } from 'react-router-dom';

const LoginRegister = ({ jwt, setJwt }) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')

    const onLogin = (e) => {
        e.preventDefault();
        const data = {
            username,
            password,
        }
        let status = 0
        fetch(
            import.meta.env.VITE_API_URL+'/api/token/',
            {
                method:'POST',
                body:JSON.stringify(data),
                headers: {'Content-Type':'application/json'}
            })
        .then(response => {
            status = response.ok
            return response.json()
        })
        .then(response => {
            if(!status){
                let message = ''
                for(let key in response){
                    message+= `${key} `+ JSON.stringify(response[key]) +'\n'
                }
                swal(message)
            } else{
                setJwt(response['access'])
                
            }
            
        })
        .catch(e=>console.log(e))
    }

    const onRegister = (e) => {
        e.preventDefault();
        const data = {
            username,
            password,
            email,
        }
        let status = 0
        fetch(
            import.meta.env.VITE_API_URL+'/api/user/',
            {
                method:'POST',
                body:JSON.stringify(data),
                headers: {'Content-Type':'application/json'}
            })
        .then(response => {
            status = response.ok
            return response.json()
        })
        .then(response => {
            if(!status){
                let message = ''
                for(let key in response){
                    message+= `${key} `+ JSON.stringify(response[key]) +'\n'
                }
                swal(message)
            } else{
                swal('Login to your account')
            }
            
        })
        .catch(e=>console.log(e))
    }

    return <div className='login-container'>
        {jwt && <Navigate to='/'/>}
        <div className='login-item'>
            <form onSubmit={(e)=>onLogin(e)}>
                <input
                    type='text'
                    placeholder='Username'
                    onChange={(e)=>setUsername(e.target.value)}
                    value={username}
                />
                <input
                    type='password'
                    placeholder='Password'
                    onChange={(e)=>setPassword(e.target.value)}
                    value={password}
                />
                <input
                    type="submit"
                    value='Login'
                />
            </form>
        </div>
        <div className='login-item'>
            <form onSubmit={(e)=>onRegister(e)}>
                <input
                    type='text'
                    placeholder='Username'
                    onChange={(e)=>setUsername(e.target.value)}
                    value={username}
                />
                <input
                    type='email'
                    placeholder='Email'
                    onChange={(e)=>setEmail(e.target.value)}
                    value={email}
                />
                <input
                    type='password'
                    placeholder='Password'
                    onChange={(e)=>setPassword(e.target.value)}
                    value={password}
                />
                <input
                    type="submit"
                    value='Register'
                />
            </form>
        </div>

    </div>
}

export default LoginRegister