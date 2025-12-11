// Image Gallery Functionality
document.addEventListener('DOMContentLoaded', function() {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxClose = document.querySelector('.lightbox-close');
    const lightboxPrev = document.querySelector('.lightbox-prev');
    const lightboxNext = document.querySelector('.lightbox-next');
    
    let currentImageIndex = 0;
    let images = [];
    
    // Collect all images with content-image class
    document.querySelectorAll('.content-image img').forEach((img, index) => {
        images.push({
            src: img.src,
            caption: img.parentElement.nextElementSibling && img.parentElement.nextElementSibling.tagName === 'FIGCAPTION' ? 
                    img.parentElement.nextElementSibling.textContent : ''
        });
        
        // Add click handler to image
        img.addEventListener('click', function() {
            currentImageIndex = index;
            openLightbox(currentImageIndex);
        });
    });
    
    // Open lightbox
    function openLightbox(index) {
        if (images.length === 0) return;
        
        const image = images[index];
        lightboxImg.src = image.src;
        lightboxCaption.textContent = image.caption;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
    
    // Close lightbox
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto'; // Restore scrolling
    }
    
    // Next image
    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        openLightbox(currentImageIndex);
    }
    
    // Previous image
    function prevImage() {
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        openLightbox(currentImageIndex);
    }
    
    // Event listeners
    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    if (lightboxPrev) lightboxPrev.addEventListener('click', prevImage);
    if (lightboxNext) lightboxNext.addEventListener('click', nextImage);
    
    // Close by clicking outside image
    if (lightbox) {
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });
    }
    
    // Close with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
            closeLightbox();
        }
        
        // Navigation with arrow keys
        if (lightbox && lightbox.classList.contains('active')) {
            if (e.key === 'ArrowRight') {
                nextImage();
            } else if (e.key === 'ArrowLeft') {
                prevImage();
            }
        }
    });
});