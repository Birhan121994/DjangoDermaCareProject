const filterBtn = document.querySelector('#filter');
const catList = document.querySelector('.DiseaseCategory');
const filterBtn1 = document.querySelector('#filter1');
const catList1 = document.querySelector('.DiseaseCategory1');



filterBtn.addEventListener('click',() => {
    if(catList.style.display === 'none'){
        catList.style.display = 'block';
    }else{
        catList.style.display = 'none';
    }
});

filterBtn1.addEventListener('click',() => {
    if(catList1.style.display === 'none'){
        catList1.style.display = 'block';
    }else{
        catList1.style.display = 'none';
    }
});


document.querySelectorAll('.Image-Container  img').forEach(Image =>{
    Image.onclick = () =>{
        document.querySelector('.Popup-Image').style.display = 'block';
        document.querySelector('.Popup-Image img').src = Image.getAttribute('src');
    }
});
document.querySelector('.Popup-Image span').onclick = () =>{
    document.querySelector('.Popup-Image').style.display = 'none';
}

