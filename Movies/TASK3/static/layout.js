document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('nav-toggle');
  const links = document.getElementById('nav-links');
  
  if (btn && links) {
    btn.addEventListener('click', (e) => {
      e.stopPropagation(); // Prevents click from immediately triggering the document listener
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
      links.classList.toggle('active');
    });

    document.addEventListener('click', (e) => {
      if (!links.contains(e.target) && e.target !== btn) {
        links.classList.remove('active');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }
});

document.addEventListener('DOMContentLoaded',() => {
  
})