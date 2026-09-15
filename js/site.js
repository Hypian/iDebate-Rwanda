document.addEventListener('DOMContentLoaded', function () {
  var toggleButton = document.getElementById('mobile-menu-toggle');
  var drawer = document.getElementById('mobile-nav-drawer');

  if (toggleButton && drawer) {
    function closeDrawer() {
      drawer.classList.add('hidden');
      toggleButton.setAttribute('aria-expanded', 'false');
    }

    toggleButton.addEventListener('click', function () {
      var isOpen = drawer.classList.toggle('hidden') === false;
      toggleButton.setAttribute('aria-expanded', String(isOpen));
    });

    drawer.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        closeDrawer();
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        closeDrawer();
      }
    });
  }
});
