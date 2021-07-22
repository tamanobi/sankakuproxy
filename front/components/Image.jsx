export default function Image(
    {
        src,
        height,
        width,
        alt,
    }
) {
    /* eslint-disable */
    return <img src={src} alt={alt} loading="lazy" />
    /* eslint-enable */
}
