const modalStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    position: 'fixed',
    width: '100vw',
    height: '100vh',
    backgroundColor: 'rgba(0, 0, 0, 0.9)',
    zIndex: 100,
};

export default function Modal(
    {
        children,
        handleClose
    }
) {
    function onClose(event) {
        event.preventDefault()
        handleClose(event)
    }

    return <div style={modalStyle} onClick={onClose}>{children}</div>
}
