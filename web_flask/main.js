// document.getElementById('pickup-btn').addEventListener('click', function() {
//     var pickupForm = document.getElementById('pickup-form');
//     if (pickupForm.style.display === 'none' || pickupForm.style.display === '') {
//         pickupForm.style.display = 'block';
//     } else {
//         pickupForm.style.display = 'none';
//     }
// });


let requestBtn = document.getElementById("pickup-btn");
requestBtn.addEventListener('click', function(){
    let pickupForm = document.getElementById("pickup-form");
    if (pickupForm.style.display == "none"){
        pickupForm.style.display = 'block';
    }
});
