// Starting index (First image)
let currentIndex = 0;

// Select elements from the DOM
const slides = document.querySelectorAll('.slide');
const slider = document.querySelector('.slider');

function changeSlide(direction) {
    // Update index forward (1) or backward (-1)
    currentIndex += direction;

    // If at the last image and 'next' is clicked, go back to the first
    if (currentIndex >= slides.length) {
        currentIndex = 0;
    } 
    // If at the first image and 'prev' is clicked, go to the last
    else if (currentIndex < 0) {
        currentIndex = slides.length - 1;
    }

    // Calculate the percentage to shift (-100%, -200%, etc.)
    const offset = -currentIndex * 100;
    
    // Apply CSS transform to slide the images horizontally
    slider.style.transform = `translateX(${offset}%)`;
}