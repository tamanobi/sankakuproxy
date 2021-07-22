import Image from "./Image.jsx"

export default function Gazou(
    {
        href,
        src,
    }
) {
    if (href) {
        return <figure><a href={href} title={href}><Image src={src} /></a></figure>
    }
    return <figure><Image src={src} /></figure>
}
