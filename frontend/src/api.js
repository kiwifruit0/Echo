const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function fetchHello() {
  const res = await fetch(`${API_URL}/test/hello`)
  if (!res.ok) {
    throw new Error("Failed to call API")
  }
  return res.json()
}