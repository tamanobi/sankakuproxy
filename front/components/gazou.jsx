import Image from "./Image.jsx"

export default function Gazou(
    {
        href,
        src,
        type,
    }
) {
    if (type !== "loaded") {
        return <figure><Image src="" /></figure>
    }
    if (href) {
        return <figure><a href={href} title={href}><Image src={src} /></a></figure>
    }
    return <figure><Image src={src} /></figure>
}
