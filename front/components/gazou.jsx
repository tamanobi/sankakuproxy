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
                <Image src={src} loaded={false}/>
            ) : (
                href ? (
                    <a href={href} title={href}><Image src={src} loaded={true}/></a>
                ) : (
                    <Image src={src}  loaded={true}/>
                )
            )}
        </figure>
    )
}
