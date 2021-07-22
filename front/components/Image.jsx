import { useState } from "react";
import styles from '../styles/Home.module.css'

export default function Image(
    {
        src,
        height,
        width,
        alt,
    }
) {
    const [loaded, setLoaded] = useState(false)

    /* eslint-disable */
    return <img className={loaded ? "" : styles.skelton} src={src} alt={alt} onLoad={() => {setLoaded(true)}} loading="lazy" />
    /* eslint-enable */
}
