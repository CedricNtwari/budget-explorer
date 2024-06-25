document.addEventListener('DOMContentLoaded', () => {
  const currentYearElement = document.getElementById('current-year')
  if (currentYearElement) {
    currentYearElement.textContent = new Date().getFullYear()
  }

  const postsContainer = document.getElementById('posts-container')
  const googleMapsMapId = postsContainer.dataset.googleMapsMapId

  if (!googleMapsMapId) {
    console.error('Google Maps Map ID is not defined.')
    return
  }

  async function initializeMaps() {
    const { AdvancedMarkerElement } = await google.maps.importLibrary('marker')

    document.querySelectorAll('.map-container').forEach((mapElement, index) => {
      var lat = parseFloat(mapElement.dataset.lat)
      var lng = parseFloat(mapElement.dataset.lng)
      var location = { lat: lat, lng: lng }

      var map = new google.maps.Map(mapElement, {
        zoom: 14,
        center: location,
        mapId: googleMapsMapId,
      })

      new AdvancedMarkerElement({
        position: location,
        map: map,
      })
    })
  }

  initializeMaps()

  let page = 2
  const loadMoreButton = document.getElementById('load-more')
  if (loadMoreButton) {
    loadMoreButton.addEventListener('click', function () {
      fetch(`?page=${page}`, {
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.posts) {
            postsContainer.insertAdjacentHTML('beforeend', data.posts)
            page += 1
            initializeMaps() // Reinitialize maps for new posts
            if (!data.has_next) {
              loadMoreButton.style.display = 'none'
            }
          }
        })
        .catch((error) => console.error('Error:', error))
    })
  }
})
