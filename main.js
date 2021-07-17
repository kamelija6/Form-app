const name =  document.querySelector('.name');
const email = document.querySelector('.email');
const btn = document.querySelector('.btn');
const AddItme = document.querySelector('.AddItme');
const myForm = document.querySelector('.my-form');

//event listener

myForm.addEventListener('submit', onClick);

function onClick(e){
    e.preventDefault();
    if(name.value === "" || email === ""){
        const msg = AddItme.innerHTML('Please enter name and email');
        setTimeout(() => msg.remove(), 1000);
    }
    else{
        const Items = document.createElement('li');
        Items.classList.add('list');
        Items.appendChild(document.createTextNode(`The Name is : ${name.value}, and the Email is : ${email.value}`));


        AddItme.appendChild(Items);


        name.value = '';
        email.value = '';
    }
}

function localserver(list){
    if(name === "" || email === ""){
        localStorage.setItem(name, email);
    }
    for (let i = 0; i <= localStorage.length; i++){
       localStorage.setItem('name', 'Kamelija Arnautova');
       localStorage.setItem('email', 'kamelija@gmail.com');
       AddItme.innerHTML += localStorage;
    } 
}




