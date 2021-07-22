const API_URL = process.env.API_URL
const IMAGE_API = process.env.IMAGE_API

async function fetchAPI(query, { variables } = {}) {
  const res = await fetch(API_URL, {
    method: 'GET',
  })

  const json = await res.json()
  if (json.errors) {
    console.error(json.errors)
    throw new Error('Failed to fetch API')
  }
  return json.body
}

export async function getAll() {
    const data = await fetchAPI()
    return data.map((post) => {
        post.src = IMAGE_API + "?path=" + encodeURIComponent(post.src)
        return post
    })
}
