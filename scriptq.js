document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.form-slide');
    let currentSlide = 0;
    
    slides[currentSlide].classList.add('active');

    window.nextSlide = function(step) {
        slides[currentSlide].classList.remove('active');
        currentSlide += step;
        slides[currentSlide].classList.add('active');
    };

    window.prevSlide = function(step) {
        slides[currentSlide].classList.remove('active');
        currentSlide -= step;
        slides[currentSlide].classList.add('active');
    };

    document.getElementById('skinForm').addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Form submitted successfully!');
    });
});