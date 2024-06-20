let slidesList = document.getElementById('slides-list');
let slides = document.querySelectorAll('.my-slides');
let next = document.getElementById('next-arrow');
let prev = document.getElementById('prev-arrow');

let currentSlide = 0;

updateSlide();

next.addEventListener('click', () => {
    if(currentSlide < slides.length -1) {
        currentSlide++;
    } else {
        currentSlide = 0;
    }
    updateSlide();
});

prev.addEventListener('click', () => {
    if (currentSlide > 0 ) {
        currentSlide--;
    } else {
        currentSlide = slides.length - 1;
    }
    updateSlide();
});

function updateSlide() {
    let slideWidth = slides[0].clientWidth;
    slidesList.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}
