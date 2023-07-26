document.querySelectorAll('.Image-Container  img').forEach(Image =>{
    Image.onclick = () =>{
        document.querySelector('.Popup-Image').style.display = 'block';
        document.querySelector('.Popup-Image img').src = Image.getAttribute('src');
    }
});
document.querySelector('.Popup-Image span').onclick = () =>{
    document.querySelector('.Popup-Image').style.display = 'none';
}