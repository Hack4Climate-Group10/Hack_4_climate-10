document.getElementById('pickup-btn').addEventListener('click', function() {
    var pickupForm = document.getElementById('pickup-form');
    if (pickupForm.style.display === 'none' || pickupForm.style.display === '') {
        pickupForm.style.display = 'block';
    } else {
        pickupForm.style.display = 'none';
    }
});

