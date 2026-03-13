import { useState } from "react"
import { fetchHello } from "./api"

export default function App() {
  const [msg, setMsg] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  async function handleApiCall() {
    setIsLoading(true)
    try {
      const data = await fetchHello()
      setMsg(data.message)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <>
      <button onClick={handleApiCall} disabled={isLoading}>
        {isLoading ? "Calling..." : "Call API"}
      </button>
      {msg && <p>{msg}</p>}
    </>
  )
}
