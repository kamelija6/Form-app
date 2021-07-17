// let persons =[
//     {
//         id: 1,
//         fname:bu,
//         lname: bla,
//         age:25
//     },
//     {
//         id: 2,
//         fname:bu,
//         lname: bla,
//         age:25
//     },
//     {
//         id: 3,
//         fname:bu,
//         lname: bla,
//         age:25
//     },
//     {
//         id: 4,
//         fname:bu,
//         lname: bla,
//         age:25
//     },
//     {
//         id: 5,
//         fname:bu,
//         lname: bla,
//         age:25
//     }
// ];

// function Bozo( id, fname, lname, age){
//     this.id = id,
//     this.fname = fname,
//     this.lname = lname,
//     this.age = age;
// }

// Bozo.prototype.getFullname = function(){
//     return `My name is ${this.fname} ${this.lname} and my age is ${this.age}`;
// }

// class People{
//      constructor(fullname, aftor, godina){
//          this.fullname = fullname;
//          this.aftor = aftor;
//          this.godina = godina;
//      }
//      getFullname(){
//         return `My name is ${this.fullname} ${this.aftor} and my age is ${this.godina}`;
//     }
// }

// class Person extends People{
//     constructor(fullname, aftor, godina, mesec){
//         super(fullname, aftor, godina);
//         this.mesec = mesec;
//     }
// }
// const peoples = new People('Miki Mauns', 'teve novela', 1058 ," April");

// // function Klovan( id, fname, lname, age, city){
// //     Bozo.call(this, id, fname, lname, age);

// //     this.city = city;
// // }
// // Klovan.prototype = Object.create(Bozo.prototype);
// // const klovan1 = new Klovan( 2, "borco", "pedero", 25, "berovo");
// // const bozo1 = new Bozo(1, "Mile", "Bozovski", 22);

// document.getElementById('demo').innerHTML = peoples.getFullname();
