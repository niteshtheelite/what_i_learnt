import { useState } from 'react'
import { Header } from './Components/Header'
import Header1 from './Components/Header'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Header title="Welcome to React" />
    <Header1 titles="Welcome to React App"/>
    </>
  )
}

export default App
