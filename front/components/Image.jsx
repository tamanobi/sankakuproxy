import { useState } from "react";
import styles from '../styles/Home.module.css'

export default function Image(
    {
        src,
        height,
        width,
        alt,
        loaded,
    }
) {
    const [canShow, setCanShow] = useState(false)

    return (
        <div className={(loaded  && canShow) ? styles.loaded : styles.skeleton}>
            {/* eslint-disable */}
            <img src={src} alt={alt} onLoad={() => {setCanShow(true)}}loading="eager" />
            {/* eslint-enable */}
        </div>
    )
}
