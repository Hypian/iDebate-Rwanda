document.addEventListener('DOMContentLoaded', function () {
  var toggleButton = document.getElementById('mobile-menu-toggle');
  var drawer = document.getElementById('mobile-nav-drawer');

  if (toggleButton && drawer) {
    toggleButton.addEventListener('click', function () {
      var isHidden = drawer.classList.toggle('hidden');
      toggleButton.setAttribute('aria-expanded', String(!isHidden));
    });
  }
});
