import Head from 'next/head'
import styles from '../styles/Home.module.css'
import { getAll } from '../lib/api'
import Image from '../components/Image.jsx'
import { useEffect, useState } from 'react'

export default function Home() {
  const [loaded, setLoaded] = useState(false)
  const [requesting, setRequesting] = useState(false)
  const [page, setPage] = useState(0)
  const [posts, setPosts] = useState([])

  async function nextFetch(page) {
    const IMAGE_API = process.env.NEXT_PUBLIC_IMAGE_API
    const API_ENDPOINT = process.env.NEXT_PUBLIC_API_ENDPOINT

    const query_params = new URLSearchParams({page})
    const res = await fetch(API_ENDPOINT + "/sankaku" + "?" + query_params, {
      method: 'GET',
    })
    const json = await res.json()
    if (json.errors) {
      console.error(json.errors)
      throw new Error('Failed to fetch API')
    }
    return json.body.map((post) => {
        post.src = IMAGE_API + "?path=" + encodeURIComponent(post.src)
        return post
    })
  }
  const next = async () => {
    setRequesting(true)
    setPosts(Array.prototype.concat(posts, await nextFetch(page + 1)))
    setPage(page + 1)
    setRequesting(false)
  }
  useEffect(async () => {
    if (!loaded) {
      setLoaded(true)
      await next()
    }
  })


  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        {posts.map((post, idx) => {
          return <figure key={idx}><a href={post.href} title={post.href}><Image src={post.src} /></a></figure>
        })}
      </main>
      <section>
        <button className={styles.button} onClick={async () => await next()} disabled={requesting}>go to {page + 1}</button>
      </section>
    </div>
  )
}

export async function getServerSideProps() {
  const allPosts = await getAll()
  return {
    props: {},
  }
}
