import Image from "./Image.jsx"

export default function Gazou(
    {
        href,
        src,
        type,
        handleClick,
    }
) {
    return (
        <figure onClick={handleClick}>
            {type !== "loaded" ? (
                <Image src="" />
            ) : (
                href ? (
                    <a href={href} title={href}><Image src={src} /></a>
                ) : (
                    <Image src={src} />
                )
            )}
        </figure>
    )
}
