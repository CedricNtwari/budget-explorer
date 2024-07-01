document.addEventListener('DOMContentLoaded', () => {
  const currentYearElement = document.getElementById('current-year')
  if (currentYearElement) {
    currentYearElement.textContent = new Date().getFullYear()
  }

  // Handle favorite/unfavorite click event
  const favoriteButtons = document.querySelectorAll('.btn-favorite')
  favoriteButtons.forEach((button) => {
    button.addEventListener('click', (e) => {
      e.preventDefault()
      fetch(button.href, {
        method: 'GET',
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === 'favorited') {
            button.classList.remove('btn-outline-danger')
            button.classList.add('btn-danger')
            button.innerHTML = '<i class="fa fa-heart"></i> Unfavorite'
          } else if (data.status === 'unfavorited') {
            button.classList.remove('btn-danger')
            button.classList.add('btn-outline-danger')
            button.innerHTML = '<i class="fa fa-heart"></i> Favorite'
          }
        })
        .catch((error) => console.error('Error:', error))
    })
  })

  window.getLocation = function () {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        document.getElementById('latitude').value = position.coords.latitude
        document.getElementById('longitude').value = position.coords.longitude
        document.forms[0].submit()
      })
    } else {
      alert('Geolocation is not supported by this browser.')
    }
  }
})
