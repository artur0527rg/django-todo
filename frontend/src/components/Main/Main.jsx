import { useEffect, useState } from 'react'
import './Main.css'
import swal from 'sweetalert';
import { Navigate } from 'react-router-dom';

const Main = ({ jwt, setJwt }) => {
    const [groups, setGroups] = useState()
    const [todos, setTodos] = useState()

    const [groupname, setGroupname] = useState('')
    const [todoname, setTodoname] = useState('')

    const [group, setGroup] = useState(undefined)

    let status = false
    useEffect(()=>{
        fetch(
            import.meta.env.VITE_API_URL + '/api/groups/',
            {
                headers: {
                    'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                }
            }
        )
        .then(response => {
            status = response.ok
            return response.json()
        })
        .then(response => {
            if(!status){
                setJwt(undefined)
            }
            setGroups(response)
        })

        if(group){
            fetch(
                import.meta.env.VITE_API_URL + '/api/groups/' + group + '/todo/',
                {
                    headers: {
                        'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                    }
                }
            )
            .then(response => {
                status = response.ok
                return response.json()
            })
            .then(response => {
                if(!status){
                    setJwt(undefined)
                }
                setTodos(response)
            })
        }

    }, [group])

    const groupHandler = (e) => {
        e.preventDefault();
        fetch(
            import.meta.env.VITE_API_URL + '/api/groups/',
            {
                method: "POST",
                headers: {
                    'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({title: groupname})
            }
        )
        .then(response => {
            status = response.ok
            return response.json()
        })
        .then(response => {
            if(!status){
                swal(JSON.stringify(response))
            } else {
                setGroups([response, ...groups])
            }
        })
    }

    const todoHandler = (e) => {
        e.preventDefault();
        fetch(
            import.meta.env.VITE_API_URL + '/api/groups/' + group + '/todo/',
            {
                method: "POST",
                headers: {
                    'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({title: todoname})
            }
        )
        .then(response => {
            status = response.ok
            return response.json()
        })
        .then(response => {
            if(!status){
                swal(JSON.stringify(response))
            } else{
                setTodos([response, ...todos])
            }
        })
    }

    const deleteGroup = (e, key) => {
        e.preventDefault()
        if(key===group){
            setGroup(undefined)
        }
        fetch(
            import.meta.env.VITE_API_URL + '/api/groups/' + key +'/',
            {
                method: "DELETE",
                headers: {
                    'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                    'Content-Type':'application/json'
                },
            }
        )
        .then(response => {
            if(!response.ok){
                swal('Something went wrong, try reloading the page')
            } else{
                setGroups(groups.filter((e)=> e.id !== key))
            }
        })
    }

    const deleteTodo = (e, key) => {
        e.preventDefault()
        fetch(
            import.meta.env.VITE_API_URL + '/api/groups/' + group +'/todo/' + key + '/',
            {
                method: "DELETE",
                headers: {
                    'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                    'Content-Type':'application/json'
                },
            }
        )
        .then(response => {
            if(!response.ok){
                swal('Something went wrong, try reloading the page')
            } else{
                setTodos(todos.filter((e)=> e.id !== key))
            }
        })
    }

    const selectTodo = (key) => {
        console.log(todos)
        const cur = todos.find(e => e.id == key)
        fetch(
            import.meta.env.VITE_API_URL + '/api/groups/' + group +'/todo/' + key + '/',
            {
                method: "PATCH",
                headers: {
                    'Authorization': import.meta.env.VITE_TOKEN_TYPE + ' ' + jwt,
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({is_checked:!cur['is_checked']})
            }
        )
        .then(response => {
            console.log(response)
            if(!response.ok){
                swal('Something went wrong, try reloading the page')
            } else{
                setTodos(todos.map(e=> e.id===key?{...e, is_checked:!e.is_checked}:e))
            }
        })
    }

    const logOut = () => {
        setJwt(undefined)
    }

    return (
        <>
        <div className='content-container'>
        <div className='item'>
            <form onSubmit={e=>groupHandler(e)}>
                <input
                    type='text'
                    placeholder='Group name'
                    onChange={(e)=> setGroupname(e.target.value)}
                    value={groupname}
                />
                <input
                    type="submit"
                    value='Create group'
                />
            </form>
            <div className='list'>
            {groups && groups.map((item)=>{
                return <>
                    <div 
                    className={item.id == group? 'active': ''}
                    key={item.id}>
                    <div onClick={()=>setGroup(item.id)} style={{display: 'inline'}}>
                    {item.title}
                    </div>
                    <input
                        type='Submit'
                        style={{ marginLeft: 5,  padding: 0, fontSize: '1.2rem', width: 40, color: 'red'}}
                        value="Del"
                        onClick={(e)=> deleteGroup(e, item.id)}
                    />
                </div>
                </> 
            })}
            </div>
        </div>
        {group &&
        <div className='item'>
            <form onSubmit={e=>todoHandler(e)} >
                <input
                    type='text'
                    placeholder='Task name'
                    onChange={(e)=> setTodoname(e.target.value)}
                    value={todoname}
                />
                <input
                    type="submit"
                    value='Create task'
                />
            </form>
            <div className='list'>
            {todos && todos.map((item)=>{
                return <div
                    key={item.id}>
                   <div
                   className={item.is_checked?'is_checked':''}
                   onClick={()=>selectTodo(item.id)}
                   style={{ display: 'inline' }}>
                    {item.title}
                    </div>
                    <input
                        type='Submit'
                        style={{ marginLeft: 5,  padding: 0, fontSize: '1.2rem', width: 40, color: 'red'}}
                        value="Del"
                        onClick={(e)=> deleteTodo(e, item.id)}
                    />
                </div>
            })}
            </div>
        </div>
        }
    </div>
    <img
    onClick={logOut}
    className="sticky"
    src="https://cdn.icon-icons.com/icons2/2518/PNG/512/logout_icon_151219.png"/>
    </>
    )
}

export default Main