export default function Image(
    {
        src,
        height,
        width,
        alt,
    }
) {
    return <img src={src} alt={alt} loading="lazy" />
}
