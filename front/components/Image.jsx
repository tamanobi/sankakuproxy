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

    return (
        <div className={loaded ? styles.loaded : styles.skeleton}>
            {/* eslint-disable */}
            <img className={styles.hogehoge} src={src} alt={alt} onLoad={() => {setLoaded(true)}} loading="eager" />
            {/* eslint-enable */}
        </div>
    )
}
